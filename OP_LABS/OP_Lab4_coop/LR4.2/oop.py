from struct import pack, unpack  # For adding info to binary files
from scipy import interpolate  # interpolation function
import numpy as np  # interpolation works only to numpy arrays
from sys import argv   # To take cli arguments
 
class FileWorker:
    def __init__(self, filename):
        self.filename = filename
        self.__head = {}
        self.__raw_data = None

    def get_file_properties(self):
        with open(self.filename, 'rb') as f:
            # Processing RIFF chunk descriptor
            chunk_id = f.read(4)   # Here we get Id of chunk
            if chunk_id != b'RIFF':  # Checking file type validity
                print("File is not RIFF-type")
                return None
            
            self.__head['chunk_id'] = 'RIFF'  # Declared file chunk type

            chunk_size = unpack("<L", f.read(4))[0]  # Finding chunk size
            self.__head['chunk_size'] = chunk_size  # Declared chunk size

            file_format = f.read(4)
            if file_format != b'WAVE':  # Checking file format
                print("File is not WAV format")
                return None
            self.__head['file_format'] = 'WAVE'  # Declaring file format
            
            # Processing fmt and data subchunk
            while f.tell() < 8 + chunk_size: # Scrolling through left file
                tag = f.read(4)   # Checking every byte combination
                sub_chunk_size = unpack('<L', f.read(4))[0]
                # Checking what info contains a tag we found 
                if tag == b'fmt ':   # 'fmt ' subchunk
                    self.__head['sub_chunk_1_id'] = 'fmt '
                    self.__head['sub_chunk_1_size'] = sub_chunk_size
                    fmt_data = f.read(sub_chunk_size)
                    fmt, num_channels, sample_rate, byte_rate, block_align, bits_per_sample = unpack('<HHLLHH', fmt_data)
                    self.__head['audio_format'] = fmt
                    self.__head['num_channels'] = num_channels
                    self.__head['sample_rate'] = sample_rate
                    self.__head['byte_rate'] = byte_rate
                    self.__head['block_align'] = block_align
                    self.__head['bits_per_sample'] = bits_per_sample
                # 'data' subchunk
                elif tag == b'data':
                    self.__head['sub_chunk_2_id'] = 'data'
                    self.__head['sub_chunk_2_size'] = sub_chunk_size
                    self.__raw_data = f.read(sub_chunk_size)
                    break   # We have already read all data
                # In case subchunk type not 'fmt ' or 'data'
                else:
                    f.seek(sub_chunk_size, 1) 

    
    def checking_file_validity(self):
        return True if self.__head['bits_per_sample'] == 8 and self.__head['num_channels'] == 1 else False
    
    def get_head(self):
        return self.__head

    def get_raw_data(self):
        return self.__raw_data

class Coordinator:
    def __init__(self, times, head):
        self.times = times  # How much to slow
        self.head = head   # File header

    def finding_old_coords(self):
        x = 0
        old_coords = []   # Ends of old unit segments
        while x < self.head['sub_chunk_2_size']:
            old_coords.append(x) # Collecting all possible old x's
            x += 1

        return old_coords

    def finding_new_coords(self):
        x = 0
        new_coords = []    # Ends of new unit segments
        while x < self.head['sub_chunk_2_size'] - 1:
            new_coords.append(x)  # Incresing amount of samples
            x += (1 / self.times)

        return new_coords

    def finding_chunk_sizes(self, new_coords):
        new_sub_chunk_2_size = len(new_coords) # Finding new characteristics of resulting file
        new_chunk_size = self.head['chunk_size'] - self.head['sub_chunk_2_size'] + new_sub_chunk_2_size
        self.head['sub_chunk_2_size'] = new_sub_chunk_2_size  # Such as subchunk2 size
        self.head['chunk_size'] = new_chunk_size              # and chunkSize 
        return new_sub_chunk_2_size

class Interpolator:
    def __init__(self, old_coords, new_coords, new_sub_chunk_2_size, raw_data):
        self.__old_coords = old_coords
        self.__new_coords = new_coords
        self.__new_sub_chunk_2_size = new_sub_chunk_2_size
        self.__raw_data = raw_data

    def __create_graph(self):  # Find by interpolation
        return interpolate.interp1d(np.array(self.__old_coords), np.array(list(self.__raw_data)))

    def __create_samples(self, graph):
        new_samples = graph(np.array(self.__new_coords)).tolist()  # Calculating from function
        for i in range(self.__new_sub_chunk_2_size):
            new_samples[i] = round(new_samples[i])  # Making samples whole numbers
        return new_samples

    def perform(self):   # Perform a result of work
        graph = self.__create_graph()
        new_samples = self.__create_samples(graph)
        return graph, new_samples

    
class Starter:
    def __init__(self, filename):
        self.filename = filename

    def printer(self):
        with open(self.filename, 'rb') as f:
            starter = f.read()[:44]
            print(starter)


class WAVWriter:
    def __init__(self, head, new_samples):
        self.head = head
        self.new_samples = new_samples

    def writer(self, filename):
        with open(filename, 'wb') as out:
            for el in self.head.keys():   # Checking our dictionary
                if type(self.head[el]) is str:
                    out.write(pack('>4s', self.head[el].encode('utf-8')))  # Write encoded info
                elif el in ['audio_format','num_channels','block_align', 'bits_per_sample']:
                    out.write(pack('<H', self.head[el]))   # Writing numerical info (2-bytes)
                else:
                    out.write(pack('<I', self.head[el]))   # Writing 4-byte non-string parameters

            for sample in self.new_samples:  # Writing music data
                out.write(pack('>B', sample))


class AudioApp:
    def __init__(self, inp, out, speed):
        self.inp = inp
        self.out = out
        self.speed = speed

    
    def main_menu(self):
        print('This program slows down 8-bit mono .wav files')
        print('You can also speed them up by typing [xxx.yyy]<1')
        print("Command format: <input.wav> <output.wav> <xxx.yyy>")
        
        input_file, output_file, speed = self.inp, self.out, self.speed
        speed = float(speed)
        fw = FileWorker(input_file)
        fw.get_file_properties()
        head = fw.get_head()
        raw_data = fw.get_raw_data()

        if fw.checking_file_validity():
            cr = Coordinator(speed, head)
            old_coords = cr.finding_old_coords()
            new_coords = cr.finding_new_coords()
            new_sub_chunk_2_size = cr.finding_chunk_sizes(new_coords)
            
            ir = Interpolator(old_coords, new_coords, new_sub_chunk_2_size, raw_data)
            graph, new_samples = ir.perform()

            ww = WAVWriter(head, new_samples)
            ww.writer(output_file)

        else:
            print("File is not valid")
            return

inp = argv[1]
out = argv[2]
speed = argv[3]
app = AudioApp(inp, out, speed)
app.main_menu()
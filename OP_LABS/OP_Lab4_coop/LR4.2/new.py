import struct
Head = {}
rawData = None
from scipy import interpolate  # функция интерполяции
import numpy as np  # функция интерполяции работает с numpy массивами


# print('This program slows down 8-bit mono .wav files')
# print('You can also speed them up by typing [xxx.yyy]<1')
# print('\n')
# user = input('[inputfilename.wav] [outputfilename.wav] [xxx.yyy](times slower): ').split()  # по методичке
# filename = user[0]
# outname = user[1]
# q = float(user[2])

filename = 'laugh.wav'  # user[0]
outname = 'laugh2.wav'  # user[1]
q = 3.5   # float(user[2])


with open(filename, "rb") as f:
    chunkId = f.read(4)
    if chunkId != b'RIFF':  # Checking file type
        print('not a valid RIFF file')
        exit(1)
    Head['ChunkID'] = 'RIFF'

    chunkSize = struct.unpack('<L', f.read(4))[0]
    # print(chunkSize)
    Head['ChunkSize'] = chunkSize
    format = f.read(4)
    if format != b'WAVE':    # Checking format
        print('not a WAV file')
        exit(1)
    Head['Format'] = 'WAVE'

    while f.tell() < 8 + chunkSize:
        tag = f.read(4)
        subchunkSize = struct.unpack('<L', f.read(4))[0]
        if tag == b'fmt ':
            Head['Subchunk1ID'] = 'fmt '
            Head['Subchunk1Size'] = subchunkSize
            fmtData = f.read(subchunkSize)
            fmt, numChannels, sampleRate, byteRate, blockAlign, bitsPerSample = struct.unpack('<HHLLHH', fmtData)
            Head['AudioFormat'] = fmt
            Head['NumChannels'] = numChannels
            Head['SampleRate'] = sampleRate
            Head['ByteRate'] = byteRate
            Head['BlockAlign'] = blockAlign
            Head['BitsPerSample'] = bitsPerSample

        elif tag == b'data':
            Head['Subchunk2ID'] = 'data'
            Head['Subchunk2Size'] = subchunkSize
            rawData = f.read(subchunkSize)
            break

        else:
            f.seek(subchunkSize, 1)

assert(Head['BitsPerSample'] == 8)
assert(Head['NumChannels'] == 1)


x = 0
old_coords = []  # концы старых единичных отрезков
while x < Head['Subchunk2Size']:
    old_coords.append(x)   # collecting all old x's
    x += 1

x = 0
new_coords = []  # концы новых единичных отрезков
while x < Head['Subchunk2Size'] - 1:     # Increasing amount of samplesand getting new x coords
    new_coords.append(x)
    x += (1 / q)

new_subchunk2Size = len(new_coords)   # Finding new characteristics of resulting file
new_chunkSize = Head['ChunkSize'] - Head['Subchunk2Size'] + new_subchunk2Size
Head['Subchunk2Size'] = new_subchunk2Size  # Such as subchunk2 size
Head['ChunkSize'] = new_chunkSize    # and chunkSize 

# finding new function that depends on new x coords
graph = interpolate.interp1d(np.array(old_coords), np.array(list(rawData)))  # 3 параметр функции - квадратная, кубическая.. см. scipy interpolate
# Finding new samples from defined function
new_samples = graph(np.array(new_coords)).tolist()  # через полученную функцию пропускаем новые переменные

for i in range(new_subchunk2Size):  # Making samples whole numbers
    new_samples[i] = round(new_samples[i])


with open(filename, "rb") as f:  # Printing starters
    starter = f.read()[:44]
    print(starter)


with open(outname, 'wb') as out:
    for el in Head.keys():    # Checking our dictionary
        print(el, Head[el])
        if type(Head[el]) is str:
            out.write(struct.pack('>4s', Head[el].encode('utf-8')))    # Write encoded string
        elif el in ['AudioFormat','NumChannels','BlockAlign', 'BitsPerSample']:   
            out.write(struct.pack('<H', Head[el]))   # Write useful information
        else:        # TTRRRRRRRRRYYYYYYY SWAP H AND I
            out.write(struct.pack('<I', Head[el]))   # Write 4-byte non-string params
    for sample in new_samples:     # Writing music data
        out.write(struct.pack('>B', sample)) 


with open(outname, "rb") as f:  # Printing starters
    starter = f.read()[:44]
    print(starter)
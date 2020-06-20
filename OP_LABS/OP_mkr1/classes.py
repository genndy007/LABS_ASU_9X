class FileWorker:
    def __init__(self, start_file, result_file, N):   # constructor
        self.start_file = start_file
        self.result_file = result_file
        self.N = N

    def __del__(self):                                 # destructor
        print("File worker has been deleted")

    def output_file(self, filename):              # outputs file to console
        with open(filename) as file:
            for line in file:
                print(line)

    def write_to_file(self, filename):             # to write into file
        with open(filename, 'w') as file:
            text = input()
            while text != '':
                file.write(f"{text}\n")
                text = input()

    def lines_counter(self, filename):       # counts lines in file
        num_lines = 0
        with open(filename) as file:
            for line in file:
                num_lines += 1
        return num_lines

    def write_to_result_file(self, num_lines):      # writes needed lines
        when_writing = num_lines - self.N + 1       # to new file
        with open(self.result_file, "w") as result:
            with open(self.start_file) as start:
                line_num = 0
                for line in start:
                    line_num += 1
                    if line_num >= when_writing:
                        result.write(line)

    def find_doubles(self, filename):        # finds repeating lines
        array_lines = []
        deletions = 0
        repeated = []

        with open(filename) as file:
            for line in file:
                array_lines.append(line)
        for i in range(len(array_lines)):
            for j in range(i + 1, len(array_lines)):
                if array_lines[i] == array_lines[j]:
                    repeated.append(array_lines[j])
                    deletions += 1

        with open(filename) as file:
            with open('new_result.txt', 'w') as result:
                for line in file:
                    if len(repeated) == 0:
                        result.write(line)
                        continue
                    for i in range(len(repeated)):
                        if line == repeated[i]:
                            continue
                        else:
                            result.write(line)

        return deletions


start_file = input("Enter start file: ")
result_file = input("Enter result file: ")
N = int(input("Enter N: "))

fw = FileWorker(start_file, result_file, N)

fw.write_to_file(start_file)
lines_in_start_file = fw.lines_counter(start_file)
fw.write_to_result_file(lines_in_start_file)
deletions = fw.find_doubles(result_file)
print("Start file looks like:")
fw.output_file(start_file)
print("Result file looks like:")
fw.output_file('new_result.txt')


print("Deletions:", deletions)

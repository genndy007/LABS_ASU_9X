result_file = open("result.txt", 'w')
start_file = input("Enter your start file: ")
n = int(input("Enter N:"))
start_file_lines = 0
with open(start_file) as start:
    for line in start:
        start_file_lines += 1

when_writing = start_file_lines - n + 1
with open(start_file) as start:
    line_number = 0
    for line in start:
        line_number += 1
        if line_number >= when_writing:
            result_file.write(line)
result_file.close()

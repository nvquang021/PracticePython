def split_and_join(line):
    line = line.split()
    result = '-'.join(line)
    return result
line = input()
b = split_and_join(line)
print(b)
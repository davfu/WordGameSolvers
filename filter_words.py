import re

# open and read input file
with open('test.txt', 'r') as file: lines = file.readlines()
print("Original word count: " + str(len(lines)))
# define chars not wanted in string
pattern = r'[0-9!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~]'
# filter out lines that match pattern
filtered_lines = [line.lower() for line in lines if not re.search(pattern, line)]
# rewrite input file
with open('test.txt', 'w') as file: file.writelines(filtered_lines)
print("Filtered word count: " + str(len(filtered_lines)))
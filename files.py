f = open('test.txt')
print(f.read())
print(f.read()) # nothing will print because the cursor is at the end, you need to reset it

f.seek(0) # resets th cursor to the start of file
print(f.readlines()) # returns each line as an item in a list

# avoid calling readlines on a very large file, because it loads and saves the entire list in memory

for line in open('test.txt'):
    print(line)
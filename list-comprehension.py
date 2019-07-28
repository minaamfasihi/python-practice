l = []

for letter in 'word':
    l.append(letter)

print(l) # output: ['w', 'o', 'r', 'd']

l = [letter for letter in 'sentence']
print(l) # output: ['s', 'e', 'n', 't', 'e', 'n', 'c', 'e']

lst = [x**2 for x in range(0, 11)]
print(lst) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

lst = [number for number in range(11) if number % 2 == 0]
print(lst) # output: [0, 2, 4, 6, 8, 10]

celsius = [0, 10, 20.1, 34.5]
fahrenheit = [temp for temp in celsius]
print(fahrenheit) # output: [0, 10, 20.1, 34.5]

fahrenheit = [(temp * (9 / 5.0) + 32) for temp in celsius]
print(fahrenheit) # output: [32.0, 50.0, 68.18, 94.1]

# Final result would be x ** 4 in range(11)
lst = [x ** 2 for x in [x**2 for x in range(11)]]
print(lst) # output: [0, 1, 16, 81, 256, 625, 1296, 2401, 4096, 6561, 10000]

lst = [x for x in range(50) if x % 3 == 0]
print(lst) # output: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]

st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word)

st = 'Create a list of the first letters of every word in the string'
lst = [word[0] for word in st]
print(lst)
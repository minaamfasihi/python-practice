from functools import reduce

phrase = 'The quick brown fox jumps over a lazy dog'

def word_lengths(sentence):
    return list(map(len, sentence.split()))

print(word_lengths(phrase))

def digits_to_num(digits):
    return reduce(lambda x, y : x * 10 + y, digits)

print(digits_to_num([1, 2, 3]))

def filter_words(word_list, letter):
    return list(filter(lambda x: x.startswith(letter), word_list))

print(filter_words(['sea', 'soup', 'john', 'sentiment'], 's'))

def concatenate(L1, L2, connector):
    return [word1 + connector + word2 for (word1, word2) in zip(L1, L2)]

print(concatenate(['A', 'B'], ['a', 'b'], '-'))

def d_list(L):
    return {key: value for value, key in enumerate(L)}

print(d_list(['a', 'b', 'c']))

def count_match_index(L):
    return len([value for key, value in enumerate(L) if key == value])

print(count_match_index([0, 2, 2, 1, 5, 5, 6, 10]))

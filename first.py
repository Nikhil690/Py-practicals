import os

try:
    file_to_read = open("doge.txt", "r") 

    data = file_to_read.read()

    num_char = len(data)
    num_words = len(data.split())
    num_lines = len(data.splitlines())

    print("number of characters: ",num_char)
    print("number of lines: ",num_lines)
    print("number of words: ",num_words)

    freq = {}

    for i in data:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    print("frequency of words",str(freq))

    words = data.split()
    words_reversed = words[::-1]

    print("words in reversed order: ",words_reversed)

except FileNotFoundError:
    print("file not found")
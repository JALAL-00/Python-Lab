input_line = input("Enter a line of text: ")

words = input_line.split()

longest_word = ''
shortest_word = words[0]  

for word in words:

    if len(word) > len(longest_word):
        longest_word = word
    
    if len(word) < len(shortest_word):
        shortest_word = word
        
print("Longest word:", longest_word)
print("Shortest word:", shortest_word)

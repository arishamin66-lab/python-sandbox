def word_analyzer(sentence):
    a = sentence.split(" ")
    count_words = len(a)
    count_characters = 0
    vowels = 0
    longest_word = a[0]
    unique_words = set(a)
    for ch in a:
        count_characters += len(ch)
        if len(ch) > len(longest_word):
            longest_word = ch
        for b in ch:
            if b == "A" or b == "a" or b == "e" or b == "E" or b == "I" or b == "i" or b == 'o' or b == "O" or b =="U" or b =="u": 
                vowels += 1

    print(vowels)
    print(longest_word)
    print(unique_words)
    print(count_characters)
    print(count_words)

a = "Hello my name is arish"

print(word_analyzer(a))
def word_analyzer(sentence):
    # Split the sentence into words
    a = sentence.split(" ")
    count_words = len(a)
    count_characters = 0
    vowels = 0
    longest_word = a[0]
    # A set automatically drops duplicate words
    unique_words = set(a)

    for ch in a:
        count_characters += len(ch)
        if len(ch) > len(longest_word):
            longest_word = ch
        for b in ch:
            if b in "AaEeIiOoUu":
                vowels += 1

    print(vowels)
    print(longest_word)
    print(unique_words)
    print(count_characters)
    print(count_words)

    # BUG FIX: the function only printed values and had no return statement,
    # so it implicitly returned None. The original code then did
    # print(word_analyzer(a)), which printed "None" after all the stats.
    # Returning the values here lets the caller decide what to do with them.
    return count_words, count_characters, vowels, longest_word, unique_words


a = "Hello my name is arish"

# word_analyzer already prints the stats internally, so we don't need to
# print its return value again here.
word_analyzer(a)

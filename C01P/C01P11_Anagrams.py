def anagrams(word1, word2):
    word1 = word1.lower().replace(' ', '')
    word2 = word2.lower().replace(' ', '')

    if not len(word1) == len(word2):
        return False

    for letter in word1:
        if letter not in word2:
            return False

    return True


print(anagrams("listen", "silent") is True)
print(anagrams("LISTEN", "silent") is True)
print(anagrams("New York Times", "monkeys write") is True)
print(anagrams("snake", "sssnakee") is False)

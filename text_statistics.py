import string
import os
import json

def text_stat(filename):
    # check for correct input
    if not os.path.exists(filename):
        return {"error": "File not found"}

    latin_alphabet = string.ascii_lowercase
    cyrillic_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    cyrillic = dict.fromkeys(cyrillic_alphabet, (0,0))
    latin = dict.fromkeys(latin_alphabet, (0, 0))
    paragraph_amount = 1
    bilingual_word_amount = 0
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        # process words in text
        paragraph_amount = text.count("\n")
        words = text.lower().split()
        for word in words:
            cyrillic_encounter = dict.fromkeys(cyrillic_alphabet, False)
            latin_encounter = dict.fromkeys(latin_alphabet, False)

            for ch in word:
                if ch in latin:
                    char_counter, word_counter = latin[ch]
                    char_counter += 1
                    if not latin_encounter[ch]:
                        latin_encounter[ch] = True
                        word_counter += 1
                    latin[ch] = (char_counter, word_counter)

                if ch in cyrillic:
                    char_counter, word_counter = cyrillic[ch]
                    char_counter += 1
                    if not cyrillic_encounter[ch]:
                        cyrillic_encounter[ch] = True
                        word_counter += 1
                    cyrillic[ch] = (char_counter, word_counter)
            if any(cyrillic_encounter.values()) and any(latin_encounter.values()):
                bilingual_word_amount += 1

    word_amount = len(words)
    result = {'word_amount' : word_amount,
            "paragraph_amount" : paragraph_amount,
            "bilingual_word_amount" : bilingual_word_amount}
    if word_amount != 0:
        for ch in latin:
            char_counter, word_counter = latin[ch]
            latin[ch] = (char_counter, round(word_counter / word_amount * 100, 2))

        for ch in cyrillic:
            char_counter, word_counter = cyrillic[ch]
            cyrillic[ch] = (char_counter,  round(word_counter / word_amount * 100, 2))
    else:
        paragraph_amount = 0

    result.update(latin)
    result.update(cyrillic)

    return result

if __name__ == '__main__':
    print(text_stat("tests/simple_sentences.txt"))
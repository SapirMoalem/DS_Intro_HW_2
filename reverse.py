
def reverse(sentence, reverse_word):
    # invalid input
    if type(reverse_word) is not str or type(sentence) is not str:
        return "invalid input"

    # the revers_word not in the sentence
    if reverse_word not in sentence:
        return "no match word found"

    # reverses the first occurrence of reverse_word in the sentence
    result = ""
    first_is_founded = False
    for word in sentence.split(" "):
        if word == reverse_word and first_is_founded is False :
            first_is_founded = True
            result += word[::-1]
        else:
            result += word
        result += " "

    # deletes the last space in the result sentence
    if result[-1:] == " ":
        result = result[:-1]

    return result



'''
print(reverse("I like apples and I also like bananas", "like"))

assert reverse("I like apples and I also like bananas", "oranges") \
                == "no match word found"
assert reverse("I like apples and I also like bananas", 3) \
                == "invalid input"
assert reverse("I like apples and I also like bananas", "Bananas") \
                == "no match word found"
assert reverse("I like apples and I also like bananas", "like") \
                == "I ekil apples and I also like bananas"

assert reverse("I like apples and I also like bananas", "bananas") \
                == "I like apples and I also like sananab"

assert reverse("I like apples and I also like bananas", "") \
                == "I like apples and I also like bananas"
'''


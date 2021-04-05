def getting_string(text="Hello, please enter a full, random sentence: "):
    return input(text)


user_string = getting_string()
user_string_split = user_string.split()


def string_reversal():
    reversed_string = user_string_split[::-1]
    return reversed_string

string_reversal()

def final_string():
    reversed_sentence = " ".join(string_reversal())
    return print(reversed_sentence)

final_string()
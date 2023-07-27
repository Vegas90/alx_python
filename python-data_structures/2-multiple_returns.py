#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if sentence else None
    return length, first_char

if __name__ == "__main__":
    length, first_char = multiple_returns(sentence)
    print("Length: {:d} - First character: {}".format(length, first_char))
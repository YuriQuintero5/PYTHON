import re

def is_isogram(string):
    string = re.sub(r"[^a-z]","", string.lower())
    # return 'Is an isogram' if len(set(string)) == len(string) else 'Is not an isogram'
    return len(set(string)) == len(string)
def is_isogram(string):
    return True if len(string.lower()) == len(set(string.lower())) else False
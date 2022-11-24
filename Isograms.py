def is_isogram(string):
    return True if len(string) == len(set(string.lower())) else False

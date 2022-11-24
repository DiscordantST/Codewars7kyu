def find_short(string):
    simple_dict = {len(simple_word): simple_word for simple_word in string.split()}
    return min(simple_dict.keys())  # l: shortest word length

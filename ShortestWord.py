def find_short(s):
    simple_dict = {len(simple_word): simple_word for simple_word in s.split()}
    return min(simple_dict.keys())  # l: shortest word length


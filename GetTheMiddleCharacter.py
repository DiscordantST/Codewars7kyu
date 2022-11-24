def get_middle(string):
    if len(string) % 2 == 0:
        simple_diggit = int(len(string)) // 2
        return string[simple_diggit - 1:simple_diggit + 1]
    if len(string) % 2 != 0:
        simple_diggit = int(len(string)) // 2
        return string[simple_diggit]

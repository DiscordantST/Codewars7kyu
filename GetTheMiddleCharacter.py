def get_middle(s):
    if len(s) % 2 == 0:
        a = int(len(s)) // 2
        return s[a - 1:a + 1]
    if len(s) % 2 != 0:
        a = int(len(s)) // 2
        return s[a]

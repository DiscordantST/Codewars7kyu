def maskify(string):
    return "".join([i.replace(i, "#") for i in string[:-4]])+string[-4:]

def get_count(sentence):
    simple_set = ("a", "e", "i", "o", "u")
    simple_arr = []
    for i in range(len(list(sentence))):
        if sentence[i] in simple_set:
            simple_arr.append(sentence[i])
    return len(simple_arr)

# Best answer from Codewars
# javafreak, ChingChangChong, hdang101, ronanodufaigh, rbordiya, alpharom, lukegb21,
# TRUUUHaZe, mwdbjbc, hectorperez_net (+ 47)
# def getCount(inputStr):
# return sum(1 for let in inputStr if let in "aeiouAEIOU")

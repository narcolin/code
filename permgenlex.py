# 202 Project 1 - 1
# Nicole Arcolino

def perm_gen_lex(string):
    # print(string)
    if len(string) == 0:  # base case
        return []
    results = []
    for i in range(len(string)):
        character = string[i]
        new_strings = string[:i] + string[i + 1:]
        li = perm_gen_lex(new_strings)
        if len(li) == 0:
            results.append(character)
        for element in li:
            element = character + element
            results.append(element)
            # print(results)
    return results
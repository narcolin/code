# 202 Project 1 - 2
# Nicole Arcolino

table = {
    0:"0",
    1:"1",
    2:"2",
    3:"3",
    4:"4",
    5:"5",
    6:"6",
    7:"7",
    8:"8",
    9:"9",
    10:"A",
    11:"B",
    12:"C",
    13:"D",
    14:"E",
    15:"F"
}

def convert_helper(num, b, answer):
    if num == 0:  # base case
        return answer
    else:
        answer = table[num % b] + answer
        num = num // b
        return convert_helper(num, b, answer)

def convert(num, b):
    if num == 0:
        return "0"
    return convert_helper(num, b, '')
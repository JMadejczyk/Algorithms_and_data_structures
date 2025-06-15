key_map = {
    2: "abc",
    3: "def", 
    4: "ghi",
    5: "jkl", 
    6: "mno", 
    7: "pqrs",
    8: "tuv", 
    9: "wxyz"
}

digits = [2, 3]
ans = []

def phone_backtrack(digits: list, string=""):
    if len(digits) == 0:
        ans.append(string)
        return
    num = digits[0]
    mapped_string = key_map[num]
    for char in mapped_string:
        phone_backtrack(digits[1:], string+char)
phone_backtrack(digits)
print(ans)
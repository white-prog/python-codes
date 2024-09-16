def sort(lis1,lis2):
    return sorted(lis1+lis2)
print(sort([1,3,5],[2,4,6]))

def paranthesis(inp):
    cnt_o = 0
    cnt_c = 0
    for i in inp:
        if i == '(':
            cnt_o += 1
        else:
            cnt_c += 1
    if cnt_o == cnt_c:
        return "Perfect"
    return "Error"
print(paranthesis("())"))
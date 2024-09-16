def bit_to_deci(val):
    vales = reversed(val)
    dec = 0
    cnt = 1
    for i in vales:
        if int(i) == 1:
            dec += cnt 
        cnt *= 2
    return dec


for i in range(4):
    inp = input("ENTER BIT: ")
    print(bit_to_deci(inp))




def minimum_coin(change_owe):
    coin_1 = 25
    coin_2 = 10
    coin_3 = 5
    coin_4 = 1
    count = 0
    
    while change_owe != 0:
        if change_owe >= coin_1:
            change_owe = change_owe - coin_1
            count = count + 1
        elif change_owe >= coin_2:
            change_owe = change_owe - coin_2
            count = count + 1
        elif change_owe >= coin_3:
            change_owe = change_owe - coin_3
            count = count + 1
        else:
            change_owe = change_owe - coin_4
            count = count + 1


            
    
    return count

print(minimum_coin(76))
        

        



def start_menu():
    print("xxxxxxxxxxxxxxxxxxxxxxxxx")
    print("1. player vs computer : pc")
    print("2. player1 vs player2 : pp")
    print("3. exit : x")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxx")

def player_vs_computer(player_nm):
    import time
    import random
    player_score  = 0
    computer_score = 0
    while True:
        option = input("Type x to exit: ")
        if option == 'x':
            break
        player = input(f"{player_nm} Choose odd or even: ")
        computer = random.choice(['odd','even'])
        print(computer)
        time.sleep(0.3)
        player_number = int(input("Enter number[1 to 6]: ")) 
        computer_number = random.randint(1,6)
        print(computer_number)
        total = player_number + computer_number
        status = "even" if total % 2 == 0 else "odd"
        player_score += (status == player) * 1
        computer_score += (status == computer) * 1
    time.sleep(0.2)
    print(f"{player_nm} : {player_score}")
    print(f"computer : {computer_score}")


        




def main():
    print("-----------")
    print("ODD or EVEN")
    print("-----------")
    for i in range(3):
        print("")
    start_menu()
    while True:
        val = input("Enter option what you choose('x' or 'pc' or 'pp'): ")
        if val == 'x':
            break
        elif val == 'pc':
            player = input("Enter name: ")
            player_vs_computer(player)
        elif val == 'pp':
            print("In work")

if __name__ == "__main__":
    main()
    


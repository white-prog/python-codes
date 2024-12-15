import time
def forward_animation(movement):
    
    for i in range(0,movement):
        string = [" " for i in range(movement)]
        string[i] = "O"
        print("".join(string),)
        time.sleep(0.25)

def main():
    print("Time for animation: ")
    user_input = int(input("Enter number of times ball move forwards: "))
    print()
    forward_animation(user_input)

    #want to override printing position

if __name__ == "__main__":
    main()
    


    
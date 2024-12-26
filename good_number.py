
def main():
    import random
    while True:
        inp = input(">>>To continue 'C' else 'E' to exit: ")
        if inp == 'E':
            break
        elif inp != 'C':
            print('>>>Invalid Command')
        val = int(input(">>>Enter value 1 to 6: "))
        comp_gen = random.randint(1,6)
        if val - comp_gen == 1 or comp_gen - val == 1:
            print(">>> You won")
        else:
            print(">>> You lose")

if __name__ == "__main__":
    main()
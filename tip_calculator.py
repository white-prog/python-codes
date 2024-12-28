def billValues(amount,tip_perc):
    tp = (amount / 100) * tip_perc
    total = tp + amount
    return (tp,amount)









def main():
    print("Welcome to the Tip Calculator!")
    while True:
        bill_amnt = int(input("Enter the total bill amount: "))
        tip = int(input("Enter the tip percentage: "))
        bill_vals = billValues(bill_amnt,tip)
        print(f"Tip : {bill_vals[0]}₹")
        print(f"Total Bill : {bill_vals[1]}₹")
        cont = input("Would you like to calculate another tip? (yes/no): ")
        if cont == "no":no
            print("Goodbye!")
            break
if __name__ == "__main__":
    main()
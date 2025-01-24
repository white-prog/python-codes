def emi_monthly_payment(amount_of_obj,months,downpayment,interest):
    emi_total_amnt = amount_of_obj - downpayment
    interest_rate_per_month = (interest / 100) * amount_of_obj
    monthly_amount = emi_total_amnt / months + interest_rate_per_month
    total_amount = amount_of_obj + ((interest_rate_per_month) * months)
    loss = total_amount - amount_of_obj
    print(f"Monthly payment : {round(monthly_amount)} ||  Total amount : {round(total_amount)} || loss : {round(loss)} || Interest : {interest_rate_per_month}")

def main():
    print("EMI DETAILS")
    for i in range(3):
        print("")
    while True:
        inp = input("If you don't want to continue type X : ")
        if inp == 'X':
            print("Thank you")
            break
        name = input("Enter name of product: ")
        price = int(input("Enter price: "))
        downpayment = int(input("Enter amount you payed: "))
        interest = int(input("Enter interest percentage: "))
        months_to_pay = int(input("How much months you need to pay: "))
        emi_monthly_payment(price,months_to_pay,downpayment,interest)

if __name__ == "__main__":
    main()

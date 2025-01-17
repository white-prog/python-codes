import argparse

def profit(expense_list,sales_list):
    return sum(sales_list) - sum(expense_list)

def main():
    parser = argparse.ArgumentParser(description="Process two lists: -e and -s.")
    
    # Adding arguments for two lists
    parser.add_argument('-e', '--expenses', nargs='+', type=float, required=True, 
                        help="List of expenses (e.g., -e 100.5 200.75 300)")
    parser.add_argument('-s', '--sales', nargs='+', type=float, required=True, 
                        help="List of sales amounts (e.g., -s 400 500.25 600)")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Access the lists
    expenses = args.expenses
    sales = args.sales
    
    print("Expenses:", sum(expenses))
    print("Sales:", sum(sales))
    print(f"Profit: {profit(expenses,sales)}")

if __name__ == "__main__":
    main()

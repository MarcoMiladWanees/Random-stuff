import time


def show_balance(balance):
    print(f"\nYour balance is ${balance:.2f}")
def withdraw(balance, amount):
    balance -= amount
    return balance
def deposit(balance, amount):
    balance += amount
    return balance

def main():
    is_running = True
    balance = 0
    while is_running:
        print("************************************",
              "          Banking Program            ",
              "************************************",
              "1.Show Balance",
              "2.Withdraw",
              "3.Deposit",
              "4.Exit",
              sep='\n')
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                show_balance(balance)
            case 2:
                amount = int(input("Enter your amount: $"))
                if amount > balance or amount < 0:
                    print("Please wait while your transaction is being processed")
                    time.sleep(2)
                    print("Invalid transaction")
                else:
                    print("Please wait while your transaction is being processed")
                    time.sleep(2)
                    balance= withdraw(balance, amount)
                    print("The transaction was Successful")
            case 3:
                amount = int(input("Enter your amount: $"))
                if amount > 0:
                    print("Please wait while your transaction is being processed")
                    time.sleep(2)
                    balance = deposit(balance, amount)
                    print("The transaction was Successful")
                else:
                    print("Please wait while your transaction is being processed")
                    time.sleep(2)
                    print("Invalid amount")
            case 4:
                is_running = False
                print("\nGoodbye")
                break
            case _:
                print("Invalid choice")
if __name__ == "__main__":
    main()
def makeMoney():
    global balance  # Use the global balance variable
    print("**********************************")
    print("make as many e's as possible")
    ecount = input("e:")
    print("**********************************")
    balance += ecount.count("e") + ecount.count("E")  # Update balance
    seeBalance()  # Call to see balance after making money

def save():
    global balance  # Use the global balance variable
    print("**********************************")
    print("how much money do you want to save")
    print("**********************************")
    save_amount = input("")  # Get input for saving
    try:
        save_amount = int(save_amount)  # Convert to integer
    except ValueError:
        print("Please enter a valid number.")
        return  # Exit if input is invalid

    if save_amount > balance:
        print("**********************************")
        print("sorry amount is too small")
        print("**********************************")
    else:
        balance -= save_amount  # Deduct from balance
        print(f"You have saved {save_amount}. New balance is {balance}.")
    
    main()  # Return to main menu

def seeBalance():
    print(f"Current balance: {balance}")
    main()  # Return to main menu

balance = 0  # Initialize balance

def main():
    while True:  # Loop to keep the menu active
        print("**********************************")
        print("1. make some mollah")
        print("2. put money into savings account")
        print("3. see balance")
        print("4. exit")
        print("**********************************")
        userOpt = input("option:")
        
        if userOpt == '1':
            makeMoney()  # Call function with parentheses
        elif userOpt == '2':
            save()  # Call function with parentheses
        elif userOpt == '3':
            seeBalance()  # Call function with parentheses
        elif userOpt == '4':
            print("Exiting the program.")
            break  # Exit the loop
        else:
            print("Invalid option, please try again.")

main()  # Start the program

import secrets
secure_random = secrets.SystemRandom()

balance = 0

while True:
    option = int(input("Enter 1 to read rules or 2 to play game:> "))
    if option == 1:
        print("> Age must be older than 18.")
        print("> Top-up money must be at least 5000.")
        print("> Each play costs at least 1000.")
    if option == 2:
        username = input("Enter your name:> ")
        age = int(input("Enter your age:> "))

        if len(username) > 2 and age > 17:
            print("Welcome,", username)

            balance = int(input("Top-up money (min 5000):> "))
            if balance >= 5000:
                while balance >= 1000:
                    print("\nYour balance: $", balance)
                    lucky_number = int(input("Enter your lucky number (10–99):> "))
                    bet = int(input("Enter your bet (min 1000):> "))

                    if bet > balance:
                        print("❌ Not enough balance!")
                    if bet <= balance and bet >= 1000:
                        balance -= bet
                        system_number = secure_random.randint(10, 99)
                        print("System Number is:", system_number)

                        if lucky_number == system_number:
                            print("🎉 You WIN! 🎉")
                            balance += bet * 10
                        if lucky_number != system_number:
                            print("❌ You lose!")

                    print("Your balance now: $", balance)

                    if balance < 1000:
                        print("❌ Not enough balance to continue. Top-up again.")
                        break

                    quit_game = int(input("Enter 0 to quit or 1 to continue:> "))
                    if quit_game == 0:
                        print("Thanks for playing! Final Balance: $", balance)
                        break
            else:
                print("❌ You need at least 5000 to start.")
        else:
            print("❌ You are not allowed to play (check name or age).")

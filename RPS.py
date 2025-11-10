import random
while True:
    print("\n --------------------------\n welcome to RPS \n --------------------------")
    user = str(input("make a choice \n 1. Rock\n 2. Paper\n 3. Scissors\n -->"))
    bot = str(random.randint(1, 3))
    def choice_str():
        global user
        global bot
        if user == "1":
            user = "Rock"
        elif user == "2":
            user = "Paper"
        elif user == "3":
            user = "Scissors"
        if bot == "1":
            bot = "Rock"
        elif bot == "2":
            bot = "Paper"
        elif bot == "3":
            bot = "Scissors"
    def user_loss():
        choice_str()
        print(f"❌ You chose {user} and bot chose {bot}. You lose!")
    def user_win():
        choice_str()
        print(f"✔ You chose {user} and bot chose {bot}. You win! ✔")
    if user in ["1", "2", "3"]:
        if user == bot:
            choice_str()
            print(f"\n 🥊 You chose {user} and bot chose {bot}. It's a draw! 🥊")
            #break
        else:
            if user == "1" and bot == "2":
                user_loss()
            if user == "1" and bot == "3":
                user_win()
            if user == "2" and bot == "1":
                user_win()
            if user == "2" and bot == "3":
                user_loss()
            if user == "3" and bot == "1":
                user_loss()
            if user == "3" and bot == "2":
                user_win()
    
                

        
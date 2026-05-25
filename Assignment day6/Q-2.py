import random

l = ["rock", "paper", "scissor"]

while True:

    c = int(input('''
1 YES
2 NO | EXIT

Enter Choice : '''))

    if c == 1:

        uscore = 0
        cscore = 0

        for a in range(1, 6):

            print("\nROUND", a)

            userinput = int(input('''
1 ROCK
2 PAPER
3 SCISSOR

Enter Your Choice : '''))

            if userinput == 1:
                uch = "rock"

            elif userinput == 2:
                uch = "paper"

            elif userinput == 3:
                uch = "scissor"

            else:
                print("Invalid Choice")
                continue

            cch = random.choice(l)

            print("Your Choice :", uch)
            print("Computer Choice :", cch)

            if uch == cch:
                print("Game Draw")
                uscore += 1
                cscore += 1

            elif ((uch == "rock" and cch == "scissor") or
                  (uch == "paper" and cch == "rock") or
                  (uch == "scissor" and cch == "paper")):

                print("You Win")
                uscore += 2

            else:
                print("Computer Win")
                cscore += 2

            print("User Score :", uscore)
            print("Computer Score :", cscore)

        print("\n----- FINAL RESULT -----")

        if uscore == cscore:
            print("Game Draw")

        elif uscore > cscore:
            print("You Won The Game")

        else:
            print("Computer Won The Game")

    else:
        print("Game Exit")
        break
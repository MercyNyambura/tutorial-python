name = input("Type your name: ")
print("Welcome", name, "to this adventure")

answer =  input("you are on a dirt road, it has come to an end and you can go left or right. which way would you like to go ?").lower()

if answer == "left":
    answer = input("you come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ",)

    if answer == "swim":
        print('You swam across and were eaten by an alligator')
    elif answer == "walk":
        print("You walked for miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")



elif answer == "right":
    answer = input("You come to a ridge , it looks wobbly, do you want to cross")

    if answer == "back":
        print("You go back and lose.")

    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? ")
        if answer == "yes":
            print("you talk to the stranger and they give you gold. You win")
    elif answer == "No":
        print ("You ignore the stranger and they are offended. you lose")
    else:
     print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")


print("Thank you for playing")
    


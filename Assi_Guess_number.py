import random
val = random.randint(1,100)
print(val)
print("LEVELS \n1. EASY\n2. MEDIUM \n3. HARD")
st = input("Choose Your Level : ")

if st.lower() == 'easy':
    print("----You Entered Easy Level----")
    print("You Gives 15 Chances")
    i=0
    while(i<15):
        print(i+1,"chances")
        ip = int(input("Enter number : "))
        if ip == val:
            print("Congratulation ! You Won")
            print("You Got",150-i*10,"Points")
            break
        elif ip>val:
            print("Hint :::::")
            print("Please choose Lower number")
        else:
            print("Hint :::::")
            print("Please choose Higher number")
        i=i+1
    else:
        print("Your chances is finished ")
        print("You Loss The Game")
        print("The Answer is",val)

elif st.lower() == 'medium':
    print("----You Entered Medium Level----")
    print("You Gives 10 Chances")
    i = 0
    while (i < 10):
        print(i + 1, "chances")
        ip = int(input("Enter number : "))
        if ip == val:
            print("Congratulation ! You Won")
            print("You Got", 100 - i * 10, "Points")
            break
        elif ip > val:
            print("Hint :::::")
            print("Please choose Lower number")
        else:
            print("Hint :::::")
            print("Please choose Higher number")
        i = i + 1
    else:
        print("Your chances is finished ")
        print("You Loss The Game")
        print("The Answer is", val)
else:
    print("----You Entered Hard Level----")
    print("You Gives 5 Chances")
    i = 0
    while (i < 5):
        print(i + 1, "chances")
        ip = int(input("Enter number : "))
        if ip == val:
            print("Congratulation ! You Won")
            print("You Got", 100 - i * 10, "Points")
            break
        elif ip > val:
            print("Hint :::::")
            print("Please choose Lower number")
        else:
            print("Hint :::::")
            print("Please choose Higher number")
        i = i + 1
    else:
        print("Your chances is finished ")
        print("You Loss The Game")
        print("The Answer is", val)


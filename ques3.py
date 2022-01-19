winning_number=27
user_input=input("guess a number between 1 and 100 :")
user_input2=int(user_input)
if user_input2==winning_number:
    print("YOU WIN!!!!")
else:
    if user_input2>winning_number:
        print("TOO HIGH")
    else:
        print("TOO LOW")
    
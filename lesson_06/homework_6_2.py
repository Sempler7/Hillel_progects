while True:
    word = input("Enter some word contains the letter H: ")
    if 'h' in word.lower():
        print("Thank you. You entered the correct word!")
        break
    else:
        print("The word does not contain 'h'. Please try again.")

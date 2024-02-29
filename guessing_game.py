import random

# Define a function that asks the user for input and DOESN'T QUIT until the user returns something valid
# In this case, "valid" means an integer between 1 and 100 (inclusive)

def get_input():
    while True:
        try:
            user_input = int(input("Please enter a number between 1 to 100: "))
            if user_input < 0 or user_input > 100:
                print("You should input a number between 1 to 100!")
            elif user_input >= 0 and user_input <= 100:
                break
        except:
            print("Your program has error!")
      
    return user_input

# Define a function that compares the user's input to the answer
# Returns a string that indicates the answer is higher or lower than the input, or provides a hint

def compare_input(user, answer):
    if user > answer:
        print("Your input is larger than answer")
        return False
    elif user < answer:
        print("Your input is smaller than answer")
        return False
    else:
        return True

# Define your main() function 

def main():
    # Set a random number between 1 & 100
    answer = random.randint(1, 100)
    # print(answer) # Commenting out to hide the answer
    while True:
        user_input = get_input()
        result = compare_input(user_input, answer)
        if result == True:
            print(f"Congratulations!, You got the answer {answer}")
            break
        else:
            if answer - user_input > 10:
                print("You are far below the answer!")
            elif answer - user_input < -10:
                print("You are far above the answer!")
            elif answer > user_input:
                print("You are close to the answer, but still below!")
            else:
                print("You are close to the answer, but still above!")

if __name__== "__main__":
    main()

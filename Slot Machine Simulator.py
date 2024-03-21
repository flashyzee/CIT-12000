import random 

def main():
    print("Welcome to the Slot Machine Simulator")

    money_inserted = int(input("Please enter the amount of money you want to insert: "))
    
    word1 = generate_word()
    word2 = generate_word()
    word3 = generate_word()

    print("Slot Machine Results:")
    print(word1)
    print(word2)
    print(word3)

    payout = calculate_payout(word1, word2, word3, money_inserted)
    if payout > 0:
        print("Congratulations! You win ${}!".format(payout))
    else:
        print("Sorry, you didn't win anything. Better luck next time!")

def generate_word():
    word_mapping = {1: "Cherries", 2: "Oranges", 3: "Plums"}
    return word_mapping[random.randint(1, 3)]

def calculate_payout(word1, word2, word3, money_inserted):
    if word1 == word2 == word3:
        return money_inserted * 3
    elif word1 == word2 or word2 == word3 or word1 == word3:
        return money_inserted * 2
    else:
        return 0

if __name__ == "__main__":
    main()
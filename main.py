import random

# Number list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Generate a random number
def number_generator():
    answer = random.choice(numbers)
    return answer


# Main loop for game
def main():
    correct = False
    guesses_remaining = 5
    guesses = 0
    random_number = number_generator()
    while guesses_remaining != 0:
        print("-----------------------------------------------")
        print(f"You have {guesses_remaining} guesses remaining.")
        #  print(f"****The correct number is {random_number}****")  # Test code
        x = int(input(f"Guess a number {numbers[0]} through {numbers[-1]}\n"))
        print("-----------------------------------------------")
        if x == random_number:
            guesses = guesses+1
            print(f"Great job! You guessed the correct number in {guesses} guesses!")
            correct = True
            break
        else:
            print("Sorry, that number is incorrect.")
            guesses = guesses + 1
            guesses_remaining = guesses_remaining - 1
    if not correct:
        print(f"You ran out of guesses! The number was {random_number}.")


main()

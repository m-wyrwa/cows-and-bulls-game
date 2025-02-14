import random
import art

# game settings
no_of_digits = 2
secret_password = "exit"


# generating random unique n-digit number
def generate_rand_num(n):
    rand_num = "".join(random.sample("0123456789", n))
    return rand_num


# checking user_guess format
def guess_format_checker(input_text):
    if len(input_text) == no_of_digits and input_text.isdigit() and len(set(input_text)) == no_of_digits:
        return True


print(art.logo)
print("Welcome to the Cows and Bulls Game!")
print(f"Try to guess a {no_of_digits}-digit number!")
print(f"Type \"{secret_password}\" exit at any prompt to exit.\n")
chosen_digits = generate_rand_num(no_of_digits)

game_over = False
guesses = 0
while not game_over:
    user_guess = input("Enter a number:")

    if user_guess == secret_password:
        print("Game Over!")
        print(f"No. of guesses: {guesses}")
        print(f"Correct answer: {chosen_digits}")
        break

    # checking game results
    if guess_format_checker(user_guess):
        cows = 0
        bulls = 0
        i = 0
        for char in chosen_digits:
            if char == user_guess[i]:
                cows += 1
            elif char in user_guess:
                bulls += 1
            i += 1
        print(f"{cows} cows, {bulls} bulls")
        print("---------------")
    else:
        print(f"Please enter valid {no_of_digits}-digit number. The digits must be all different.")
        print("---------------")

    guesses += 1

    # if player guesses all digits
    if user_guess == chosen_digits:
        print(f"Correct! The answer is {chosen_digits}")
        print(f"No. of guesses: {guesses}")
        print("You guessed all digits!")
        print(art.prize)
        game_over = True

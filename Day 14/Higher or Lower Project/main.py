import game_data
from art import logo, vs
import random

def check_answer(user_guess, a_followers, b_followers):
    """Verify if user guesses correctly."""
    print("check answer")
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

def get_random_account():
    """Get random account from game_data."""
    return random.choice(game_data.data)

def game():
    """Main game logic."""
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    a_follower_count = account_a['follower_count']

    while game_should_continue:
        account_b = get_random_account()
        b_follower_count = account_b['follower_count']
        while account_a == account_b:
            account_b = random.choice(game_data.data)

        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
        print(vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()

        is_correct = check_answer(answer, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            account_a = account_b
            print(logo)
            print(f"You're right! Current score: {score}")
        else:
            game_should_continue = False
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")

game()




import game_engine

game = game_engine.GuessingGame(10) #1-10
player_name = (input("Enter your name: "))
print(f"Greetings {player_name}!")


while game.solved() is not True:
    user_guess = int(input(f"Guess the number from 1 to {game.num}: "))
    game.guess(user_guess)
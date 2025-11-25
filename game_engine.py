"""Import random module"""
import random
class GuessingGame:
    """Guessing Game Class"""
    def __init__(self, num):
        self.num = num
        self.answer = random.randint(1,num)
        self._solved = False
        self.count = 1
        
    def guess(self, user_guess):
        """get Guess name and input method"""
        if user_guess == self.answer:
            print(f"Congratulations! You solved it. The answer was {self.answer}")
            print(f"It only took you {self.count} tries!")
            self._solved = True

        if user_guess > self.answer:
            self.response(user_guess, "too high. Try again!")

        if user_guess < self.answer:
            self.response(user_guess, "too low. Try again!")
        self.count +=1
    
    def response(self, user_guess, message):
        """Response of last guess method"""
        print(f"Oops! Your last guess {user_guess} was {message}")

    def solved(self):
        """Solved method to call instance solved"""
        return self._solved

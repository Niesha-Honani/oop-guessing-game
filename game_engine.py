import random

class GuessingGame:
    
    def __init__(self, num):
        self.num = num
        self.answer = random.randint(1,num)
        self._solved = False
    
        
    def guess(self, user_guess):
        if user_guess == self.answer:
            print(f"Congratulations! You solved it. The answer was {self.answer}")
            self._solved = True
        
        return self.response(user_guess, "Too high. Try again..") if user_guess >self.answer else self.response(user_guess, "Too Low Try Again")
        
    
    def response(self, user_guess, message):
        print(f"Oops! Your last guess {user_guess} was {message}")
        pass
    
    def solved(self):
        return self._solved
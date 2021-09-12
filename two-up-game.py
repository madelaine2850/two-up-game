import random


class Game:

    @staticmethod
    def flip_coin():
        results = ["H", "T"]
        coin1 = random.choice(results)
        coin2 = random.choice(results)
        result = coin1 + coin2
        return result

    @staticmethod
    def game():
        operation = 1
        score = 0
        while operation == 1:
            guess = input("Please place your bet (HH, HT, or TT):\n")
            if guess == Game.flip_coin():
                print(f"{guess} You Win!\n")
                score += 1
            else:
                print(f"{Game.flip_coin()} You lose!\n")
            print(f"Your score is {score} now.")
            again = input("Do you want another round? (Y or N)\n")
            if again == "Y":
                pass
            else:
                operation = 0


Game.game()


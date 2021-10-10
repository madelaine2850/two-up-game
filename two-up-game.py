import random

from breezypythongui import EasyFrame


class Game(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title="Two Up Game")

        self.askBet = self.addLabel(text="Please place your bet (HH, HT, or TT):\n",
                                    row=0, column=0)

        self.answerField = self.addTextField(text="",
                                             row=1, column=0)

        self.submitButton = self.addButton(text="Submit",
                                           row=2, column=0, command=self.game)

        self.result = self.addTextField(text="",
                                        row=3, column=0)

    @staticmethod
    def flip_coin():
        results = ["H", "T"]
        coin1 = random.choice(results)
        coin2 = random.choice(results)
        result = coin1 + coin2
        return result

    def game(self):
        score = 0
        if self.answerField.getText() == Game.flip_coin():
            answer = f"{self.answerField.getText()} You Win!\n"
        else:
            answer = f"{Game.flip_coin()} You lose!\n"
        self.result.setText(answer)


Game().mainloop()

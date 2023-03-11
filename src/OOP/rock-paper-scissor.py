class Participant:
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.choice = ""

    def choose(self):
        self.choice = input(f"{self.name}, select rock,paper or scissor: ")
        print(f"{self.name} selects {self.choice}")

    def incrementPoints(self):
        self.points += 1

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.choice]


class GameRound:
    def __init__(self, p1, p2):
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]
        p1.choose()
        p2.choose()
        result = self.compareChoices(p1, p2)
        print(f"Round resulted in a {result}")
        if result > 0:
            p1.incrementPoint()
        elif result < 0:
            p2.incrementPoint()

    def compareChoices(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

    def awardPoints(self):
        print("implement")


class Game:
    def __init__(self) -> None:
        self.endGame = False
        self.participant = Participant("Spock")
        self.secondParticipant = Participant("Kirk")

    def start(self):
        while not self.endGame:
            GameRound(self.participant, self.secondParticipant)
            self.checkEndCondition()

    def checkEndCondition(self):
        answer = input("Continue game Y or N: ")
        if answer.lower() == 'y':
            GameRound(self.particiant, self.secondParticipant)
        else:
            print("Game ended,{p1name} has {p1points}, and {p2name} has {p2points}".format(p1name=self.particiant.name,
                  p1points=self.particiant.points, p2name=self.secondParticipant.name, p2points=self.secondParticipant.points))
            self.determineWinner()
            self.endGame = True

    def determineWinner(self):
        resultString = "It's a Draw"
        if self.particiant.points > self.secondParticipant.points:
            resultString = f"Winner is {self.particiant.name}"
        elif self.particiant.points < self.secondParticipant.points:
            resultString = f"Winner is {self.secondParticipant.name}"
        print(resultString)


game = Game()
game.start()

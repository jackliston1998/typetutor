import sys, random, time

class Game():
    def __init__(self):
        self.game_time = input("how long would you like to play?(seconds)")

    def start(self, user):
        endtime = time.time() + int(self.game_time)
        while time.time() < endtime:
            word = self.randInput()
            print(word)        
            n = input()
            user.setScore(user.getScore() + self.ansCheck(n, word))

    def randInput(self):
    # returns a random word from the words.txt file
        return random.choice(open("words.txt").readlines()).strip()
    
    def ansCheck(self,n, word):
    # checks if the guess was correct and if so returns 1
    # else it returns 0 and passes the mistake to be logged
        if n == word:
            return 1
        else:
            user.setMistakes(n,word)
            return 0
    
class User():
    def __init__(self):
        self.score = 0
        self.mistake = {}

    def setScore(self, new_score):
        self.score = new_score        
    
    def getScore(self):
        return self.score
    
    def setMistake(self,n,word):
        for item in self.getError(n,word):
            self.mistake[item] += 1

    def getMistake(self):
        return self.mistake

    def getError(self,n,word):
        oppsies = []
        length = max([n, word], key=len)
        i = 0
        while i < length:
            if a[i] != word[i]:
                oppsies.append(a[i])
            i+=1






if __name__ == "__main__":
    game = Game()
    user = User()
    game.start(user)
    print(user.getScore())

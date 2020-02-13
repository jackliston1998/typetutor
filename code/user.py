import operator, curses, random, sys
class User():
    def __init__(self):
        self.score = 0
        self.mistake = {}

    def setScore(self, new_score):
        self.score = new_score        
    
    def getScore(self):
        return self.score
    
    def setMistake(self,ltr):
        if ltr in self.mistake:
            self.mistake[ltr] += 1
        else:
            self.mistake[ltr] = 1
            
    def getMistake(self):
        sorted_x = sorted(self.mistake.items(), key=operator.itemgetter(1))
        for item in sorted_x:
            print(item[0], "wrong", item[1], "times")

    def getError(self,n,word):
        oppsies = []
        length = max([n, word], key=len)
        i = 0
        while i < length:
            if a[i] != word[i]:
                oppsies.append(a[i])
            i+=1

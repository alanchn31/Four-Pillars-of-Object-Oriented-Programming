class PreciousStones:

    def __init__(self,stones):              #stones is a list parameter
        if len(stones) > 5:
           self.stones = stones[-5:]
        else:
           self.stones = stones
        print("Stones: " + str(self.stones))

    def addStones(self,stone):              #stone is a list parameter
        x = self.stones
        x.extend(list(stone))
        if len(x) > 5:
           self.stones = x[-5:]
        else:
           self.stones = x
        print("Stones: " + str(self.stones))


    def removeStones(self,stone):           #stone is a list parameter
        for i in stone:
            self.stones.remove(i)
        print("Stones: " + str(self.stones))


class  Generator:
    def __init__(self,filePathCsv):
        self.filePathCsv = filePathCsv
        self.list = []


    def generatePlayers(self):
        return self.list

    def countPlayerList(self):
        i=0
        for players in self.list:
            i+=1
        return i



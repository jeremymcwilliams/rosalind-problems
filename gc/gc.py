class gc:
    def __init__(self, fastaFile):
        fasta = open(fastaFile, 'r').read()
        #print(fasta)
        self.percent=0
        self.title=""
        self.fastaDict=self.splitFile(fasta)



    def splitFile(self, fasta):
        fastaDict={}
        y=fasta.split(">")
        del y[0]
        i=0
        while i < len(y):
            piece=y[i]
            z=y[i].split("\n")
            title=z[0]
            del z[0]
            fas=''.join(z)
            fastaDict[title]=fas
            i += 1

        return fastaDict


    def computeGc(self):
        results={}
        for title, dna in self.fastaDict.items():
            dnaLen=len(dna)
            cgCount=0
            for x in range(dnaLen-1):
                if (dna[x]=="C" or dna[x]=="G"):
                    cgCount+=1
            percent=round((cgCount/dnaLen)*100,7)
            results[title]=percent
            self.setVals(title,percent)
        self.printVals()
        print(results)


    def setVals(self, title, percent):
        if(percent > self.percent):
            self.percent=percent
            self.title=title


    def printVals(self):
        print (self.title)
        print (self.percent)



if __name__ =="__main__":


    gc=gc("fasta.txt")
    gc.computeGc()

    #percentGc=gc.computeGc()
    #print(percentGc)

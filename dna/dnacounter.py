class NucleotideCounter:
    def __init__(self, dna):
        self.dna=dna
        self.a=0
        self.c=0
        self.g=0
        self.t=0

    def countLetter(self, letter):
        for l in self.dna:
            if l is "A":
                self.a+=1
            elif l is "C":
                self.c+=1
            elif l is "G":
                self.g+=1
            elif l is "T":
                self.t+=1
            else:
                print ("bad input")

    def countAllLetters():
        pass

    def printOuput(self):
        print ("{} {} {} {}".format(self.a, self.c, self.g, self.t))

if __name__ == '__main__':
    nc=NucleotideCounter("AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC")

    nc.countLetter("A")
    nc.printOuput()

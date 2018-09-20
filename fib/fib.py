class Rabbits:

    def countRabbits(self, n, k):
        #k=self.k
        if n == 0:
            return 0
        if n == 1:
            return 1
        else:
            return self.countRabbits(n-1, k) + k*self.countRabbits(n-2, k)



if __name__ == '__main__':

    r=Rabbits()
    print r.countRabbits(30,2)

class Rabbits:
    def __init__(self, n, k):
        self.n=n
        self.k=k

    def fib(self, n):

        #n=self.n
        if n == 0: return 0
        elif n == 1: return  self.k 
        else: return self.fib(n-1)+self.fib(n-2)





if __name__ == '__main__':

    r=Rabbits(5,3)
    x=r.fib(5)
    print(x)

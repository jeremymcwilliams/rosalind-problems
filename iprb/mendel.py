class mendel:

    def __init__(self, k, m, n):
        self.k=k
        self.m=m
        self.n=n

    def compute(self):
        sum=self.k+self.m+self.n
        print(sum)


        pr=(1/((sum)*(sum-1))*(k*(k-1)+2*k*m + 2*k*n + 0.75*(m*(m-1))+ m*n))
        print(pr)




if __name__ == '__main__':

    k=20
    m=30
    n=28
    doIt=mendel(k,m,n)
    doIt.compute()

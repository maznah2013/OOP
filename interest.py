class Interest:
    def __init__(self,principal,time,rate):
        self.principal=principal
        self.time=time
        self.rate=rate
        self.si=0
        self.amount=0

    def simple_interest(self):
        self.si=(self.principal*self.rate*self.time)/100
        print(f"The simple interest is {self.si}")

    def amt(self):
        self.amount=self.principal+self.si
        print(f"Your final amount is {self.amount}")


interest1=Interest(500,2,5)
interest1.simple_interest()
interest1.amt()

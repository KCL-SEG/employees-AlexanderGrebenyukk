"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

class Salary(Employee):
    def __init__(self,name,salary):
        super().__init__(name)
        self.salary=salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        pay = self.get_pay()
        return f"{self.name} works on a monthly salary of {pay}.  Their total pay is {pay}."

class Contract(Employee):
    def __init__(self,name,hours,rate):
        super().__init__(name)
        self.hours=hours
        self.rate=rate

    def get_pay(self):
        return self.hours*self.rate

    def __str__(self):
        pay = self.get_pay()
        return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour.  Their total pay is {pay}."

class CommissionsSalary(Salary):
    def __init__(self,name,salary,amount,rates):
        super().__init__(name,salary)
        self.amount=amount
        self.rates=rates

    def get_pay(self):
        pay = super().get_pay()
        pay = pay + (self.amount*self.rate)
        return pay

    def __str__(self):
        pay = self.get_pay()
        return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.amount} contract(s) at {self.rates}/contract.  Their total pay is {pay}."

class CommissionsContract(Contract):
    def __init__(self,name,hours,rate,amount,rates):
        super().__init__(name,hours,rate)
        self.amount=amount
        self.rates=rates

    def get_pay(self):
        pay = super().get_pay()
        pay = pay + (self.amount*self.rates)
        return pay

    def __str__(self):
        pay = self.get_pay()
        return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.amount} contract(s) at {self.rates}/contract.  Their total pay is {pay}."

class CommissionSalary(Salary):
    def __init__(self,name,salary,commission):
        super().__init__(name,salary)
        self.commission=commission

    def get_pay(self):
        return super().get_pay() + self.commission

    def __str__(self):
        pay = self.get_pay()
        return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.commission}.  Their total pay is {pay}."

class CommissionContract(Contract):
    def __init__(self,name,hours,rate,commission):
        super().__init__(name,hours,rate)
        self.hours=hours
        self.rate=rate
        self.commission=commission

    def get_pay(self):
        return super().get_pay() + self.commission

    def __str__(self):
        pay = self.get_pay()
        return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.commission}.  Their total pay is {pay}."

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Contract('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = CommissionsSalary('Renee',3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = CommissionsContract('Jan',150,25,3,220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = CommissionSalary('Robbie',2000,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = CommissionContract('Ariel',120,30,600)

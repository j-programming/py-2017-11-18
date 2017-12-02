#!/usr/bin/env python

class BankAccount(object):
    def __init__(self,value):
        self._id=value
        self._balance=0

    @property
    def id(self):
        return self._id

    @property
    def balance(self):
        return self._balance

    @property
    def state(self):
        return 'normal' if self._balance>=0 else 'overdraft' 

    def deposit(self,value):
        self._balance+=value


    def withdraw(self,value):
        if self.state=='normal':
            self._balance-=value
        else:
            raise ValueError('Insufficient funds for bank account: '+ str(self._id))


    def pay_interest(self):
        if self.state=='normal':
            self._balance *=1.1
        else:
            self._balance*=1.2

account = BankAccount(1234)
print account.id
print account.balance
print account.state

account.deposit(1000)
print account.balance
print account.state

print account.balance
account.pay_interest()
print account.balance

account.withdraw(1600)
print account.balance
print account.state

#Oczekiwane zachowanie - withdraw() przy debecie
account.withdraw(100)
print account.balance

account.pay_interest()
print account.balance
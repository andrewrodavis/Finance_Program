from processes.transactions import *
from processes.transactions.add_a_transaction import testThisFun

def trans_main():
   print("In the transaction menu")
   print("Testing process pull")
   x = testThisFun(1)
   print(x)
   input()

   input()
   return True, "account", True

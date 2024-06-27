'''eno=int(input('Enter Employee Number:'))
ename=input('Enter Employee Name:')
esal=float(input('Enter Employee Salary:'))
eaddr=input('Enter Employee Address:')
married=bool(input('Is Employee Married?[True|False]:'))
print('Plase confirm your provided information')
print('Employee Number:',eno)
print('Employee Name:',ename)
print('Employee Salary:',esal)
print('Employee Address:',eaddr)
print('Employee Married?:',married)'''



"""for i in range(3):
    for j in range (3):
        if i==j:
            break
        print(i,j)   """
        
        
        
        
'''cart=[10,20,30,40,50]
for item in cart:
    if item>500:
       print('we cantnot place this order because of insurence')
       break
    print('Processing Item:',item)
else:
    print('Congratutations,all items process successfuly')    '''
    
    
'''from abc import *
class Loan(ABC):
    @abstractmethod
    def getInterestRate(self):
        pass
class HomeLoan(Loan):
    def getInterestRate(self):
        return 8
class VehicleLoan(Loan):
    def getInterestRate(self):
        return 11 
h=HomeLoan()
print(h.getInterestRate())   '''

'''2

import string
import random
 
# initializing size of string
N = 7
 
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
 
# print result
print("The generated random string : " + str(res))

'''
 
 
 
'''  5
a = [1, 2, 4]
b = a[:]
b.insert(3, 3)
print(b)

'''

'''4
test_string = "jgfdfbfjeenb"
print("The original string : " + str(test_string))
res = ''.join(sorted(test_string))
print("String after sorting : " + str(res))

'''


''' 3
def removeDulipcates(arr):
    return list(set(arr))
arr = [1, 2, 5, 1, 7, 2, 4, 2] 
# Function call
print(removeDulipcates(arr))

'''


arr=[26,45,32,12.,8,9,13]
n= len(arr)
arr.sort()
print("second smallest elements is:"+str(arr[1]))

#a,b=[int(x) for x in input('Enter two Number:').split()]
#print('The Sum:',a+b)
 
 

#a,b=[int(x) for x in input ('Enter two number:').split(',')]
#print('The Sum:',a+b)


#a,b,c=[float(x) for x in input('Enter 3 float value, separation:').split(',')]
#print('The Sum:',a+b+c)

#x=eval(input("enter something"))
#print(type(x))

#x=eval("10+20+30")
#print(x,type(x))

#x=eval("10+20/3**4//5*40")
#print(x)

#from sys import argv
#print(type(argv))


"""from  sys import argv
args=argv[1:]
sum=0
for x in args:
    sum=sum+x
print('The Sum:',sum)"""



"""name = input('Enter Name:')
if name == 'shweta':
    print('Hello Shweta, Good Morning')
print('How are you!!!')"""


"""name = input('Enter Name:')
if name == 'shweta':
    print('Hello Shweta,Good Morning')
else:
    print('Hello guys,Good Morning')
print('How are you') """ 



"""brand = input('enter your fav. brand : ')
if brand =='KF':
    print('It is children brand')
elif brand == 'KO':
    print('Is is too light')
elif brand == 'RC':
    print('It is not that much kick')
elif brand  == 'FO':
    print('Boy are GET one FREE')
else:
    print('other brand not recomenderd') """
    
    
   
"""a=int(input('Enter the frist number:'))
b=int(input('Enter the Second number:'))
if a>b:
    print('a is a biggest number')
else:
    print('b is a biggest number')"""
    


"""a=int(input('Enter the frist number'))
b=int(input('Enter the second number'))
c=int(input('Enter the third number'))
if a>b and a>c:
    print('a is biggest number')
elif b>c:
    print('b is biggest number')
else:
    print('c is biggest number')"""
    
    
    
"""a= int(input('Enter the first number:'))
b= int(input('Enter the second number:'))
c=int(input('Enter the third number:'))
if a<b and a<c:
    print('a is smallest number')
elif b<c:
    print('b is smallest number')
else:
    print('c is smallest number')"""
    
   
   
"""n= int(input('Enter the number:'))
if n>=1 and n<=100:
    print('The number is between 1 and 100'.format(n))
else:
    print('The number {} is not in between 1 and 100'.format(n)) """
    
    
"""n=int(input('Enter any digit from 0 and 5:'))
if n==0:
    print('Zero')
elif n==1:
    print('One')
elif n==2:
    print('Two')
elif n==3:
    print('Three')
elif n==4:
    print('Four')
elif n==5:
    print('Five')    
else:
    print('plz enter a digite from 0 to 5 only')"""
    


"""s='shweta'
i=0
for x in s:
    print('The character present at {} index{}')"""
    
'''for x in range(10):
    print('Hello Welcome to Python for loop') '''
    
    
'''for x in range(1,11):
    print(x) '''
   
'''for x in range(100):
    if x%2 ==0:
        print(x) ''' 
        
'''for x in range(50,0,-1):
    print(x)'''
 
 
"""list=eval(input("Enter Some List numbers"))
Sum=0
for x in list:
    sum=sum+x
    print('The sum',sum)""" 


'''i=1
while i<=10:
    print('hello,welcome to while loop')
    i=i+1'''
 
 
    
'''i=1
while i<=10:
    print(i)
    i=i+1 '''
    
    
    
'''x=1
while x<=20:
    if x%3==0:
        print(x)
    x=x+1'''
    


'''n=int(input('Enter Number:'))
sum=0
i=1
while i<n:
    sum=sum+i
    i=i+1
print('The Sum',sum)'''



'''name=''
while name !='sunny':
    name=input('Enter Your Favourite Actress:')
print('Thanks for confirmation') '''


'''i=1
while True:
    print('Hello:',i)
    i=i+1 '''
    
    
'''for i in range (3):
    for j in range(2):
        print('Hello')'''
        
        
'''for i in range(3):
    for j in range(2):
        print('i={},j={}'.format(i,j))'''
        
        
'''n= int(input('Enter n value:'))
for i in range (n):
    print('*',end='')'''
    
    
"""n=int(input('Enter no of row:'))
for i in range(n):
     print('#' *4) """
     

"""n= int(input("enter no of row: "))
for i in range(n):
    print((str(i+1)+' ')*n) """
    


"""n= int(input('enter no of row:'))
for i in range (n):
    print((chr(65+i)+' ')*n)  """
    
    
"""n= int(input('enter no of rows'))
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()  """
    
    
    
"""n= int(input('enter no of rows:'))
for i in range(n):
    print('*' *(n-i))
print()  """


"""def sum(n):
    if (n==0):
        return 0
    return n + sum(n-1)
sum(5)  """


"""n= int(input('enter no of row:'))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))   """
    
    

"""n=int(input('Enter Number of Row:'))
for i in range(n):
    print(' '*(i)+'* '*(n-i))"""
    
    
    
"""n=int(input('Enter the Number of Row:'))
for i in range(n):
    print(' '*(n-i-1)+'* '*(i+1))
for i in range(n):
    print(' '*(i+1)+'* '*(n-i-1))    """
    
    
    
# FLOW CONTROL 

"""for i in range(10):
    if i==7:
        print('Processing is enough,break loop execution...')
        break
    print(i)
print('outside of loop') """



"""cart=[10,20,30,600,70,80]
for item in cart:
    if item > 500:
        print('TO place this order, insurence must be required , cant proced ')
        break
    print('processing item:,item')  """
    
    
    
"""x = 10
if x > 40:
    print('we are stopping program')
    break
print('Hello')   """


"""cart=[10,20,600,700,80,90]
for item in cart:
    if item >500:
        print('insurence must be required, just string')
        continue
    print('Processing item:',item)  """
    
    
"""l=[10,20,0,5,0,30]
for x in l:
    if x==0:
        print('Hello S')"""


'''x = int(input("enter marks"))
if x>=35:
    print("Success")    '''
    
    
'''s1='durga' 
s2=s1
s3=s1
del s1
print(s2)
print(s3)   '''






 




        
        
        
        
        
        
        



          
       
       
                    
             
        
        
    
    
       
    

          
          
    
    
    



                     
                         
    
    
    
          
    
        
           
 
       
    
         
        
                






    



          

    

     
    















from ast import Num
import numbers
from turtle import numinput


a=float(input("enter first side"))
b=float(input("enter second side"))
c=float(input("enter third number"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print(' area of the triangle is %0.2f'%area)
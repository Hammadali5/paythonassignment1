# paythonassignment1
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

# program 1
#poem code
line1 = "twinkle, twinkle, little star,\n"
line2 = "\t\tHow i wonder what you are,\n"
line3 = "\t\t\t\tUp above the world so high,\n"
line4 = "\t\t\t\tlike the daimond in the sky,\n"
line5 = "twinkle, twinkle, little star,\n"
line6 = "\t\tHow i wonder what you are,"
print(line1, line2, line3, line4, line5, line6)

#program 2
#version of python
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


#program 3
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()
print("now =", now)
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

#program 4
#calculate the area of circle
pi=3.14
r=float(input("enter the radius of a circle"))
area=pi*r*r
print(("Area of circle=%.2f")%area)

#program 5 
aa = input("Input your First Name : ")
bb = input("Input your Last Name : ")
print (("Hello, ") ,bb, aa)


#program6
aaa=int(input("entre first number="))
bbb=int(input("entre 2nd number="))
sum = aaa+bbb
print(("addition of two number is="),sum)

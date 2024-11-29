print("Le Van Thanh")
print("MSSV:235752021610020")
#general solution
a= float (input("enter a (a<>0): "))
b= float(input("nhap b :"))
c= float (input("enter c :"))
delta=b*b-4*a*c
if delta == 0:
  print("pt means x1-x2=",-b/(2*a))
if delta>0:
  print("The equation has 2 distinct solutions xl=", (-b+delta**0.5/(2*a), "and x2=", (-b-delta**0.5/(2*a))))
if delta < 0:
  print("ptvn")


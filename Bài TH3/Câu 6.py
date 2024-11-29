print("Le Van Thanh")
print("MSSV:235752021610020")
def get_sum(*num):
    tmp=0
    #browse parameters
    for i in num:
         tmp +=i
    return tmp
result=get_sum(1,2,3,4,5)
print (result)

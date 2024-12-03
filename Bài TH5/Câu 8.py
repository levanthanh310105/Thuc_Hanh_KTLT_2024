print("le van thanh")
print("mssv: 235752021610020")
def Sequential_Search(dlist, item):
    for i in range(len(dlist)):
        if dlist[i] == item:
            return (True, i)  
    return (False, -1) 
n = int(input("Enter the number of elements in the list: "))
dlist = [int(input(f"Enter the {i + 1}th element: ")) for i in range(n)]
item = int(input("Enter the element to find: "))
ket_qua = Sequential_Search(dlist, item)
print("Search results:", ket_qua)

print("le van thanh")
print("mssv: 235752021610020")
def bubblesort(nlist):
    n = len(nlist)
    for i in range(n):
        for j in range(0, n - i - 1):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
n = int(input("Enter the number of elements in the list: "))
nlist = [int(input(f"Enter the {i + 1}th element: ")) for i in range(n)]
bubblesort(nlist)
print("List after sorting:", nlist)


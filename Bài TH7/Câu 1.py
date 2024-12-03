print("le van thanh")
print("mssv: 235752021610020")
input_file=open('D:/a.txt','r')
for line in input_file:
    l =len (line)
    s='  '
    while l >=1:
       s=s+line[l - 1]
       l =l - 1
    print(s)
input_file.close()

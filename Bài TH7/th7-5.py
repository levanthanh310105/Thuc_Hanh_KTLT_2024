print("le van thanh")
print("mssv: 235752021610020")
def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
               myfile.write("Python Exercises\n")
               myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read( 'a.txt')

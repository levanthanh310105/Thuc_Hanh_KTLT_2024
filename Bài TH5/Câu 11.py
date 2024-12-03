print("le van thanh")
print("mssv: 235752021610020")
import numpy as np
students = np.array(
    [
        ('James', 5, 48.5),
        ('Nail', 6, 52.5),
        ('Paul', 5, 42.1),
        ('Pit', 5, 40.11)
    ],
    dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')]
)

sorted_students = np.sort(students, order=['class', 'height'])
print("Sort result:")
print(sorted_students)

import numpy as np

"""
The program sorts the student id with increasing height of the students from given students id and height.
It prints the integer indices that describes the sort order by multiple columns and the sorted data.
"""

if __name__ == '__main__':
    students_id = np.array([3, 2, 4, 1])
    students_height = np.array([3, 2, 4, 1])
    integer_indices = np.lexsort((students_id, students_height))
    print("Sort order:")
    print(integer_indices)
    print("Sorted data:")
    for student in integer_indices:
        print(students_id[student], students_height[student])
        
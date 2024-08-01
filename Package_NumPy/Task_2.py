import numpy as np

arr = np.array([[8, 7, 9], [6, 8, 7], [9, 9, 8], [7, 6, 8]])
one_pupil_marks = arr.shape[1]
total_for_one_student = arr.sum(axis=1)

average_grades = list(map(lambda n: int(n) / one_pupil_marks, total_for_one_student))
print(average_grades)
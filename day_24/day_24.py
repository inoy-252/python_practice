import numpy as np

py_list1 = [1, 2, 3]
py_list2 = [4, 5, 6]
print("Pyhton list '+':", py_list1 + py_list2)

np_arr1 = np.array([1, 2, 3])
np_arr2 = np.array([4, 5, 6])
print("Numpy array '+':", np_arr1 + np_arr2)

vector = np.array([10, 20, 30, 40, 50])
print("\n--- 1D Vector ---")
print("Vector:", vector)
print("Dimensions (ndim):", vector.ndim)
print("Shape:", vector.shape)

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("\n ---2D Vector ---")
print(matrix)
print("Dimensions (ndim):", matrix.ndim)
print("Shape (rows, columns):", matrix.shape)
print("Total Elements size:", matrix.size)

scores = np.array([72, 85, 90, 64, 88, 95, 78])

print("\n --- Student Exam Scores ---")
print("Original scores:", scores)
print("curved (+5 bonus):", scores + 5)
print("scaled (10% boost):", scores * 1.1)

print("\n ---Statistical Analysis ---")
print("Count (Total):        ", scores.size)
print("Sum:                  ", np.sum(scores))
print("Minimum Score:        ", np.min(scores))
print("Maximum Score:        ", np.max(scores))
print("Mean (Average):       ", np.mean(scores))
print("Median (Middle):      ", np.median(scores))
print("Standard Deviation:   ", round(np.std(scores), 2))

grades = np.array(
    [
        [80, 85, 90],
        [70, 75, 65],
        [95, 90, 100],
    ]
)

print("\n ---2D Matrix:Gradebook--- ")
print("Full Gradebook:\n", grades)
print("Overall Average:", round(np.mean(grades), 2))
print("Subject Average (Axis=0 - down the columns):", np.round(np.mean(grades, axis=0)))
print("Student Average (Axis=1 - across rows):", np.round(np.mean(grades, axis=1)))

print("\n--- Slicing & Indexing ---")
print("Student 1 entire record (Row 0):    ", grades[0, :])
print("All Math scores (Column 0):         ", grades[:, 0])
print("All Coding scores (Column 2):       ", grades[:, 2])
print("Student 2's Coding score:           ", grades[1, 2])

print("\n--- Reshaping ---")
flat_line = np.arange(1, 13)
print("Flat line (1D):", flat_line)
print("Shape", flat_line.shape)

grid = flat_line.reshape(3, 4)
print("\nReshaped into 3x4 Grid (2D):\n", grid)
print("New Shape:", grid.shape)

print("\n--- Boolean Filtering ---")
print("Original scores:                ", scores)
print("Scores >= 85 (Honor Roll):      ", scores[scores >= 85])
print("Failing scores (< 70):          ", scores[scores < 70])

arr = np.random.randint(1, 100, size =(5,5))

print(arr)

arrMax, arrMin = arr.max(), arr.min()
arr_normalized = (arr - arrMin)/(arrMax - arrMin)

print(arr_normalized)
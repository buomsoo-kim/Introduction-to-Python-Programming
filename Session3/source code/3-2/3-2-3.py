arr = np.arange(9).reshape(3,3)
diag = np.diag(arr)

print(diag)

diag_mat = np.diag(np.diag(arr))

print(diag_mat)
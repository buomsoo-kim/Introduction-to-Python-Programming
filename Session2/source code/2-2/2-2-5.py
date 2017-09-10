# 이진탐색 구현
def binary_search(alist, value):
    lower = 0
    upper = len(alist)
    while lower < upper:
        x = lower + (upper - lower) // 2
        temp = alist[x]
        if value == temp:
            return x
        elif value > temp:
            if lower == x:
                break
            lower = x
        else:
            upper = x

# 이진 탐색의 인풋은 정렬된 리스트여야 함
print(binary_search([1,5,8,10], 5))
print(binary_search([1,5,8,10], 0))
print(binary_search([1,2,9,10,12,15,19], 9))
print(binary_search([1,2,9,10,12,15,19], 20))
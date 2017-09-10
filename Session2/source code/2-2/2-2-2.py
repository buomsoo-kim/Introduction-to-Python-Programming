## implementing Queue ADT

# front는 리스트의 끝, rear는 리스트의 시작
def is_empty(queue):
    return bool(len(queue))
def enqueue(queue, item):
    queue.append(item)
def dequeue(queue):
    temp = queue[0]
    for i in range(len(queue)-1):
        queue[i] = queue[i+1]
    queue.pop()
    return temp
def get_size(queue):
    return len(queue)

queue = [1, 2, 3, 4, 5]
print(is_empty(queue))
enqueue(queue, 6)
print(queue)
dequeue(queue)
print(queue)
print(get_size(queue))


## Alternatively,

# front는 리스트의 시작, rear는 리스트의 끝
def is_empty(queue):
    return bool(len(queue))
def enqueue(queue, item):
    queue.append(None)
    for i in range(len(queue) - 1, 0, -1):
        queue[i] = queue[i-1]
    queue[0] = item
def dequeue(queue):
    return queue.pop()
def get_size(queue):
    return len(queue)

queue = [5, 4, 3, 2, 1]
print(is_empty(queue))
enqueue(queue, 6)
print(queue)
dequeue(queue)
print(queue)
print(get_size(queue))
## implementing Stack ADT

def is_empty(stack):
    return bool(len(stack))
def push(stack, item):
    stack.append(item)
def pop(stack):
    return stack.pop()
def top_value(stack):
    return stack[len(stack) - 1]
def get_size(stack):
    return len(stack)

stack = [1, 2, 3, 4, 5]
print(is_empty(stack))
push(stack, 6)
print(stack)
pop(stack)
print(stack)
print(top_value(stack))
print(get_size(stack))
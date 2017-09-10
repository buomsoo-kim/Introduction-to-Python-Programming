def divide_by_two(integer):
    remainder = integer % 2
    quotient = int(integer/2)
    return (quotient, remainder)

def converter(integer):
    result = ''
    while integer != 0:
        (q, r) = divide_by_two(integer)
        result = str(r) + result
        integer = q
    return int(result)

converter(24)
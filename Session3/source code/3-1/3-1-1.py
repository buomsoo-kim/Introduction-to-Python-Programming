n = int(input())
integers = [int(i) for i in input().split()]
m = int(input())

divisor_sum = 0
multiple_sum = 0
for i in integers:
    if m%i == 0:
        divisor_sum += i
    # 약수이면서 배수인 경우(i=m)도 있으므로 if문 두개를 활용한다
    if i%m == 0:        
        multiple_sum += i

print(divisor_sum)
print(multiple_sum)
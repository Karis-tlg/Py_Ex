def is_valid_parentheses(number):
    stack = []
    for digit in str(number):
        if int(digit) % 2 == 0:
            stack.append('(')
        else:
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0

def count_and_sum_square_parentheses(a, b):
    count = 0
    total = 0
    for number in range(a, b + 1):
        if is_valid_parentheses(number):
            count += 1
            total += number ** 2
    return count, total

t = int(input())

# Duyệt qua từng testcase
for _ in range(t):
    a, b = map(int, input().split())

count, total = count_and_sum_square_parentheses(a, b)
print(count, total)

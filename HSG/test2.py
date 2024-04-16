def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def digit_sum(n):
    return sum(int(digit) for digit in str(n))

def digit_square_sum(n):
    return sum(int(digit)**2 for digit in str(n))

def are_coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a == 1

def is_unusual_number(n):
    digit_sum_value = digit_sum(n)
    digit_square_sum_value = digit_square_sum(n)
    return is_prime(digit_sum_value) and is_prime(digit_square_sum_value) and are_coprime(digit_sum_value, digit_square_sum_value)

def count_unusual_numbers(L, R):
    count = 0
    for num in range(L, R + 1):
        if is_unusual_number(num):
            count += 1
    return count

# Đọc đầu vào từ người dùng
L, R = map(int, input().split())

# In số lượng số bất thường trong đoạn [L, R]
print(count_unusual_numbers(L, R))

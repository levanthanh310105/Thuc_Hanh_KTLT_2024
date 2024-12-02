print("le van thanh")
print("mssv: 235752021610020")
def fibonacci_list(n):
    fibonacci = [0, 1]  # Bắt đầu với hai số đầu tiên của dãy Fibonacci
    while True:
        next_fib = fibonacci[-1] + fibonacci[-2]  # Tính số Fibonacci tiếp theo
        if next_fib >= n:
            break
        fibonacci.append(next_fib)
    return fibonacci

# Nhập số n
n = int(input("Nhập số n: "))
print("Danh sách các số Fibonacci nhỏ hơn", n, "là:", fibonacci_list(n))

def print_pattern(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)

if __name__ == "__main__":
    # Ödev için 5 satırlık örnek
    print_pattern(5)

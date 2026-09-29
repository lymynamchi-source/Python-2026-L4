import math

# ==========================================
# CÁC HÀM XỬ LÝ 12 BÀI TẬP
# ==========================================

# Bài 1: Tính diện tích hình tròn
def exercise_1():
    print("\n--- Exercise 1: Circle Area ---")
    r = float(input("Enter circle radius? "))
    area = 3.14 * (r ** 2)
    print(f"Circle area = {area}")


# Bài 2: Đổi nhiệt độ Celsius sang Fahrenheit
def exercise_2():
    print("\n--- Exercise 2: Celsius to Fahrenheit ---")
    c = float(input("Enter the temperature in Celsius? "))
    f = (c * 1.8) + 32
    c_display = int(c) if c.is_integer() else c
    print(f"{c_display} (C) = {f:.1f} (F)")


# Bài 3: Kiểm tra số nguyên tố
def exercise_3():
    print("\n--- Exercise 3: Prime Number Checker ---")
    n = int(input("Enter a number? "))
    if n <= 1:
        print(f"{n} is a NOT prime number")
        return
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is a NOT prime number")


# Bài 4: Kiểm tra số hoàn hảo
def exercise_4():
    print("\n--- Exercise 4: Perfect Number Checker ---")
    n = int(input("Enter a number? "))
    if n <= 0:
        print(f"{n} is a NOT perfect number")
        return
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    if divisors_sum == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is a NOT perfect number")


# Bài 5: Tìm kiếm màu trong danh sách
def exercise_5():
    print("\n--- Exercise 5: Color Lookup ---")
    colors = ["Blue", "Yellow", "Black", "Red", "Pink"]
    color = input("What is your favorite color? ").strip()
    if color in colors:
        print(f"Your colod is at index {colors.index(color)} in my list")
    else:
        print("Sorry, I could not find your color")


# Bài 6: Tạo và in các dãy số bằng range()
def exercise_6():
    print("\n--- Exercise 6: Sequences with range() ---")
    range1 = list(range(0, 7))
    range2 = list(range(1, 11, 3))
    range3 = list(range(5, 0, -1))
    range4 = list(range(6, -3, -2))
    
    print("range1:", ", ".join(map(str, range1)))
    print("range2:", ", ".join(map(str, range2)))
    print("range3:", ", ".join(map(str, range3)))
    print("range4:", ", ".join(map(str, range4)))


# Bài 7: Hàm xóa ký tự $ trong chuỗi
def remove_dollar_sign(s):
    return s.replace("$", "")

def exercise_7():
    print("\n--- Exercise 7: Remove Dollar Sign ---")
    raw_str = input("Enter a string with '$': ")
    result = remove_dollar_sign(raw_str)
    print("Result:", result)


# Bài 8: Hàm trích xuất các phần tử chẵn trong danh sách
def extract_even(l):
    even_list = []
    for item in l:
        if item % 2 == 0:
            even_list.append(item)
    return even_list

def exercise_8():
    print("\n--- Exercise 8: Extract Even Numbers ---")
    raw_input = input("Enter integer numbers separated by space (e.g., 1 4 5 -1 10): ")
    numbers = [int(x) for x in raw_input.split()]
    even_numbers = extract_even(numbers)
    print("Even numbers:", even_numbers)


# Bài 9: Hàm tính giai thừa
def factorial(n):
    if n < 0:
        return None
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def exercise_9():
    print("\n--- Exercise 9: Factorial ---")
    n = int(input("Enter a non-negative integer: "))
    ans = factorial(n)
    if ans is None:
        print("Factorial does not exist for negative numbers.")
    else:
        print(f"{n}! = {ans}")


# Bài 10: Hàm tìm tất cả các ước số
def get_divisors(n):
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

def exercise_10():
    print("\n--- Exercise 10: Divisors of a Number ---")
    n = int(input("Enter an integer: "))
    divisors = get_divisors(n)
    print(f"Divisors of {n}:", divisors)


# Bài 11: Tính khoảng cách giữa hai điểm
def exercise_11():
    print("\n--- Exercise 11: Distance Between Two Points ---")
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    print(f"Distance between two points: {dist:.2f}")


# Bài 12: In hình chữ nhật rỗng kích thước m x n
def print_hollow_rectangle(m, n):
    for i in range(m):
        row_chars = []
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                row_chars.append("*")
            else:
                row_chars.append(" ")
        print(" ".join(row_chars))

def exercise_12():
    print("\n--- Exercise 12: Print Pattern m x n ---")
    m = int(input("Enter number of rows (m): "))
    n = int(input("Enter number of columns (n): "))
    print_hollow_rectangle(m, n)


# ==========================================
# MENU ĐIỀU KHIỂN CHÍNH
# ==========================================

def main():
    while True:
        print("\n" + "=" * 45)
        print("        PYTHON BASICS - LAB SESSION 1")
        print("=" * 45)
        print(" 1. Exercise 1: Circle Area")
        print(" 2. Exercise 2: Celsius to Fahrenheit")
        print(" 3. Exercise 3: Prime Number Checker")
        print(" 4. Exercise 4: Perfect Number Checker")
        print(" 5. Exercise 5: Favorite Color Lookup")
        print(" 6. Exercise 6: Sequences with range()")
        print(" 7. Exercise 7: Remove '$' Sign")
        print(" 8. Exercise 8: Extract Even Numbers")
        print(" 9. Exercise 9: Factorial of a Number")
        print("10. Exercise 10: Get Divisors of a Number")
        print("11. Exercise 11: Distance Between Two Points")
        print("12. Exercise 12: Hollow Rectangle Pattern")
        print(" 0. Exit")
        print("=" * 45)
        
        choice = input("Select an exercise (0-12): ").strip()
        
        if choice == '1':
            exercise_1()
        elif choice == '2':
            exercise_2()
        elif choice == '3':
            exercise_3()
        elif choice == '4':
            exercise_4()
        elif choice == '5':
            exercise_5()
        elif choice == '6':
            exercise_6()
        elif choice == '7':
            exercise_7()
        elif choice == '8':
            exercise_8()
        elif choice == '9':
            exercise_9()
        elif choice == '10':
            exercise_10()
        elif choice == '11':
            exercise_11()
        elif choice == '12':
            exercise_12()
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option! Please enter a number between 0 and 12.")

if __name__ == "__main__":
    main()
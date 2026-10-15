def even_sum_count(numbers):
    even_sum = 0
    even_count = 0

    for num in numbers:
        if num % 2 == 0:
            even_sum += num
            even_count += 1

    return even_sum, even_count

if __name__ == "__main__":
    numbers = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
    print(numbers)
    even_sum, even_count = even_sum_count(numbers)
    print(f"Sum of even numbers: {even_sum}")
    print(f"Count of even numbers: {even_count}")

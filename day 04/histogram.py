def histogram(numbers):
    for num in numbers:
        print(f"{num}: " + "*" * num)

# User input
nums = list(map(int, input("Enter numbers (space-separated): ").split()))

# Print histogram
histogram(nums)
def check_order(names):
    if names == sorted(names):
        return "INCREASING"
    elif names == sorted(names, reverse=True):
        return "DECREASING"
    else:
        return "NEITHER"

# Taking input
N = int(input())  # Number of names
names = [input().strip() for _ in range(N)]  # List of names

# Output result
print(check_order(names))
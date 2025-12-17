# define fuction overlapping
def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# User input
list1 = input("Enter elements of first list (space-separated): ").split()
list2 = input("Enter elements of second list (space-separated): ").split()

# Check overlap
if overlapping(list1, list2):
    print("True")
else:
    print("False")
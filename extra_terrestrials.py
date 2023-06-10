# function for reversing a string
def reverse_str(a_string):
    # using string slicing to reverse a string
    return a_string[::-1]


user_str = input("Enter a string: ")
print(reverse_str(user_str))

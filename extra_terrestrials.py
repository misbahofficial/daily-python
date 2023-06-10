'''
This is a sololearn code coach problem which falls under easy category.
The problem states that: You meet a group of aliens, and their language is just like English except that they say backwards.
Now, the task is take your input and reverse it for them to understand.
'''
# function for reversing a string
def reverse_str(a_string):
    # using string slicing to reverse a string
    return a_string[::-1]


user_str = input("Enter a string: ")
print(reverse_str(user_str))

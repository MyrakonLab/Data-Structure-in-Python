def print_version(x):
    print(x * 2)  # displays the result given, nothing back
    
def return_version(x):
    return x * 2  # returns the result, can be used later

# noe let's try use the result of each function
result_a = return_version(5)  # returns 10
return_b = print_version(5)  # prints 10, but returns None

print(result_a)  # prints 10
print(return_b)  # prints None, since print_version does not return anything


def count_first_letter(names, letter):
    count = 0
    for name in names:
        if name[0] == letter:
            count += 1
            
    return count
    
first_letter = count_first_letter(["Moses", "Mathew", "John"], "M")
print(first_letter)
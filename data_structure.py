# Big O Notation

from pandas import merge


def print_first(names):
    print(names[0])  # O(1) - Constant time complexity
    
    
print_first(["MyrakTech", "Alex", "Sam"])

def student_score(scores):
    print(scores[0])  
    
    
student_score([85, 90, 78, 92])

# O(n) - Linear time complexity  

def print_all(names):
    for name in names:
        print(name)  # O(n) - Linear time complexity
        
        
print_all(["MyrakTech", "Alex", "Sam"])


def contain_name(names, target):
    for name in names:
        if name == target:
            return True  # O(n) - Linear time complexity
    return False  # O(n) - Linear time complexity

print(contain_name(["MyrakTech", "Alex", "Sam"], "Alex"))  # True
print(contain_name(["MyrakTech", "Alex", "Sam"], "John"))  # False


def first_letter(names, letter):
    count = 0
    for name in names:
        if name[0] == letter:
            count += 1  # O(n) - Linear time complexity
        
    return count  # O(n) - Linear time complexity

print(first_letter(["MyrakTech", "Alex", "Sam"], "M"))

# O(n^2) in Big O Notation - Quadratic time complexity

def print_pairs(names):
    for name1 in names:
        for name2 in names:
            print(name1, name2)
            
print_pairs(["Myraktech", "John", "Moses"])


def has_duplicates(names):
    for i in range(len(names)):
        for j in range(len(names)):
            if i != j and names[i] == names[j]:
                return True  # O(n^2) - Quadratic time complexity
    
    return False
print(has_duplicates(["MyrakTech", "Alex", "Sam", "Alex"])) 


def duplicate_num(number):
    for a in range(len(number)):
        for b in range(len(number)):
            if a != b and number[a] == number[b]:
                return True
    
    return False

total_numbers = duplicate_num([12, 34, 56, 4, 78, 45])
print(total_numbers)


# 0(log n) - Logarithmic time complexity

def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if numbers[mid] == target:
            return target  # O(log n) - Logarithmic time complexity
        
        elif numbers[mid] < target:
            left = mid + 1
        
        else:
            right = mid - 1
    return -1  # O(log n) - Logarithmic time complexity


# o (n log n) - Log-linear time complexity

def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers  # O(n log n) - Log-linear time complexity
    
    middle = len(numbers) // 2
    
    left_half = merge_sort(numbers[:middle])
    right_half = merge_sort(numbers[middle:])
    
    return merge(left_half, right_half)  # O(n log n) - Log-linear time complexity

# o(2^n) - Exponential time complexity

def subsets(numbers):
    if not numbers:
        return [[]]

    rest = subsets(numbers[1:])

    return rest + [
        subset + [numbers[0]]
        for subset in rest
    ]
    


# o(n!) - Factorial time complexity

from itertools import permutations

numbers = [1, 2, 3]

for arrangement in permutations(numbers):
    print(arrangement)
    

from itertools import combinations

alphabets = ["a", "b", "c", "d", "e"]

for arrangement in permutations(alphabets):
    print(arrangement)
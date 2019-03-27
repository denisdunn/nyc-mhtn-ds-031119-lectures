# Make a function to determine if a number is odd or even

def odd_even(number):
    if number%2==0:
        return 'even'
    else:
        return 'odd'

# Make a function that takes in a list of numbers and returns the numbers that are even

def even_list(numbers):
    numbers_list=[]
    for number in range(len(numbers)):
        if numbers[number]%2==0:
            numbers_list.append(numbers[number])
    return numbers_list

# Given a list return the unique names in the list

def unique_names(list_of_names):
    answer=[]
    names= set(list_of_names)
    for name in names:
        if name not in list_of_names:
            answer.append(name)


    return answer

# Make a function that determines if a word is a palindrome

def palindrome_detector(string):
    if string == string[::-1]:
        return True
    else:
        return False



print(odd_even(4))
print(odd_even(139))
print(even_list([1,3,4,6,7]))
print(unique_names(['frank', 'john', 'john']))
print(palindrome_detector('racecar'))
print(palindrome_detector('mamam'))

def count_occurrences(lst, elem):

      # This function takes a list 'lst' and an element 'elem'
       # It returns the count of 'elem' in 'lst'
    return lst.count(elem)


# Defining the list to search within
my_list = [1, 2, 3, 2, 3, 5, 4, 3, 2, 8, 6, 9, 0, 3, 1, 2, 4, 5, 4,4, 9, 7, 5,  2, 5, 2]

# Defining the target element to count in the list
target_element = 3
# Calling the count_occurrences function and storing the result
count = count_occurrences(my_list, target_element)

# Printing the count of the target element in the list
print(f"The element {target_element} occurs {count} times in the list.")


#Output
#The element 3 occurs 4 times in the list.

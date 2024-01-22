#Exercise 10: Create a new list from two list using the following condition
#Create a new list from two list using the following condition
#Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

#Create new list new that contain odd numbers from the first list and even numbers from the second list
def create_new_list(list_one, list_two):
    odd_numbers = [num for num in list_one if num % 2 != 0]
    even_numbers = [num for num in list_two if num % 2 == 0]
    new_list = odd_numbers + even_numbers
    return new_list

#Print new list
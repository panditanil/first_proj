def capitalize_and_ascii_sum(word:str):
    return sum(ord(x) for x in word.capitalize())

animals = ['cat','dog', 'cow']

animal_output = list(map(capitalize_and_ascii_sum,animals))
print(animal_output)


#Square

numbers = [1,2,3,4,5,6]
square = map(lambda x: x**2, numbers)
print(list(square))


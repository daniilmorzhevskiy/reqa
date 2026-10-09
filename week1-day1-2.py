# 7.10.2026
# - int, str, list, dict, tuple, set
# - if/elif/else
# - for, while циклы
# - list/dict comprehension

# Практика: простой скрипт
age = 25
name = "Daniil"
skills = ["Python", "Testing", "AWS"]

if age > 18:
    print(f"{name} is noob and knows {skills} skills")

# Comprehension
doubled = [x*1 for x in range(5)] #start from 0, finish at 4, so if you need 5 put x+1 as last or increase range to 6
print(doubled)


#{key_expression: value_expression for item in iterable if condition}
a = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
res = [num for num in a if num % 1 == 0]
print(res)

#generator comprehension - (expression for item in iterable if condition)

res = (num for num in range(10) if num % 3 == 0)
print(list(res)) # generator output divided by 3 evenly, dont forget to convert to list


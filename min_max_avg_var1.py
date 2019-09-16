def my_max_function(numbers):
    max_value = None
    for value in numbers:
        if not max_value:
            max_value = value
        elif value > max_value:
            max_value = value
    return max_value

def my_min_function(numbers):
    min_value = None
    for value in numbers:
        if not min_value:
            min_value = value
        elif value < min_value:
            min_value = value
    return min_value


numbers = [-5, 23, 0, -9, 12, 99, 105, -43]
avg_n = 0
for i in range (len(numbers)):
    avg_n += numbers[i]
    i += 1
avg_n = avg_n / i 
print("The avg is : " ,avg_n)

n_min = my_min_function(numbers)
n_max = my_max_function(numbers)
print("The smalles number is : " ,n_min)
print("The biggest number is : " ,n_max)
print("")

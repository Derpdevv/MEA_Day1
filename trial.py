def multiplication_or_sum(num1, num2):
    #calculate produce of two numbers
    prodct = num1 * num2
    # check if product is less than 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)
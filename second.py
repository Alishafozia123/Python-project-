# Function to calculate product and average
def calculate_product_and_average(a, b, c):
    # Calculate product
    product = a * b * c
    # Calculate average
    average = (a + b + c) / 3
    return product, average

# Get input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    # Calculate product and average
    product, average = calculate_product_and_average(num1, num2, num3)

    # Display the results
    print(f"The product of {num1}, {num2}, and {num3} is: {product}")
    print(f"The average of {num1}, {num2}, and {num3} is: {average}")



def classify_triangle(a, b, c):
    """
    Classifies a triangle based on its side lengths.

    Args:
        a (int or float): Length of the first side.
        b (int or float): Length of the second side.
        c (int or float): Length of the third side.

    Returns:
        str: Type of the triangle ("Equilateral", "Isosceles", "Scalene", or "Not a triangle").
    """
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a triangle"

    if a == b == c:
        return "Equilateral"
    elif a == b or a == c or b == c:
        return "Isosceles"
    else:
        return "Scalene"


# Getting user input
try:
    side1 = float(input("Enter the length of the first side: "))
    side2 = float(input("Enter the length of the second side: "))
    side3 = float(input("Enter the length of the third side: "))

    # Calling the function and printing the result
    result = classify_triangle(side1, side2, side3)
    print(f"The triangle is {result}.")

except ValueError:
    print("Invalid input! Please enter numeric values for the sides.")

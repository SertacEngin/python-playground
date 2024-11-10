"""This is a function that classifies triangles as equilateral, isosceles, or scalene"""

# Equilateral - 3 equal sides
# Isosceles - 2 equal sides
# Scalene - no equal sides


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
    # Check if the given sides form a valid triangle
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a triangle"

    # Check for Equilateral triangle (all sides are equal)
    if a == b == c:
        return "Equilateral"

    # Check for Isosceles triangle (two sides are equal)
    elif a == b or a == c or b == c:
        return "Isosceles"

    # Otherwise, it is a Scalene triangle (all sides are different)
    else:
        return "Scalene"


# Example usage
side1 = 7
side2 = 8
side3 = 8

triangle_type = classify_triangle(side1, side2, side3)
# Output: The triangle is Isosceles.
print(f"The triangle is {triangle_type}.")

# Example Calls
print(classify_triangle(5, 5, 5))
print(classify_triangle(5, 5, 8))
print(classify_triangle(3, 4, 5))
print(classify_triangle(1, 2, 3))

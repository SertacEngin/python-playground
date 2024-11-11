def is_palindrome(s):
    # Remove spaces and make lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]


# Example usage
print(is_palindrome("xaxax"))  # Output: True
print(is_palindrome("xax"))    # Output: False

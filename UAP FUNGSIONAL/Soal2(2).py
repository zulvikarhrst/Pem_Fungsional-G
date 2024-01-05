def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string

string = 'radar'
hasil = is_palindrome(string)
print(hasil) 
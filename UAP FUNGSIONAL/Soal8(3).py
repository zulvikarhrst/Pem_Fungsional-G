def is_palindrome(string):
    cleaned_string = ''.join(char.lower() for char in string if char.isalnum())
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string

string = 'Ada apa dengan si m daffa raihan s'
kata_kalimat = string.split()

palindrome = [kata.lower() for kata in kata_kalimat if is_palindrome(kata)]
non_palindrome = [kata.lower() for kata in kata_kalimat if not is_palindrome(kata)]

print("data:", kata_kalimat)
print("palindrome:", palindrome)
print("non-palindrome:", non_palindrome)
# Fungsi tambah
def add(a, b):
    return a + b

# Fungsi kurang
def minus(a, b):
    return a - b

# Fungsi perkalian
def mult(a, b):
    return a * b

# Fungsi pembagian
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Pembagian oleh nol tidak diperbolehkan"

# Fungsi tree yang mengambil ekspresi dalam bentuk tupel
def tree(expression):
    if isinstance(expression, tuple):
        left, operator, right = expression
        if operator == '+':
            return add(tree(left), tree(right))
        elif operator == '-':
            return minus(tree(left), tree(right))
        elif operator == '*':
            return mult(tree(left), tree(right))
        elif operator == '/':
            return div(tree(left), tree(right))
    else:
        return expression

# Contoh penggunaan
expression_tree = ((2, '+', 3), '*', (5, '-', 1))
result = tree(expression_tree)
print("Hasil evaluasi pohon ekspresi:",result)
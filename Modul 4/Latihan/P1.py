def perkalian(a):
    def dengan(b):
        return a * b
    return dengan

# Higher-Order Function (HOF) 
hasil_kali_dengan_5 = perkalian(5)
result_hof = hasil_kali_dengan_5(3)
print("Dengan HOF : ", result_hof)

# Currying
result_currying = perkalian(5)(3)
print("Dengan Currying : ", result_currying)
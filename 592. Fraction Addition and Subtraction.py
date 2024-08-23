from fractions import Fraction

def fraction_calculator(expression: str) -> str:
    expression = expression.replace(' ', '')
    
    terms = []
    temp = ''
    for char in expression:
        if char in '+-':
            if temp:
                terms.append(temp)
            temp = char  
        else:
            temp += char
    if temp:
        terms.append(temp)  

    total = Fraction(0)

    for term in terms:
        total += Fraction(term)

    return f"{total.numerator}/{total.denominator}"

# expression = "-1/2 + 1/2 - 1/3"
expression = input("Enter the string: ")
result = fraction_calculator(expression)
print("Ans: ",result)  

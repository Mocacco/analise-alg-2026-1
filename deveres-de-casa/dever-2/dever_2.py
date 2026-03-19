def is_palindromo(arr):

    if len(arr) <= 1:
        return True

    if arr[0] == arr[-1]:
        return is_palindromo(arr[1:-1])

    return False


array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "c"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(f"array1 = {array1} ->", "É palíndromo" if is_palindromo(array1) else "Não é palíndromo")
print(f"array2 = {array2} ->", "É palíndromo" if is_palindromo(array2) else "Não é palíndromo")
print(f"array3 = {array3} ->", "É palíndromo" if is_palindromo(array3) else "Não é palíndromo")
print(f"array4 = {array4} ->", "É palíndromo" if is_palindromo(array4) else "Não é palíndromo")
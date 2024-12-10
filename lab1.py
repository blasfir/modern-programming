alphabet = 'abcdefghijklmnopqrstuvwxyz'
def decrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += alphabet[(alphabet.index(char) - 13) % 26]
            else:
                result += alphabet[(alphabet.index(char.lower()) - 13) % 26].upper()
        elif char.isspace():
            result += char
        else:
            raise ValueError("Текст містить недопустимі символи. Дозволені лише латинські літери та пробіли.")
    return result   

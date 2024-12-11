import sys
alphabet = 'abcdefghijklmnopqrstuvwxyz'
def rot_13(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                result += alphabet[(alphabet.index(char) + 13) % 26]
            else:
                result += alphabet[(alphabet.index(char.lower()) + 13) % 26].upper()
        elif char.isspace():
            result += char
        else:
            raise ValueError("Текст містить недопустимі символи. Дозволені лише латинські літери та пробіли.")
    return result 
  
def main():
    try:
        input_text = input("Введіть текст:")
        result = rot_13(input_text)
        print(result)
        sys.exit(0)
    except Exception as e:
        print(f"Помилка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
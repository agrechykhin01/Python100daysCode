alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    result_text = ""
    for letter in text:
        if letter in alphabet:
            letter_index = alphabet.index(letter)

            if direction == "encode":
                new_letter_index = letter_index + shift
            elif direction == "decode":
                new_letter_index = letter_index - shift
            result_text += alphabet[new_letter_index]
        else:
            result_text += letter
    print(f"The {direction}d text is: {result_text}")

from art import logo
print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    caesar(text, shift, direction)

    result = input("Type 'yes' if you want to go again. Otherwise type 'no':\n")
    if result == 'no':
        should_continue = False
        print("Goodbye!")

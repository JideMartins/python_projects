alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input(
    "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encoded_text = ""
    for char in original_text:
        char_index = alphabet.index(char)

        # To avoid IndexOutOfRange error
        index_shift = (char_index + shift_amount) % len(alphabet)

        encoded_text += alphabet[index_shift]
    print(f"original text: {original_text}")
    print(f"encrypted text is {encoded_text}")


encrypt(text, shift)

# Define decrypt function


def encrypt(original_text, shift_amount):
    decoded_text = ""
    for char in original_text:
        char_index = alphabet.index(char)
        index_shift = (char_index - shift_amount) % len(alphabet)

        decoded_text += alphabet[index_shift]
    print(f"original text: {original_text}")
    print(f"decrypted text is {decoded_text}")

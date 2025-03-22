alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Combine both the encrypt and decrypt functions
def caesar(original_text, shift_amount, cipher_direction):
    output_text = ""
    if cipher_direction == "decode":
        # negative if we want to decode
        shift_amount *= -1

    for letter in original_text:
        letter_index = alphabet.index(letter)
        index_shift = letter_index + shift_amount

        # Ensure index remains within list limit
        # index_shift = (char_index + or - shift_amount) % len(alphabet)
        index_shift %= len(alphabet)
        output_text += alphabet[index_shift]
    print(f"Here is your {cipher_direction}d text: {output_text}")

caesar(text, shift, direction)
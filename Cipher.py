from base64 import encode

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art
print(art.logo)

#DECRYPT
def decrypt(original_text,shift_amount,) :
    decoded_word = ""
    for letter in original_text :
        if letter not in alphabet :
            decoded_word += letter
        else :
            position = int(alphabet.index(letter))
            shift_number = position - shift_amount
            if shift_number >= 26 :
                shift_number = shift_number - 26
            decoded_letter = alphabet[shift_number]
            decoded_word += decoded_letter

    print(f"Here is the decoded result: {decoded_word}")



#ENCODE
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        if letter not in alphabet :
            cipher_text += letter
        else :
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {cipher_text}")





def caesar(org_direction,org_text,org_shift) :
    if org_direction == "encode" :
        encrypt(org_text,org_shift)
    if org_direction == "decode" :
        decrypt(org_text,org_shift)

rerun = "yes"
while rerun == "yes" :

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction,text,shift)
    value = input("Do you wish to continue yes or no ?")
    rerun = value
    if rerun == "no" :
        print("Goodbye , This sequence will self destruct in 5 seconds .")





alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
l = len(alpha)

def continue_game():
    while True:
        answer = input("\nDo you want to try again? 'Y' for yes, 'N' for no: ").lower()
        if answer in ["y","n"]:
            break
        else:
            print("Answer is not valid!")
    return answer

def caeser(text, shift, direction):
    caeser_alpha = []
    caeser_text = []

    for letter in alpha:
        caeser_alpha.append(letter)
    
    for i in range (0, shift):
        n = caeser_alpha.pop(0)
        caeser_alpha.append(n)
    
    for char in text:
        if not char.isalpha():
            caeser_text += char
        else:
            for i in range(l):
                if direction == "e":
                    if char == alpha[i]:
                        caeser_text += caeser_alpha[i]
                else:
                    if char == caeser_alpha[i]:
                        caeser_text += alpha[i]
        
    print(''.join(caeser_text))

yn = True

while yn:
    print("\nWelcom to Ceasar Cipher!")
    while True:
        direction = input("Type 'e' for encoding and 'd' for decoding: ").lower()
        if direction in ["e","d"]:
            break
        else:
            print("\nUpsss, invalid choice. Please type a valid answer!")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))

    caeser(text, shift, direction)
        
    choices = continue_game()

    if choices == 'n':
        print("See you next time!")
        yn = False
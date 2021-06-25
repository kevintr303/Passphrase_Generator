import json
import random
import string

words = json.load(open("words.json", "r"))
min_length = 4  # This is the min length for random passphrases
max_length = 7  # This is the max length for random passphrases


######################################
##    Create a random passphrase    ##
##     using inputted password      ##
######################################
def convert(pwd, passphrase=[]):
    # If no password is inputted, generate a random one
    if not pwd:
        pwd = "".join(
            random.choice(string.ascii_uppercase)
            for i in range(random.randint(min_length, max_length))
        )
    # Take each char and append a random word starting with it, if not a letter: just append
    for char in pwd.upper():
        passphrase.append(
            random.choice(words[char] if char in string.ascii_uppercase else char)
        )
    return " ".join(passphrase), pwd.lower()


if __name__ == "__main__":
    psp, pwd = convert(
        input("Enter a password to convert to passphrase (empty for random)\n")
    )
    print(f"Your generated passphrase: {psp}\nPassword form: {pwd}")

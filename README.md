# Passphrase_Generator
**What is a passphrase?** A passphrase is a collection of words combined together to create a phrase. It's basically a password that is easier to remember. Here's an example: ``xaujs`` could be your password. To remember it, a phrase could be used such as ``xray ambitious unruly joke system``, or you could simply use the passphrase as your password. Using a passphrase as your password makes it so your password is really hard to bruteforce (if it isn't a common phrase).

# Usage
This script will generate a random passphrase, or take a password and convert it to a passphrase. It's easy to use. First you need to clone this repo:
```bash
git clone https://github.com/kevintr303/Passphrase_Generator
```
Next, you just run the script ``generate.py``. **There are no dependencies required apart from the Python standard library.** After running it, you will be prompted to enter an existing password, or enter nothing to generate one. You can also use symbols and numbers in your password. For example:
```
Input: he,1ab!
Output: horn enchanting , 1 alike borrow !
```
There will be a space in between characters.

# Settings
In the script, there are two things you could change:
```python3
min_length = 4  # This is the min length for random passphrases
max_length = 7  # This is the max length for random passphrases
```
With the ```words.json``` file, you can add and remove words accordingly. There are already about 2000 words, but you can add more words for uncommon letters such as "X".


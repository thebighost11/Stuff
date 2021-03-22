import hashlib
from urllib.request import urlopen
 
def read_word_list(url):
    try:
        listfile = urlopen(url).read()
    except Exception as e:
        print(" error while reading the wordlist, error:", e)
        exit()
    return listfile
 
 
def hash(passwordlist):
    result = hashlib.sha1(passwordlist.encode())
    return result.hexdigest()
 
 
def bruteforce(guesspasswordlist, actual_password_hash):
    for guesspassword in guesspasswordlist:
        if hash(guesspassword) == actual_password_hash:
            print("your password is:", guesspassword)
            exit()


url = 'https://raw.githubusercontent.com/berzerk0/Probable-Wordlists/master/Real-Passwords/Top12Thousand-probable-v2.txt'
password = '***'
actual_password_hash = hash(password)
 
wordlist = read_word_list(url).decode('UTF-8')
guesspasswordlist = wordlist.split('\n')
bruteforce(guesspasswordlist, actual_password_hash)
print(" I couldn't guess this password")
 
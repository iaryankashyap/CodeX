
'''
~Codex v1.1

This Module is registered under Apache License 2.0

Contact:

    Email: aryank.kashyap77783@gmail.com
    Github: @iaryankashyap

'''

# Importing modules
import smtplib
import random

# Functions

# STACK_FUNCTIONS


def isempty(Stack):
    '''Checks if a stack is empty or not'''
    if len(Stack) == 0:
        return True
    else:
        return False


def delete_first_element(Stack):
    ''' Deletes the first element from the stack and returns a new stack'''
    g = Stack.pop()
    return Stack


def insert_first_element(Stack, element):
    '''Inserts an element at the first positon of the stack and returns a new stack'''
    Stack.append(element)
    return Stack


def auto_stack(size):
    '''Creates a random stack from the given size'''
    stack = []
    for i in range(size):
        a = random.randint(0, 9)
        stack.append(a)
    return stack


def display(Stack):
    '''Displays the stack vertically'''
    print()
    for i in range(len(Stack)-1, -1, -1):
        print(Stack[i])
    print()

# PASSWORD_ENCRYPTION-DECRYPTION_FUNCTIONS


def encrypt(text, key="ZXCVMNBLKJFGHDSAQWEYTRUIOP"):
    '''Encrypts the normal text as per the key'''
    if len(key) != 26 or key.isupper() == False or isstring(text) == False:
        print("KeyError: Key is not valid")
        return
    else:
        normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        cipher_text = ""
        key_list = list(key)
        normal_list = list(normal)
        new_plain = text.upper()

        for i in range(len(new_plain)):
            if new_plain[i].isalpha():
                index = normal_list.index(new_plain[i])
                cipher_text = cipher_text + key_list[index]
            else:
                cipher_text = cipher_text + new_plain[i]
        return cipher_text


def decrypt(text, key="ZXCVMNBLKJFGHDSAQWEYTRUIOP"):
    '''Decrypts the encrypted text as per the key'''

    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plain_text = ""
    key_list = list(key)
    normal_list = list(normal)
    new_plain = text.upper()
    if len(key) != 26 or key.isupper() == False or isstring(text) == False:
        print("KeyError: Key is not valid")
        return
    else:
        for i in range(len(text)):
            if new_plain[i].isalpha():
                index = key_list.index(new_plain[i])
                plain_text = plain_text + normal_list[index]
            else:
                plain_text = plain_text + new_plain[i]
        return plain_text


# STRING_RELATED_FUNCTIONS

def isstring(string):
    '''Checks if entry is a valid string'''
    for i in range(len(string)):
        if string[i].isalpha():
            pass
        else:
            return False


def wordcount(text):
    '''Counts the number of words in a string'''
    count = 1
    for i in range(len(text)):
        if text[i] == " ":
            count = count + 1
    return count


def vowelcount(text):
    '''Counts the number of vowels in a string'''
    count = 0
    for i in range(len(text)):
        if text[i] in ("a", "e", "i", "o", "u"):
            count = count + 1
    return count


def strreverse(string):
    '''Reverses a string'''
    return string[::-1]


# CREDENTIAL_VALIDATION

def phonecheck(number):
    '''Checks the phone number for validation'''
    if len(str(number)) == 10:
        return True
    else:
        return False


def passcheck(password):
    '''Checks the password for validation'''
    upper = 0
    for i in range(len(password)):
        if password[i].isupper():
            upper = upper + 1
    if len(password) > 8 and upper > 1:
        return True
    else:
        print("Error: Password must be more than 8 digits and must include one uppercase letter.")
        return False


def isemail(email):
    '''Checks for a valid email address.'''
    at = 0
    firat = False
    for i in range(len(email)):
        if email[i] == '@':
            at += 1
        if email[0] == '@':
            firat = True
    if at == 1 and firat == False:
        print(True)
    else:
        print(False)

# File_Writing_Credentials


def register_cred(username, password, path):
    '''Registers the username and password to text file as per the path'''
    f = open(path, "a")
    encryption = username+"#"+password+"#"+"$"
    f.write(encryption)
    f.close()


def cred_checker(username, password, path):
    '''Checks if password and username matches with the database as per the path'''
    c = ""
    l = ""
    o = ""
    m = ""
    users = []
    data_list = []
    f = open(path, "r")
    r = f.read()
    for i in range(0, len(r)):
        if r[i] != "$":
            c = c+r[i]
        else:
            data_list = data_list+[c]
            c = ""
            continue

    for i in range(0, len(data_list)):
        o = data_list[i]
        for j in range(0, len(o)):
            if o[j] != "#":
                m = m+o[j]
            else:
                users = users+[m]
                m = ""

        o = ""

    usernms = []
    pswrds = []
    for i in range(0, len(users), 2):
        usernms = usernms+[users[i]]

    for i in range(1, len(users), 2):
        pswrds = pswrds+[users[i]]

    f.close()

    for i in range(0, len(usernms)):
        if username == usernms[i]:
            if password == pswrds[i]:
                return True
            else:
                return False

# OTP_PLUGIN


def send_otp(emailid, admin_email, password):
    '''Sends an e-mail containing otp on the email address passed into the function'''
    x = random.randint(1000, 5000)
    content = "Hello there your OTP is " + str(x) + "\n\nPowered by Codex."
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.ehlo()
    server.login(admin_email, password)
    server.sendmail(admin_email, emailid, content)
    server.close()
    return x


# LIST_FUNCTIONS

def listgreatest(list):
    '''returns greatest element of a list'''
    list.sort()
    return list[len(list)-1]


def uniquelist(list):
    '''deletes all the duplicate elements of a list'''
    l = len(list)
    k = 0
    try:
        while k < l:
            if list.count(list[k]) > 1:
                g = list.pop(k)
                if k == 1:
                    k = k-1
                if k > 1:
                    k = k-2
                else:
                    k = k-1
            k = k+1
    except:
        pass
    else:
        pass
    return list

# DS-ALGOS

# binary search


def binary_search(arr, x):
    arr.sort()
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        # Check if x is present at mid
        if arr[mid] < x:
            low = mid + 1

        # If x is greater, ignore left half
        elif arr[mid] > x:
            high = mid - 1

        # If x is smaller, ignore right half
        else:
            return mid

    # If we reach here, then the element was not present
    return "Not Found"

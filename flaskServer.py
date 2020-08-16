import json
from flask import Flask, request, Response

app = Flask(__name__)

stats = {'Attempts': 0, 'Success': 0}

@app.route('/')
def hello():
    return f'Hello, user!, stats = {stats}'

@app.route('/auth', methods = ['POST'])
def auth():
    stats['Attempts'] += 1
    data = request.json
    login = data['login']
    password = data['password']
    print(login, password)

    with open('C:/Users/admin/.vscode/Bruteforce/users_file.json', 'r') as users_f:
        users = json.load(users_f)

    if login in users and users[login] == password:
        status_code = 200
        stats['Success'] += 1
    else:
        status_code = 401
    
    return Response(status = status_code)

if __name__ == '__main__':
    app.run()
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Witaj w moim API!"}

@app.route('/mojastrona')
def mojastrona():
    return {"message": "To jest moja strona!"}

@app.route('/hello')
def hello():
    name = request.args.get('name')  # Pobierz parametr z URL-a
    if name:
        return f"Hello {name}!"
    else:
        return "Hello!"

if __name__ == '__main__':
    app.run()

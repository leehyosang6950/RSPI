from flask import Flask

app = Flask(__name__)

@app.route('/<manner>')
def hello(manner):
    if manner=='hi':
        return 'hi'
    elif manner=='hello':
        return 'hello world!'

if __name__=="__main__":
    app.run(host='0.0.0.0')

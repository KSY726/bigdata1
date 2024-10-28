from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'so sally can wait she knows its too late'

if __name__ == '__main__':
    app.run()


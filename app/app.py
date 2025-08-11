from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hey, Appsec Family!!\n"

if __name__ == '__main__':
    # use 0.0.0.0 so container maps correctly
    app.run(host='0.0.0.0', port=8080)

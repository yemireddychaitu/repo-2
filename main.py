from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return 'Welcom to python flask world v1 from ci-cd-2'

if __name__ == '__main__':
          app.run(host='0.0.0.0', port=8080)

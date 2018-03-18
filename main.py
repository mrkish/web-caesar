from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def main():
    return


if __name__ == "__main__":
    app.run()
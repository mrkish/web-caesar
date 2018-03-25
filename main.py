from flask import Flask, request, render_template, redirect
from caesar import rotate_string, encrypt
import os
import string

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def main():
    return render_template('base.html', spot='')

@app.route('/', methods=['POST'])
def encrypt():
    mess = request.form['text']

    for char in request.form['rot']:
        is_digit = False
        if char in string.digits:
            is_digit = True 
        else:
            is_digit = False
        cyp = int(request.form['rot'])

    if is_digit == True:
        cyp = int(request.form['rot'])
        encrypted = rotate_string(mess, cyp)
        return render_template('base.html', spot=encrypted) 
    elif is_digit == False:
        encrypted = encrypt(mess, cyp)
        return render_template('base.html', spot=encrypted)
    else:
        return render_template('base.html', spot=encrypted)

if __name__ == "__main__":
    app.run()

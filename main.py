from flask import Flask, redirect
import base64

app = Flask(__name__)

@app.route('/redir/<url64>')
def greet(url64):
    decoded_bytes = base64.urlsafe_b64decode(url64)
    decoded_str = decoded_bytes.decode('ascii')
    return redirect(decoded_str)

if __name__ == '__main__':
    app.run()
from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='.')

@app.route('/')
@app.route('/<path:path>')
def serve_static(path=''):
    if path:
        return send_from_directory('.', path)
    return send_from_directory('.', 'index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def web(): return render_template('index.html')

@app.route('/assets/<path:filename>')
def assets(filename): return send_from_directory('assets', filename)

if __name__ == '__main__':
    app.run(debug=True)
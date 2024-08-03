from flask import Flask, render_template, jsonify
from checker import check_website

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check')
def check():
    try:
        is_open = check_website()
        return jsonify(status="success", is_open=is_open)
    except Exception as e:
        return jsonify(status="error", message=str(e))

if __name__ == '__main__':
    app.run(debug=True)

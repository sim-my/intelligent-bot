from flask import Flask, render_template,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    if(request.form.get('input-url')):
        value = request.form.get('input-url')
    elif(request.form.get('input-text')):
        value = request.form.get('input-text')
    return render_template('ask.html', value = value)

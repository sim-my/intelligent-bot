from flask import Flask, render_template,request, session
from model import tokenize, bot_response
from flask_session import Session
app = Flask(__name__)
SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def sendData():
    if(request.form.get('input-url')):
        value = request.form.get('input-url')
        session['sentence_list'] = tokenize('url',value)
    elif(request.form.get('input-text')):
        value = request.form.get('input-text')
        session['sentence_list'] = tokenize('text',value)
    return render_template('ask.html', sentence_list = session['sentence_list'])

@app.route("/ask")
def get_bot_response():
    if(session.get('sentence_list')):
        userText = request.args.get('msg') 
        list_of_sent = session['sentence_list'] 
        answer = bot_response(userText, list_of_sent )
        return answer
    else:
        return 'No answer'

    

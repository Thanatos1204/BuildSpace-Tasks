from flask import Flask, render_template,request
app = Flask(__name__)

def removeEmptyNewlines(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/count', methods=['GET', 'POST'])
def count():
     text = request.form['text']

     words = len(text.split())
     paras = removeEmptyNewlines(text)
     text = text.replace('\r','')
     text = text.replace('\n','')

     chars = len(text)

     return render_template('index.html',words = words,  paras=paras, chars = chars)



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)

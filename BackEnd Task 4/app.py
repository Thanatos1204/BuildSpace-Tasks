from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
   return render_template('blog.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/contact')
def contact():
    return render_template('contactMe.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 
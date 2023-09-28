from flask import Flask, render_template, request, redirect

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/store', methods=['POST'])
def store():
    title = request.form['title']
    content = request.form['content']
    posts.append({'title': title, 'content': content})
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

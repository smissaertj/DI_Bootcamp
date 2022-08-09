from flask import Flask, render_template
app = Flask(__name__)

# default page
@app.route('/')
def home():
    return "Hello World!"

@app.route('/<name>')
def index(name):
    return render_template('index.html', username=name)

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/blog/articles')
def articles():
    return render_template('articles.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True,port=8080)
from  flask import Flask, render_template, redirect, url_for
app = Flask(__name__)

@app.route('/blog')
def blog():
    return render_template('homepage.html')

@app.route('/blog/articles')
def blog_articles():
    articles = {'title': 'myTitle', 'content': 'myContent', 'author': 'myAuthor'}
    return render_template('articles.html', articles=articles)

@app.route('/profile')
def profile():
    return redirect(url_for('blog'))

if __name__ == "__main__":
    app.run(debug=True,port=8080)
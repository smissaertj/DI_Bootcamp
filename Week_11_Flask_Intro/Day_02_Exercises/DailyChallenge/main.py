from flask import Flask, render_template
from flaskext.markdown import Markdown

app = Flask(__name__)
Markdown(app)


@app.route('/exercises')
def exercises():
    mkd_text = None
    with open('lesson1/exercises.md', mode='r') as file:
        mkd_text = file.read()
    return render_template('index.html', mkd_text=mkd_text)

@app.route('/lesson')
def lesson():
    mkd_text = None
    with open('lesson1/in-this-chapter.md', mode='r') as file:
        mkd_text = file.read()
    return render_template('index.html', mkd_text=mkd_text)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
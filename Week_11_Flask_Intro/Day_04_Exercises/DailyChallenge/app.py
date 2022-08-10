from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')


@app.route('/<bgcolor>')
def color(bgcolor):
    return render_template('color.html', bgcolor=bgcolor)


if __name__ == '__main__':
    app.run(debug=True)
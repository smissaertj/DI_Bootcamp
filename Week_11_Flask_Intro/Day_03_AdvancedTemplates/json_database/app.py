from flask import Flask, render_template
import database_manager # this is our module

app = Flask(__name__)
database_manager.create_database()


@app.route("/")
@app.route("/products")
def products_page():
    data = database_manager.load_database()
    return render_template('my_template.html', products=data)

app.run(debug=True)
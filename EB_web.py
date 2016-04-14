from flask import Flask,render_template,url_for
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def EB():
    return render_template('EB.html')




if __name__ =="__main__":
    app.run(debug=True)
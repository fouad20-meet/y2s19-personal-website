from database import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def homepage1():
	if request.method == 'POST':
		add_rating(request.form['starValue'])
		avg = average()
		return render_template("homepage1.html",avg=avg)
	else:
		avg = average()
		return render_template("homepage1.html",avg=avg)

if __name__ == '__main__':
   app.run(debug = True)
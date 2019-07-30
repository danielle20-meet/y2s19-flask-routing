from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home(Name="Danielle"):
    return render_template("home.html",Name=Name)
@app.route('/student/<int:student_id>')
def display_student(student_id):
 	return render_template("student.html",student_id=student_id)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask,render_template,request
app= Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods=['POST'])
def submit():
    username=request.form['name']
    rollno=request.form['roll']
    email=request.form['email']
    return render_template('results.html',username=name,rollno=roll,email=email)
if __name__=='__main__':
    app.run(debug=True)

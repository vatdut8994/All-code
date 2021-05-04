# from flask import Flask, render_template, request
# app=Flask(__name__)
# @app.route('/')
# def connect():
#     return render_template('index.html')

# @app.route("/result",methods=['GET','POST'])
# def response():
#     if request.method == 'POST':
#         curry = request.form['Curry']
#         chapati = request.form['Chapati']
#         water = request.form['Water']
#         print(curry,chapati,water)
#         return render_template('index.html', Total=t)

# if __name__ == "__main__":
#     app.run()

from flask import Flask,render_template,request
app=Flask(__name__)
@app.route("/")
def fhfhf():
    return render_template("index.html")
@app.route("/result",methods=['GET','POST'])
def fjkfkj():
    if(request.method=='POST'):
        if request.form['buttons'] == 'Select curry':
            curry=request.form['Select Curry']
            print(curry)
        return render_template('index.html')

if __name__=="__main__":
    app.run(print('hello'))
    

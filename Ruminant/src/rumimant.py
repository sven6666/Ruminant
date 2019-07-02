from flask import Flask, render_template, request, url_for, redirect, session
from flask.ext.mysqldb import MySQL
app=Flask(__name__)

@app.route("/")
def eShop():
    return redirect(url_for('home',))
@app.route("/home",methods=['GET','POST'])
def Home():
    return render_template('')
@app.route("/checkout",methods=['GET','POST'])
def Warenkorb():
    return("")
@app.route("/shop",methods=['GET','POST'])
def Waren():
    return("")
@app.route("/login",methods=['GET','POST'])
def login():
    if request.method=='POST':
        loggedIn=true;
        return redirect(url_for('loggedIn',))
    return render_template('Login.html',message=message)


if __name__ == "__main__":
   app.run()

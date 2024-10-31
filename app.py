from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/logout")
def logout():
    return redirect(url_for("home"))

# when submit is clicked
# GET    is not secured it shows the passowrd in the URL
# While POST method is the opposite of GET
@app.route("/submit", methods =['POST','GET'])
def submit():
    if request.method == 'POST':
        user = request.form['username']
        return f"logged in successfullyby post , hello {user}"
    else: 
        user = request.args.get('username')
        return f"logged in successfully by get, hello {user}"

if __name__ == "__main__":
    app.run(debug=True) 
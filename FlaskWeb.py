from flask import Flask , render_template
fisrt_app = Flask(__name__)

@fisrt_app.route("/")
def homepage():
    return render_template("main.html", pagetitle= "homepage" , test = "I'm the home page ")

@fisrt_app.route("/page2")
def name(): 
    return render_template("page2.html" , pagetitle ="about" , test = "I'm the about page ")
if __name__ == "__main__" : 
    fisrt_app.run(debug=True , port=9000)

from flask import Flask , render_template
fisrt_app = Flask(__name__)


data = [("html" , 80) , ("css" , 60), ("js" , 75)]
@fisrt_app.route("/")
def homepage():
    return render_template("main.html", pagetitle= "homepage" , test = "page 1 :  " , mydata = data)

@fisrt_app.route("/page2")
def name(): 
    return render_template("page2.html" , pagetitle ="about" , test = "page 2 :  " , cssfile = "page2" )

@fisrt_app.route("/add") 
def add():
    return render_template("add.html",pagetitle = "add" , test= 'page 3 : ' , cssfile = "add"  )

if __name__ == "__main__" : 
    fisrt_app.run(debug=True , port=9000)
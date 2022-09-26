from flask import Flask,render_template,request
from model import promoted


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/res',methods = ["POST","GET"])
def he():
    if request.method == "POST":
        x1 =  request.form["dep"]
        x2 =  request.form["reg"]
        x3 =  request.form["edu"]
        x4 =  request.form["gen"]
        x5 =  request.form["rec"]
        x6 =  request.form["not"]
        x7 =  int(request.form["age"])
        x8 =  int(request.form["pyr"])
        x9 =  int(request.form["los"])
        x10 =  request.form["awards"]
        x11 =  request.form["avg_train"]
        ans = promoted(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11)
        
        return render_template("result.html",ans= ans)
        
        
        
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
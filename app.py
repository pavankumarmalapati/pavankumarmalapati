from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "Pavan_key"

@app.route("/")

def index():
    flash("what's your rating ?")
    return render_template("index.html")

@app.route("/Rate", methods =["POST", "GET"])

def rate ():
    if request.method == "POST":
        rate_input = int(request.form.get('Rate_input'))
        if rate_input <= 5:
            flash("Thanks for the " + str(request.form['Rate_input']) + " rating, I will do better next time.")
        elif rate_input >= 7 and rate_input <= 8:
            flash("Thanks for the generous " + str(request.form['Rate_input']) + " rating, I will Built a better project next time.")
        else:
            flash("OWW!! I did't expect that. Thanks for the " + str(request.form['Rate_input']) + " rating")
    return render_template("index.html")
app.run(host="0.0.0.0", port=80)
   

    

        


    

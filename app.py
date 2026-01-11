from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
# Login route
#-------K-------
def login():
    if request.method == "POST":
        empname = request.form.get("empname")
        empid = request.form.get("empid")
        empsalary = request.form.get("empsalary")
        #-----Prince------
        #------Toby------

        # No database – just display the entered values----kk
        #------Khushboo------
        #-----Gaurav------
        #-----Anand-------
        return f"""
        <h2>Login Successful</h2>
        <p><b>Employee Name:</b> {empname}</p>
        <p><b>Employee ID:</b> {empid}</p>
        <p><b>Employee Salary:</b> {empsalary}</p>
        """

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)

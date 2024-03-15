from flask import Flask, request, render_template

# Flask constructor
app = Flask(__name__)

# A decorator used to tell the application
# which URL is associated with the function
@app.route('/', methods=["GET", "POST"])
def process_form():
    if request.method == "POST":
        # getting input with name = fname and lname in HTML form
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        password = request.form.get("pass")  # Include password if needed

        # You can perform further processing/validation here if necessary

        return render_template("formular.html", first_name=first_name, last_name=last_name)

    # Render the HTML form when the method is GET
    return render_template("formular.html")

if __name__ == '__main__':
    app.run(debug=True)

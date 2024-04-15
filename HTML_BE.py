from flask import Flask, request, render_template, jsonify
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'martin2kelko@gmail.com'
app.config['MAIL_PASSWORD'] = 'Nepijemrum22'

mail = Mail(app)

@app.route('/', methods=["GET", "POST"])
def process_form():
    if request.method == "POST":
        email = request.form.get("email")

        if not email:
            return jsonify({'error': 'Email address is required!'}), 400

        try:
            msg = Message('Hello from Flask-Mail!',
                          sender='martin2kelko@gmail.com', recipients=[email])
            msg.body = 'This is a test email sent from Flask-Mail.'
            mail.send(msg)
            return jsonify({'message': 'Email sent successfully!'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 500

    return render_template("form.html")

if __name__ == '__main__':
    app.run(debug=True)

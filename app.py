from flask import Flask, render_template, request, redirect
import datetime
import urllib.parse
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///requests.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model
class MaterialRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request_date = db.Column(db.String(20), nullable=False)
    employee = db.Column(db.String(100), nullable=False)
    clip_date = db.Column(db.String(20), nullable=False)
    clip_time = db.Column(db.String(20), nullable=False)
    purpose = db.Column(db.String(200), nullable=False)
    client = db.Column(db.String(100), nullable=False)
    received_by = db.Column(db.String(100), nullable=False)
    whatsapp_number = db.Column(db.String(20), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        employee_name = request.form['employee_name']
        purpose = request.form['purpose']
        client_name = request.form['client_name']
        date_of_clip = request.form['date_of_clip']
        time_of_clip = request.form['time_of_clip']
        received_by = request.form['received_by']
        whatsapp_number = request.form['whatsapp_number']

        request_data = {
            "Request Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Employee": employee_name,
            "Clip Date": date_of_clip,
            "Clip Time": time_of_clip,
            "Purpose": purpose,
            "Client": client_name,
            "Received By": received_by
        }

        # Save to database
        new_request = MaterialRequest(
            request_date=request_data["Request Date"],
            employee=employee_name,
            clip_date=date_of_clip,
            clip_time=time_of_clip,
            purpose=purpose,
            client=client_name,
            received_by=received_by,
            whatsapp_number=whatsapp_number
        )
        db.session.add(new_request)
        db.session.commit()

        # Format the message for WhatsApp
        message = "*NEW MATERIAL REQUEST*\n\n"
        for key, value in request_data.items():
            message += f"*{key}:* {value}\n"

        encoded_message = urllib.parse.quote(message)
        whatsapp_url = f"https://wa.me/{whatsapp_number}?text={encoded_message}"

        return redirect(whatsapp_url)

    return render_template('index.html')

@app.route('/requests')
def view_requests():
    requests = MaterialRequest.query.all()
    return render_template('requests.html', requests=requests)
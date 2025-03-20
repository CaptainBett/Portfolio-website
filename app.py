from flask import Flask, render_template, request, flash, redirect, url_for, send_from_directory
from flask_wtf.csrf import CSRFProtect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
import secrets

load_dotenv()

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), 'static')
)
app.secret_key = os.environ.get('SECRET_KEY', secrets.token_hex(32))
csrf = CSRFProtect(app)

# Optional: Add an explicit route for static files (Flask already does this by default)
@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory(app.static_folder, filename)

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASSWORD')

def send_email(form_data):
    message = MIMEMultipart()
    message['From'] = app.config['MAIL_USERNAME']
    message['To'] = 'enockbett427@gmail.com'
    message['Subject'] = f"New Contact: {form_data['inputSubject3']}"
    
    body = f"""
    New contact form submission from captaincodes.co.ke:
    
    Name: {form_data['inputName3']}
    Email: {form_data['inputEmail3']}
    Category: {form_data['inputSelect3']}
    
    Message:
    {form_data['inputMessage3']}
    """
    
    message.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP(app.config['MAIL_SERVER'], app.config['MAIL_PORT']) as server:
        server.starttls()
        server.login(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        server.send_message(message)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and request.form.get('form_id') == 'contact_form':
        form_data = {
            'inputName3': request.form.get('inputName3'),
            'inputEmail3': request.form.get('inputEmail3'),
            'inputSubject3': request.form.get('inputSubject3'),
            'inputSelect3': request.form.get('inputSelect3'),
            'inputMessage3': request.form.get('inputMessage3')
        }
        
        # Basic validation
        if not all([form_data['inputName3'], form_data['inputEmail3'], form_data['inputMessage3']]):
            flash('Please fill in all required fields', 'danger')
        else:
            try:
                send_email(form_data)
                flash('Message sent successfully!', 'success')
            except Exception as e:
                flash('Failed to send message. Please try again later.', 'danger')
                app.logger.error(f"Email failed to send: {str(e)}")
        
        return redirect(url_for('index', _anchor='contact'))
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
 
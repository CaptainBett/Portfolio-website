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
    # Create a MIMEMultipart message with alternative parts (plain and HTML)
    message = MIMEMultipart("alternative")
    message['From'] = app.config['MAIL_USERNAME']
    message['To'] = 'captainbett77@gmail.com'
    message['Subject'] = f"New Contact Inquiry: {form_data['inputSubject3']}"

    # Plain text version
    text = f"""\
Dear Captain Bett,

You have received a new contact inquiry from the website captaincodes.co.ke.

Details of the submission are as follows:

Name: {form_data['inputName3']}
Email: {form_data['inputEmail3']}

Message:
{form_data['inputMessage3']}

We kindly request you to review the inquiry at your earliest convenience.

Best regards,
Your Website Team
"""

    # HTML version for a premium, formatted look
    html = f"""\
<html>
  <head>
    <style>
      body {{
        font-family: Arial, sans-serif;
        line-height: 1.6;
        color: #333;
      }}
      .content {{
        max-width: 600px;
        margin: auto;
      }}
      .header {{
        background-color: #f8f8f8;
        padding: 10px;
        text-align: center;
        border-bottom: 1px solid #ddd;
      }}
      .details {{
        padding: 20px;
      }}
      .details table {{
        width: 100%;
        border-collapse: collapse;
      }}
      .details td {{
        padding: 8px;
        vertical-align: top;
      }}
      .details tr:nth-child(even) {{
        background-color: #f2f2f2;
      }}
      .footer {{
        padding: 10px;
        text-align: center;
        font-size: 0.9em;
        color: #777;
      }}
    </style>
  </head>
  <body>
    <div class="content">
      <div class="header">
        <h2>New Contact Inquiry</h2>
      </div>
      <div class="details">
        <p>Dear Captain Bet,</p>
        <p>You have received a new inquiry from <strong>captaincodes.co.ke</strong>. Please review the details below:</p>
        <table>
          <tr>
            <td><strong>Name:</strong></td>
            <td>{form_data['inputName3']}</td>
          </tr>
          <tr>
            <td><strong>Email:</strong></td>
            <td>{form_data['inputEmail3']}</td>
          </tr>
          <tr>
            <td><strong>Category:</strong></td>
            <td>{form_data['inputSelect3']}</td>
          </tr>
          <tr>
            <td colspan="2"><strong>Message:</strong><br>{form_data['inputMessage3']}</td>
          </tr>
        </table>
        <p>We kindly request you to review this inquiry at your earliest convenience.</p>
      </div>
      <div class="footer">
        <p>Best regards,<br>Your Website Team</p>
      </div>
    </div>
  </body>
</html>
"""

    # Attach both parts to the message
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    message.attach(part1)
    message.attach(part2)

    # Send the email via SMTP with TLS encryption
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
    app.run(debug=True,port=5002)
 
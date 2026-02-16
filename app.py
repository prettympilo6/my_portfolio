from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Nompilo@2010'

# Email configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME') or 'prettynompilo6@gmail.com'  
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD') or 'kbkptteaidvugeql'
app.config['MAIL_DEFAULT_SENDER'] = 'prettynompilo6@gmail.com'

# Initialize Flask-Mail
mail = Mail(app)

# Portfolio data
portfolio_data = {
    "name": "Nompilo",
    "full_name": "Nompilo",
    "title": "ICT Graduate | Junior Business Analyst | Aspiring Systems Analyst",
    "summary": "I am an ICT graduate specialising in Business Analysis and Systems Development with strong exposure to analysing organisational problems and designing ICT-based solutions. I have worked on academic projects involving web-based systems and facial recognition attendance solutions, and I have hands-on experience supporting university systems and administrative operations. I am passionate about building practical, efficient, and user-centred technology solutions and I am eager to grow within the ICT industry.",
    "skills": [
        {"category": "Business Analysis", "items": ["Requirements Gathering", "System Documentation", "Process Mapping", "Stakeholder Engagement"]},
        {"category": "Systems Development", "items": ["Web-Based Systems", "Facial Recognition", "Database Design", "System Analysis"]},
        {"category": "Technical", "items": ["HTML / CSS", "Python", "SQL", "ICT Infrastructure"]},
        {"category": "Soft Skills", "items": ["Problem Solving", "Communication", "Detail Oriented", "Adaptability"]}
    ],
    "projects": [
        {
            "title": "Facial Recognition Attendance System",
            "description": "Designed and developed an academic project implementing a facial recognition-based attendance tracking solution for educational environments, reducing manual processes and improving accuracy.",
            "tech": ["Python", "Computer Vision", "Systems Analysis"],
            "category": "Systems Development",
            "github": "https://github.com/yourusername/facial-recognition-attendance"  #actual repo
        },
        {
            "title": "Web-Based Information System",
            "description": "Built a web-based system as part of academic coursework, focusing on user-centred design principles and efficient data management for organisational workflows.",
            "tech": ["HTML", "CSS", "JavaScript", "Database Design"],
            "category": "Web Development",
            "github": "https://github.com/yourusername/web-information-system"  #actual repo
        },
        {
            "title": "University Systems Support",
            "description": "Provided hands-on support for university administrative systems and operations, assisting with ICT infrastructure and ensuring smooth operational continuity.",
            "tech": ["ICT Support", "Systems Administration", "Documentation"],
            "category": "Systems Support",
            "github": ""  # Leave empty if no repo
        }
    ],
    "education": [
        {
            "degree": "ICT Diploma",
            "specialisation": "Business Analysis & Systems Development",
            "institution": "University",
            "description": "Specialised in analysing organisational problems and designing ICT-based solutions with a focus on business and systems alignment."
        }
    ],
    "contact": {
        "email": "prettynompilo6@gmail.com",  
        "linkedin": "https://www.linkedin.com/in/nompilo-pretty-mbatha-340233261/",  # Add your LinkedIn URL
        "github": "https://github.com/prettympilo6",  # Add your GitHub username
        "instagram": "https://www.instagram.com/nompiloprettymbatha/"  # Add your Instagram username
    }
}

@app.route("/")
def home():
    return render_template("home.html", data=portfolio_data)

@app.route("/about")
def about():
    return render_template("about.html", data=portfolio_data)

@app.route("/projects")
def projects():
    return render_template("projects.html", data=portfolio_data)

@app.route("/contact")
def contact():
    return render_template("contact.html", data=portfolio_data)

@app.route("/send-message", methods=["POST"])
def send_message():
    """Handle contact form submission and send email"""
    try:
        # Get form data
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        subject = request.form.get('subject', '').strip()
        message = request.form.get('message', '').strip()
        
        # Validate required fields
        if not all([name, email, message]):
            return jsonify({
                'success': False,
                'message': 'Please fill in all required fields.'
            }), 400
        
        # Create email message
        msg = Message(
            subject=f"Portfolio Contact: {subject or 'New Message'}",
            sender=app.config['MAIL_DEFAULT_SENDER'],
            recipients=[app.config['MAIL_USERNAME']],
            reply_to=email
        )
        
        # Email body
        msg.body = f"""
New message from your portfolio contact form:

From: {name}
Email: {email}
Subject: {subject or 'No subject'}

Message:
{message}

---
Sent on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Reply to this email to respond directly to the sender.
        """
        
        msg.html = f"""
        <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; background-color: #f9f9f9;">
            <div style="background-color: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                <h2 style="color: #A8792A; margin-top: 0;">New Portfolio Contact Message</h2>
                
                <div style="background-color: #f5f5f5; padding: 15px; border-radius: 4px; margin: 20px 0;">
                    <p style="margin: 5px 0;"><strong>From:</strong> {name}</p>
                    <p style="margin: 5px 0;"><strong>Email:</strong> <a href="mailto:{email}">{email}</a></p>
                    <p style="margin: 5px 0;"><strong>Subject:</strong> {subject or 'No subject'}</p>
                </div>
                
                <div style="background-color: #ffffff; padding: 15px; border-left: 3px solid #A8792A; margin: 20px 0;">
                    <h3 style="color: #333; margin-top: 0;">Message:</h3>
                    <p style="color: #555; line-height: 1.6; white-space: pre-wrap;">{message}</p>
                </div>
                
                <hr style="border: none; border-top: 1px solid #e0e0e0; margin: 20px 0;">
                
                <p style="color: #999; font-size: 12px; margin: 10px 0;">
                    Sent on: {datetime.now().strftime('%Y-%m-%d at %H:%M:%S')}
                </p>
                <p style="color: #999; font-size: 12px; margin: 10px 0;">
                    Reply to this email to respond directly to the sender.
                </p>
            </div>
        </div>
        """
        
        # Send the email
        mail.send(msg)
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.'
        }), 200
        
    except Exception as e:
        print(f"Error sending email: {str(e)}")
        return jsonify({
            'success': False,
            'message': 'Sorry, there was an error sending your message. Please try again later or contact me directly via email.'
        }), 500

@app.route("/api/data")
def api_data():
    return jsonify(portfolio_data)

if __name__ == "__main__":
    app.run(debug=True)

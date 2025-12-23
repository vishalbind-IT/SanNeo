from flask import Flask, render_template_string, request, jsonify,render_template
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# Mock Database for Projects with Mini Case Studies
PROJECTS = [
    {
        "id": 1,
        "title": "AI Resume Job Matcher",
        "category": "Web",
        "image": "/static/images/ai_resume_project.png",
        "description": "An intelligent platform that matches resumes with job descriptions using NLP and Generative AI for skill similarity scoring and recommendations.",
        "tech": ["Python", "FastAPI", "Generative AI","MySQL"],
        "challenge": "Analyzing resumes and job descriptions written in different formats and structures, and accurately identifying relevant skills, experience, and job fit in an automated way.",
        "solution": "Developed a FastAPI-based backend that processes resumes and job descriptions, extracts key skills using NLP techniques, and applies Generative AI logic to calculate similarity scores and matching insights.",
        "result": "Delivered a functional AI-powered resume matching system that provides clear match scores, highlights missing skills, and helps users quickly identify suitable job opportunities."
    },
    {
        "id": 2,
        "title": "Grocery E-Commerce Web Application",
        "category": "Web",
        "image": "/static/images/grocery_project.png",
        "description": "A complete online grocery platform that allows users to browse products, manage carts, place orders, and track purchases through a secure and responsive interface.",
        "tech": ["Python",  "Flask",  "MySQL",  "HTML",  "CSS",  "JavaScript", "Bootstrap"],
        "challenge": "Building a scalable and user-friendly grocery platform with secure authentication, real-time cart updates, and reliable order management while maintaining good performance and clean UI.",
        "solution": "Developed a full-stack web application using Flask with structured backend logic, optimized MySQL queries, session-based authentication, and a responsive frontend built with Bootstrap and JavaScript.",
        "result": "Successfully delivered a fully functional grocery web application with smooth user experience, secure backend operations, and responsive design suitable for real-world usage."
    },
    {
        "id": 3,
        "title": "Online Banking Management System",
        "category": "Web",
        "image": "/static/images/online_bank_project.png",
        "description": "A secure full-stack banking web application that enables users to create accounts, perform deposits and withdrawals, and track transaction history with a responsive and user-friendly interface.",
        "tech": ["Django", "MySQL", "Flask", "Python", "HTML", "CSS", "JavaScript", "Bootstrap"],
        "challenge": "Building a secure and reliable banking system that handles user accounts, transactions, and sensitive financial data while ensuring data consistency, validation, and a clear user experience.",
        "solution": "Developed a full-stack banking management system using Flask with structured backend logic, secure authentication, transaction handling, and optimized MySQL queries. Implemented a responsive frontend using Bootstrap and JavaScript for smooth user interaction.",
        "result": "Delivered a fully functional banking system supporting account creation, deposits, withdrawals, balance tracking, and transaction history, demonstrating strong backend engineering and full-stack development skills."
    }   
]

# Client & Testimonial Data
CLIENTS = ["Stripe", "Framer", "Airbnb", "Intercom", "Linear"]
TESTIMONIALS = [
    {
        "quote": "Alex is a rare talent who deeply understands both the aesthetic and the engineering. The dashboard he built for us is world-class.",
        "author": "Sarah Chen",
        "role": "CTO at Nexus Labs",
        "image": "https://i.pravatar.cc/150?u=sarah"
    },
    {
        "quote": "Working with Alex was the best decision for our rebranding. The technical performance of the site is simply unmatched.",
        "author": "James Wilson",
        "role": "Founder of Ethereal",
        "image": "https://i.pravatar.cc/150?u=james"
    }
    
]

#------Render_Templates--------
@app.route('/')
def index():
    return render_template("index.html", PROJECTS=PROJECTS, CLIENTS=CLIENTS, TESTIMONIALS=TESTIMONIALS)

SENDER_EMAIL = os.environ.get("farzigmng7@gmail.com")
APP_PASSWORD = os.environ.get("jhpgvixeqknztfqg")
RECEIVER_EMAIL = os.environ.get("farzigmng7@gmail.com")


@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
  
    # ---------- SEND EMAIL ----------
    msg = EmailMessage()
    msg['Subject'] = "New Portfolio Contact"
    msg['From'] = "farzigmng7@gmail.com"
    msg['To'] = "farzigmng7@gmail.com"
    msg.set_content(f"""
New message received from your portfolio:

Name: {name}
Email: {email}

Message:
{message}
    """)
    #-------Error Handling--------
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("farzigmng7@gmail.com", "jhpgvixeqknztfqg")
            smtp.send_message(msg)
            return jsonify({"success": True})
    except Exception:
        return jsonify({"success": False}), 500
    

from flask import Flask, render_template_string, request, jsonify



app = Flask(__name__)




# Mock Database for Projects with Mini Case Studies
# IMPROVEMENT: Added 'live_url', 'github_url', and 'features' to support the new Live View requirements
PROJECTS = [
    {
        "id": 1,
        "title": "SanNeo – Personal Portfolio Website",
        "category": "SAAS",
        "image": "/static/images/portfolio_project.png",
        "description": "A modern personal portfolio website designed to showcase projects, skills, and professional experience with a clean layout, smooth interactions, and responsive design.",
        "tech": ["HTML", "CSS", "JavaScript", "Bootstrap"],
        "challenge": "Creating a professional personal brand website that effectively highlights projects, skills, and contact information while maintaining fast performance, accessibility, and visual consistency.",
        "solution": "Designed and developed a fully responsive portfolio website using HTML, CSS, Bootstrap, and JavaScript with structured sections, reusable components, and clean UI patterns.",
        "result": "Successfully launched a polished portfolio website that serves as a professional online presence for freelancing and job opportunities, enabling clear project presentation and easy client contact.",
        "live_url": "https://sanneo.onrender.com/", 
        "github_url": "#", 
        "features": ["Professional Hero Section",
        "Projects & Work Showcase",
       "Skills & Tech Stack Display",
       "Contact Form UI",
       "Responsive Layout (Mobile & Desktop)",
       "Clean & Modern UI Design"] 
    },
    {
        "id": 2,
        "title": "AI Resume Job Matcher",
        "category": "Mobile",
        "image": "/static/images/ai_resume_project.png",
        "description": "An intelligent platform that matches resumes with job descriptions using NLP and Generative AI for skill similarity scoring and recommendations.",
        "tech": ["Python", "FastAPI", "Generative AI","MySQL"],
        "challenge": "Analyzing resumes and job descriptions written in different formats and structures, and accurately identifying relevant skills, experience, and job fit in an automated way.",
        "solution": "Developed a FastAPI-based backend that processes resumes and job descriptions, extracts key skills using NLP techniques, and applies Generative AI logic to calculate similarity scores and matching insights.",
        "result": "Delivered a functional AI-powered resume matching system that provides clear match scores, highlights missing skills, and helps users quickly identify suitable job opportunities.",
        "live_url": "https://example.com", 
        "github_url": "#", 
        "features": ["Wearable API Integration", "Offline Mode", "Biometric Encryption"] 
    },
    {
             "id": 3,
        "title": "YumioRunner – Food Delivery Landing Page",
        "category": "Web",
        "image": "/static/images/yumiorunner_project.png",
        "description": "A modern, polished single-page application for food delivery, showcasing restaurant listings, popular dishes, categories, app promotion, and enhanced user interactions with a focus on clean UI and smooth UX.",
        "tech": ["HTML", "CSS", "JavaScript", "Bootstrap", "Tailwind CSS"],
        "challenge": "Designing a high-conversion, interactive food delivery SPA with persistent cart, favorites, modals for product details, authentication flows, and responsive design across all devices.",
        "solution": "Built a fully responsive single-page application using HTML, CSS, Bootstrap, Tailwind, and JavaScript. Added structured sections, reusable components, smooth interactions, lazy-loading images, toast notifications, dark mode toggle, and localStorage data persistence.",
        "result": "Delivered a professional, visually appealing, and interactive food delivery SPA with persistent state, enhanced UI/UX, quick product details, favorites system, and simulated order tracking, suitable for startups, demos, and client presentations.",
        "live_url": "https://yumiorunner.onrender.com", 
        "github_url": "#", 
        "features": ["Enhanced Authentication: Sign In / Sign Up with validation and loading states",
        "Persistent Cart & Favorites using localStorage",
        "Quick View Product Details Modal with nutritional info",
        "Dynamic Order Tracking Simulation",
        "Responsive Navigation & Hero Section",
        "Food Categories & Popular Items UI",
        "Mobile & Tablet Responsive Design",
        "Scroll to Top Button and Dark Mode Toggle",
        "Loading spinners & improved toast notifications"] 
    }
]

# Client & Testimonial Data (Unchanged)
CLIENTS = ["Stripe", "Framer", "Airbnb", "Intercom", "Linear"]
TESTIMONIALS = [
    {
        "quote": "Vish is a rare talent who deeply understands both the aesthetic and the engineering. The dashboard he built for us is world-class.",
        "author": "Sarah Chen",
        "role": "CTO at Nexus Labs",
        "image": "https://i.pravatar.cc/150?u=sarah"
    },
    {
        "quote": "Working with Vish was the best decision for our rebranding. The technical performance of the site is simply unmatched.",
        "author": "James Wilson",
        "role": "Founder of Ethereal",
        "image": "https://i.pravatar.cc/150?u=james"
    }
]

# --- TEMPLATE PARTS ---

SHARED_HEAD = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>SanNeo</title>
    
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Google Fonts: Inter & Poppins -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&family=Poppins:wght@700&display=swap" rel="stylesheet">
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>

    <style>
        /* --- ORIGINAL STYLES PRESERVED --- */
        :root {
            --bg-body: #f8fafc;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --accent-primary: #6366f1;
            --accent-secondary: #0ea5e9;
            --card-bg: #ffffff;
            --border-light: rgba(0, 0, 0, 0.08);
            --nav-bg: rgba(248, 250, 252, 0.9);
        }

        body {
            background-color: var(--bg-body);
            color: var(--text-main);
            font-family: 'Inter', sans-serif;
            overflow-x: hidden;
            scroll-behavior: smooth;
        }

        h1, h2, h3, .navbar-brand { font-family: 'Poppins', sans-serif; font-weight: 700; }

        .animated-bg {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%; z-index: -1;
            background: linear-gradient(-45deg, #f8fafc, #f1f5f9, #e0e7ff, #f3f4f6);
            background-size: 400% 400%; animation: gradientShift 15s ease infinite;
        }

        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .navbar {
            backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px);
            background: transparent; border-bottom: 1px solid transparent;
            padding: 1.5rem 0; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }

        .navbar.scrolled {
            background: var(--nav-bg); border-bottom: 1px solid var(--border-light);
            padding: 0.85rem 0; box-shadow: 0 4px 20px rgba(0, 0, 0, 0.03);
        }

        .navbar-brand { font-size: 1.6rem; letter-spacing: -1px; transition: transform 0.3s ease; }
        .navbar-brand:hover { transform: scale(1.05); }

        .nav-link {
            color: var(--text-main) !important; font-weight: 600; font-size: 0.95rem; margin: 0 12px;
            position: relative; padding: 5px 0 !important; transition: color 0.3s ease;
        }

        .nav-link::after {
            content: ''; position: absolute; bottom: 0; left: 0; width: 0; height: 2px;
            background: var(--accent-primary); transition: width 0.3s ease;
        }

        .nav-link:hover { color: var(--accent-primary) !important; }
        .nav-link:hover::after { width: 100%; }

        @media (max-width: 991.98px) {
            .navbar { padding: 1rem 0; background: var(--nav-bg) !important; border-bottom: 1px solid var(--border-light) !important; }
            .navbar-collapse {
                background: var(--card-bg); margin-top: 1rem; padding: 1.5rem;
                border-radius: 1.5rem; border: 1px solid var(--border-light);
                box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
            }
            .nav-link { margin: 10px 0; padding: 10px 0 !important; }
            .nav-link::after { display: none; }
        }

        /* Hero Specifics */
        .hero-section { min-height: 100vh; display: flex; align-items: center; padding-top: 100px; padding-bottom: 60px; overflow: hidden; }
        
        /*Improved Hero Title*/
        .hero-title {
            background: linear-gradient(to right, var(--text-main) 20%, var(--accent-primary) 40%, var(--accent-secondary) 60%, var(--text-main) 80%);
            background-size: 200% auto;
            color: var(--text-main);
            background-clip: text;
            text-fill-color: transparent;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: shine 5s linear infinite;
            line-height: 1.1;
            letter-spacing: -0.02em;
        }
        
        
        
        .kinetic-text {
            background: linear-gradient(to right, var(--text-main) 20%, var(--accent-primary) 40%, var(--accent-secondary) 60%, var(--text-main) 80%);
            background-size: 200% auto; color: var(--text-main); background-clip: text;
            text-fill-color: transparent; -webkit-background-clip: text; -webkit-text-fill-color: transparent;
            animation: shine 5s linear infinite; font-size: clamp(2.5rem, 8vw, 5rem);
            line-height: 1.1; letter-spacing: -0.02em;
        }
        @keyframes shine { to { background-position: 200% center; } }

        .hero-visual-container { position: relative; z-index: 1; perspective: 1000px; }
        .hero-main-img {
            width: 100%; max-width: 500px; border-radius: 2rem;
            box-shadow: 0 20px 80px rgba(99, 102, 241, 0.2);
            animation: floatHero 6s ease-in-out infinite; position: relative; z-index: 2;
        }
        .hero-decorative-card {
            position: absolute; background: rgba(255, 255, 255, 0.8); backdrop-filter: blur(10px);
            padding: 1rem; border-radius: 1rem; border: 1px solid var(--border-light);
            box-shadow: 0 10px 30px rgba(0,0,0,0.05); z-index: 3;
            animation: floatHero 8s ease-in-out infinite alternate-reverse;
        }
        .card-1 { top: -20px; right: -30px; animation-delay: 1s; }
        .card-2 { bottom: 40px; left: -40px; animation-delay: 2s; }
        
        .glow-sphere {
            position: absolute; width: 300px; height: 300px;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.2) 0%, transparent 70%);
            border-radius: 50%; filter: blur(40px); z-index: 0; animation: pulseGlow 10s infinite;
        }
        @keyframes floatHero {
            0% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(1deg); }
            100% { transform: translateY(0) rotate(0deg); }
        }
        @keyframes pulseGlow {
            0%, 100% { transform: scale(1); opacity: 0.5; }
            50% { transform: scale(1.3); opacity: 0.8; }
        }

        /* Buttons */
        .btn-premium {
            background: linear-gradient(45deg, var(--accent-primary), var(--accent-secondary));
            border: none; padding: 14px 36px; border-radius: 50px; color: white !important;
            font-weight: 600; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            text-decoration: none; display: inline-block; text-align: center;
        }
        .btn-premium:hover { transform: translateY(-3px); box-shadow: 0 12px 24px rgba(99, 102, 241, 0.3); }

        /* IMPROVEMENT: Custom Live Demo Button Styles */
        .btn-live-demo {
            background: var(--text-main);
            color: white;
            border: none;
            padding: 10px 24px;
            border-radius: 50px;
            font-weight: 600;
            font-size: 0.9rem;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: 0 4px 12px rgba(15, 23, 42, 0.15);
            cursor: pointer;
        }

        .btn-live-demo:hover {
            background: var(--accent-primary);
            transform: translateY(-2px);
            box-shadow: 0 8px 20px rgba(99, 102, 241, 0.3);
            color: white;
        }
        
        .btn-live-demo i { transition: transform 0.3s ease; }
        .btn-live-demo:hover i { transform: scale(1.1); }

        .btn-outline-custom {
            border: 1px solid var(--border-light); padding: 14px 36px; border-radius: 50px;
            color: var(--text-main); transition: all 0.3s ease; text-decoration: none;
            display: inline-block; text-align: center;
        }
        .btn-outline-custom:hover { border-color: var(--accent-primary); background: #fff; }

        /* Project Cards & Filters */
        .filter-wrapper { overflow-x: auto; -webkit-overflow-scrolling: touch; padding-bottom: 10px; margin-bottom: 30px; }
        .filter-container { display: inline-flex; gap: 12px; justify-content: center; min-width: 100%; }
        .filter-btn {
            background: var(--card-bg); border: 1px solid var(--border-light); color: var(--text-main);
            padding: 10px 24px; border-radius: 30px; cursor: pointer; transition: all 0.3s ease;
            font-weight: 500; white-space: nowrap;
        }
        .filter-btn.active { background: var(--accent-primary); border-color: var(--accent-primary); color: white; }

        .project-card {
            background: var(--card-bg); border: 1px solid var(--border-light); border-radius: 24px;
            overflow: hidden; transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1); height: 100%;
            display: flex; flex-direction: column; box-shadow: 0 4px 20px rgba(0,0,0,0.03);
        }
        .project-card:hover { transform: translateY(-10px); border-color: var(--accent-primary); box-shadow: 0 15px 35px rgba(0,0,0,0.08); }
        .project-img { height: 250px; object-fit: cover; width: 100%; transition: transform 0.6s ease; }
        .project-card:hover .project-img { transform: scale(1.08); }

        /* Other Sections */
        .service-card {
            background: var(--card-bg); border: 1px solid var(--border-light); border-radius: 24px;
            padding: 2rem; transition: all 0.3s ease; height: 100%; display: flex; flex-direction: column;
            box-shadow: 0 4px 20px rgba(0,0,0,0.02);
        }
        .service-card:hover { border-color: var(--accent-primary); transform: translateY(-5px); }
        .price-range { font-size: 1.25rem; font-weight: 800; color: var(--accent-secondary); margin: 20px 0; }
        
        .testimonial-card { background: var(--card-bg); border: 1px solid var(--border-light); border-radius: 24px; padding: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.02); }
        .client-logo { filter: grayscale(1); opacity: 0.5; transition: all 0.3s ease; max-width: 120px; }
        .client-logo:hover { filter: grayscale(0); opacity: 1; transform: scale(1.1); }
        
        .skill-item {
            background: var(--card-bg); border: 1px solid var(--border-light); border-radius: 16px;
            padding: 24px; text-align: center; transition: all 0.3s ease; box-shadow: 0 4px 15px rgba(0,0,0,0.02);
        }
        .skill-item:hover { background: var(--accent-primary); color: white; border-color: var(--accent-primary); }
        .skill-item:hover i { color: white !important; }

        .timeline { border-left: 2px solid var(--border-light); padding-left: 25px; position: relative; }
        .timeline-item { margin-bottom: 40px; position: relative; }
        .timeline-item::before {
            content: ''; position: absolute; left: -34px; top: 6px; width: 16px; height: 16px;
            border-radius: 50%; background: var(--accent-primary); box-shadow: 0 0 10px var(--accent-primary);
        }

        .form-control { background: #fff; border: 1px solid var(--border-light); color: var(--text-main); padding: 15px; border-radius: 12px; }
        .form-control:focus { box-shadow: 0 0 0 0.25rem rgba(99, 102, 241, 0.1); border-color: var(--accent-primary); }

        .reveal { opacity: 0; transform: translateY(30px); transition: opacity 0.8s ease-out, transform 0.8s ease-out; visibility: hidden; }
        .reveal.active { opacity: 1; transform: translateY(0); visibility: visible; }
        
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: var(--bg-body); }
        ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 10px; }
        ::-webkit-scrollbar-thumb:hover { background: var(--accent-primary); }

        /* LIVE PREVIEW STYLES */
        .modal-live-view .modal-content { border-radius: 1.5rem; overflow: hidden; border: none; }
        .iframe-container {
            position: relative; width: 100%; padding-bottom: 56.25%; /* 16:9 Aspect Ratio */
            background: #f1f5f9;
        }
        .iframe-container iframe {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none;
        }
        .iframe-fallback {
            position: absolute; top: 0; left: 0; width: 100%; height: 100%;
            display: flex; flex-direction: column; align-items: center; justify-content: center;
            background: #f8fafc; text-align: center;
        }

        /* --- IMPROVEMENT: CLIENT SCROLLER ANIMATION --- */
        .client-scroller {
            overflow: hidden;
            width: 100%;
            position: relative;
            mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
            -webkit-mask-image: linear-gradient(to right, transparent, black 10%, black 90%, transparent);
        }
        .client-track {
            display: flex;
            gap: 4rem;
            width: max-content;
            animation: scroll 20s linear infinite;
            padding: 1rem 0;
        }
        .client-logo-item {
            white-space: nowrap;
            opacity: 0.6;
            transition: opacity 0.3s;
            font-weight: 700;
            font-size: 1.5rem;
            color: var(--text-muted);
        }
        .client-logo-item:hover { opacity: 1; color: var(--text-main); cursor: default; }
        
        @keyframes scroll {
            to { transform: translateX(-50%); }
        }
    </style>
</head>
<body>
    <div class="animated-bg"></div>
"""

SHARED_NAV = """
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg fixed-top" id="mainNavbar">
        <div class="container">
            <a class="navbar-brand text-main" href="/" style="color: var(--text-main) !important;"><h3 class="hero-title">SanNeo
            </h3></a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto align-items-center">
                    <li class="nav-item"><a class="nav-link" href="/">Home</a></li>
                    <!-- IMPROVEMENT: Added Portfolio Link -->
                    <li class="nav-item"><a class="nav-link" href="/portfolio">Portfolio</a></li>
                    <li class="nav-item"><a class="nav-link" href="/#services">Services</a></li>
                    <li class="nav-item"><a class="nav-link" href="/#testimonials">Clients</a></li>
                    <li class="nav-item"><a class="nav-link" href="/#about">About</a></li>
                    <li class="nav-item"><a class="nav-link" href="/#contact">Contact</a></li>
                </ul>
            </div>
        </div>
    </nav>
"""

HOME_BODY_START = """
    <!-- Home Section -->
    <section id="home" class="hero-section container">
        <div class="row align-items-center">
            <div class="col-lg-7">
                <p class="small fw-bold mb-3 text-uppercase" style="color: var(--accent-primary); letter-spacing: 2px;">Hello, I'm Vish</p>
                <h1 class="kinetic-text">Designer, Full Stack Developer<br>& Creator</h1>
                <p class="lead text-muted mt-4 mb-5" style="max-width: 650px;">
                    I build scalable, secure, and high-performance web applications using Python, Django, Flask, FastAPI and modern frontend technologies. I specialize in end-to-end full-stack development—from backend architecture to responsive user interfaces.
                </p>
                <div class="d-flex flex-column flex-sm-row gap-3">
                    <a href="#contact" class="btn-premium">Hire Me</a>
                    <a href="#work" class="btn-outline-custom">View Work</a>
                </div>
            </div>
            <!-- Improved Hero Visual Area -->
            <div class="col-lg-5 d-none d-lg-block">
                <div class="hero-visual-container">
                    <div class="glow-sphere" style="top: 10%; right: 10%;"></div>
                    <div class="hero-decorative-card card-1 d-flex align-items-center gap-3">
                        <div class="p-2 rounded-circle bg-success-subtle text-success"><i data-lucide="trending-up" style="width:16px;"></i></div>
                        <div>
                            <p class="mb-0 small fw-bold">Conversion Rate</p>
                            <p class="mb-0 smaller text-muted">+14% last month</p>
                        </div>
                    </div>
                    <div class="hero-decorative-card card-2 d-flex align-items-center gap-3">
                        <div class="p-2 rounded-circle bg-primary-subtle text-primary"><i data-lucide="zap" style="width:16px;"></i></div>
                        <div>
                            <p class="mb-0 small fw-bold">Performance</p>
                            <p class="mb-0 smaller text-muted">99/100 Lighthouse</p>
                        </div>
                    </div>
                    <img src="/static/images/hero_img.png" alt="Dashboard" class="hero-main-img" alt="Dashboard" class="hero-main-img">
                </div>
            </div>
        </div>
    </section>

    <!-- Work Section -->
    <section id="work" class="container py-5 reveal">
        <div class="text-center mb-5">
            <p class="small fw-bold text-uppercase" style="color: var(--accent-primary); letter-spacing: 1px;">Work</p>
            <h2 class="display-5 fw-bold">Featured Projects</h2>
        </div>
        
        <div class="row g-4" id="projectGrid">
            <!-- IMPROVEMENT: Loop limited to first 3 projects only -->
            {% for project in PROJECTS[:3] %}
            <div class="col-md-6 col-lg-4 project-item" data-category="{{ project.category }}">
                <div class="project-card">
                    <div class="overflow-hidden">
                        <img src="{{ project.image }}" class="project-img" alt="{{ project.title }}">
                    </div>
                    <div class="p-4 flex-grow-1 d-flex flex-column">
                        <span class="small text-uppercase fw-bold" style="color: var(--accent-secondary); letter-spacing: 1px; opacity: 0.7;">{{ project.category }}</span>
                        <h3 class="h4 mt-2 mb-3">{{ project.title }}</h3>
                        <p class="text-muted small mb-4">{{ project.description }}</p>
                        
                        <div class="mt-auto d-flex flex-column gap-3">
                            <div class="d-flex gap-2">
                                {% for t in project.tech[:2] %}
                                <span class="badge bg-light border border-secondary text-muted">{{ t }}</span>
                                {% endfor %}
                            </div>
                            <!-- IMPROVEMENT: Enhanced Live Demo Button -->
                            <div class="d-flex justify-content-between align-items-center mt-2">
                                <button onclick="openLiveDemo('{{ project.title }}', '{{ project.description }}', '{{ project.live_url }}', '{{ project.github_url }}', {{ project.tech }})" 
                                    class="btn-live-demo">
                                    <i data-lucide="play-circle" style="width: 18px;"></i> Live Demo
                                </button>
                                <button class="btn btn-link text-decoration-none p-0 fw-bold small" 
                                        style="color: var(--accent-primary)"
                                        data-bs-toggle="modal" 
                                        data-bs-target="#modal-{{ project.id }}">
                                    Details <i data-lucide="arrow-right" class="d-inline-block ms-1" style="width: 14px;"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <!-- IMPROVEMENT: View All Projects Button -->
        <div class="text-center mt-5">
            <a href="/portfolio" class="btn-outline-custom">View All Projects</a>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services" class="container py-5 reveal">
        <div class="text-center mb-5">
            <p class="small fw-bold text-uppercase" style="color: var(--accent-primary); letter-spacing: 1px;">Offerings</p>
            <h2 class="display-5 fw-bold">What I Do</h2>
        </div>
        <div class="row g-4">
            <div class="col-md-4">
                <div class="service-card">
                    <i data-lucide="monitor" class="mb-4" style="color: var(--accent-primary); width: 40px; height: 40px;"></i>
                    <h3 class="h4">Full-Stack Web Development</h3>
                    <p class="text-muted small flex-grow-1">End-to-end web application development including backend, frontend, database, and deployment.</p>
                    <p class="price-range">Starting at ₹8,000</p>
                    <a href="#contact" class="btn btn-outline-custom w-100">Get a Quote</a>
                </div>
            </div>
            <div class="col-md-4">
                <div class="service-card">
                    <i data-lucide="palette" class="mb-4" style="color: var(--accent-primary); width: 40px; height: 40px;"></i>
                    <h3 class="h4">UI/UX Design</h3>
                    <p class="text-muted small flex-grow-1">Creating world-class user interfaces and intuitive user experiences that convert visitors into loyal customers.</p>
                    <p class="price-range">Starting at ₹2,000</p>
                    <a href="#contact" class="btn btn-outline-custom w-100">Enquire Now</a>
                </div>
            </div>
            <div class="col-md-4">
                <div class="service-card">
                    <i data-lucide="edit-3" class="mb-4" style="color: var(--accent-primary); width: 40px; height: 40px;"></i>
                    <h3 class="h4">Backend & API Development</h3>
                    <p class="text-muted small flex-grow-1">Secure REST APIs, authentication, database design, and performance optimization.</p>
                    <p class="price-range">Starting at ₹4,000</p>
                    <a href="#contact" class="btn btn-outline-custom w-100">Work With Me</a>
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials / Clients -->
    <section id="testimonials" class="container py-5 reveal">
        <div class="text-center mb-5">
            <p class="small fw-bold text-uppercase" style="color: var(--accent-primary); letter-spacing: 1px;">Social Proof</p>
            <h2 class="display-5 fw-bold">Trusted by Innovators</h2>
        </div>
        
        <!-- IMPROVEMENT: Continuous Client Scroller -->
        <div class="client-scroller mb-5">
            <div class="client-track">
                <!-- Duplicate list for seamless infinite scroll -->
                {% for client in CLIENTS %}
                <div class="client-logo-item">{{ client }}</div>
                {% endfor %}
                {% for client in CLIENTS %}
                <div class="client-logo-item">{{ client }}</div>
                {% endfor %}
            </div>
        </div>

        <div class="row g-4">
            {% for testimonial in TESTIMONIALS %}
            <div class="col-md-6">
                <div class="testimonial-card h-100">
                    <i data-lucide="quote" class="mb-3" style="color: var(--accent-primary)"></i>
                    <p class="lead mb-4">"{{ testimonial.quote }}"</p>
                    <div class="d-flex align-items-center">
                        <img src="{{ testimonial.image }}" class="rounded-circle me-3 shadow-sm" width="50" height="50" alt="">
                        <div>
                            <h6 class="mb-0 fw-bold">{{ testimonial.author }}</h6>
                            <p class="small text-muted mb-0">{{ testimonial.role }}</p>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <!-- About Section (Unchanged) -->
    <section id="about" class="container py-5 reveal">
        <div class="row align-items-center mb-5">
            <div class="col-lg-4 mb-4 mb-lg-0">
                <div class="position-relative">
                    <img src="/static/images/profile_pic.jpg" 
                         class="img-fluid rounded-4 shadow-lg border" alt="Vish Profile">
                </div>
            </div>
            <div class="col-lg-8 ps-lg-5">
                <p class="small fw-bold text-uppercase" style="color: var(--accent-primary); letter-spacing: 1px;">About Me</p>
                <h2 class="display-6 fw-bold mb-4">Turning Business Requirements into Production-Ready Web Solutions</h2>
                <p class="lead text-muted mb-4">
                    I am a Full-Stack Developer with strong experience across Python, JavaScript and Bootstrap ecosystems. I build complete, production-ready web applications using Django, Flask, FastAPI, and the Generative AI.
                   My focus is on clean architecture, secure APIs, optimized databases, and responsive user interfaces that deliver real business value.
                </p>
                <div class="row g-4">
                    <div class="col-sm-6">
                        <h5 class="fw-bold"><i data-lucide="zap" class="me-2" style="width: 18px; color: var(--accent-primary);"></i>My Approach</h5>
                        <p class="text-muted small">I believe in "Performance First" design—ensuring speed, accessibility, and clean architecture are never sacrificed for aesthetics.</p>
                    </div>
                    <div class="col-sm-6">
                        <h5 class="fw-bold"><i data-lucide="refresh-cw" class="me-2" style="width: 18px; color: var(--accent-primary);"></i>My Workflow</h5>
                        <p class="text-muted small">Requirement Analysis
→ System & API Design
→ Database Modeling
→ Development
→ Testing & Optimization
→ Deployment & Support</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="row mt-5 pt-5 border-top border-light">
            <div class="col-lg-5">
                <p class="small fw-bold text-uppercase" style="color: var(--accent-primary); letter-spacing: 1px;">Experience</p>
                <h2 class="display-6 fw-bold mb-5">Professional Journey</h2>
            </div>
            <div class="col-lg-7">
                <div class="timeline">
                    <div class="timeline-item">
                        <h4 class="h5 fw-bold mb-1">Full-Stack Developer
                          Freelance & Project-Based</h4>
                        <p class="mb-1 fw-bold" style="color: var(--accent-primary)">Stripe • 2024 - Present</p>
                        <p class="text-muted small">• Designed and developed full-stack web applications using Python, Django, Flask, FastAPI and Gen-AI<br>• Built secure REST APIs and backend architectures<br>• Worked with MySQL and MongoDB databases <br>• Developed responsive user interfaces using HTML, CSS, JavaScript, and Bootstrap <br>• Delivered production-ready solutions for real-world use cases</p>
                    </div>
                    <div class="timeline-item">
                        <h4 class="h5 fw-bold mb-1">Backend Developer (Projects & Internships)</h4>
                        <p class="mb-1 fw-bold" style="color: var(--accent-primary)">Projects & Internships • 2023 - 2024</p>
                        <p class="text-muted small">• Developed backend systems and APIs using Flask and Django <br>• Implemented authentication, authorization, and data validation <br>• Designed relational and NoSQL database schemas <br>• Integrated frontend components with backend services</p>
                    </div>
                    <div class="timeline-item">
                        <h4 class="h5 fw-bold mb-1">Web Developer (Learning & Practice Phase)</h4>
                        <p class="mb-1 fw-bold" style="color: var(--accent-primary)">Self-Directed Projects • 2022 - 2023</p>
                        <p class="text-muted small">• Built multiple CRUD-based applications and dashboards <br>• Practiced full-stack development using Python, PHP, and JavaScript <br>• Worked on real-world problem statements and system design</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Skills Section (Unchanged) -->
    <section class="container py-5 reveal">
        <div class="row mb-5">
            <div class="col-lg-6">
                <p class="small fw-bold text-uppercase" style="color: var(--accent-primary); letter-spacing: 1px;">Expertise</p>
                <h2 class="display-5 fw-bold">Tech Stack</h2>
            </div>
        </div>
        <div class="row g-3">
            <div class="col-6 col-md-3">
                <div class="skill-item">
                    <i data-lucide="layers" class="mb-3" style="color: var(--accent-primary)"></i>
                    <h6 class="fw-bold mb-0">Python | JavaScript</h6>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="skill-item">
                    <i data-lucide="code" class="mb-3" style="color: var(--accent-secondary)"></i>
                    <h6 class="fw-bold mb-0">Django | Flask | FastAPI</h6>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="skill-item">
                    <i data-lucide="database" class="mb-3 text-warning"></i>
                    <h6 class="fw-bold mb-0">MySQL | MongoDB | PostgreSQL</h6>
                </div>
            </div>
            <div class="col-6 col-md-3">
                <div class="skill-item">
                    <i data-lucide="framer" class="mb-3 text-danger"></i>
                    <h6 class="fw-bold mb-0">HTML | CSS | JS | Bootstrap</h6>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section (Unchanged) -->
    <section id="contact" class="container py-5 reveal">
        <div class="project-card p-4 p-md-5 border-0" style="border-radius: 3rem;">
            <div class="row">
                <div class="col-lg-6 mb-5 mb-lg-0">
                    <h2 class="display-5 fw-bold mb-4">Let's work together</h2>
                    <p class="text-muted mb-5">Have a project in mind? Reach out today and let's turn your vision into a reality.</p>
                    
                    <div class="d-flex align-items-center mb-4">
                        <div class="me-3 p-3 bg-light rounded-circle border"><i data-lucide="mail" style="width: 20px;"></i></div>
                        <div>
                            <p class="mb-0 text-muted small">Email me</p>
                            <p class="mb-0 fw-bold">bindvish811@gmail.com</p>
                        </div>
                    </div>
                    <div class="d-flex align-items-center mb-4">
                        <div class="me-3 p-3 bg-light rounded-circle border"><i data-lucide="phone" style="width: 20px;"></i></div>
                        <div>
                            <p class="mb-0 text-muted small">Call or Text</p>
                            <p class="mb-0 fw-bold">+91 1234567890</p>
                        </div>
                    </div>

                    <div class="mt-5">
                        <p class="text-muted mb-3 small fw-bold text-uppercase">Connect</p>
                        <div class="d-flex gap-3">
                            <a href="http://www.linkedin.com/in/vishal-bind-63473123a" class="btn btn-outline-custom rounded-circle p-2" style="width:45px; height:45px; display:flex; align-items:center; justify-content:center;"><i data-lucide="linkedin" style="width:18px;"></i></a>
                            <a href="https://github.com/vishalbind-IT" class="btn btn-outline-custom rounded-circle p-2" style="width:45px; height:45px; display:flex; align-items:center; justify-content:center;"><i data-lucide="github" style="width:18px;"></i></a>
                            <a href="https://www.instagram.com/" class="btn btn-outline-custom rounded-circle p-2" style="width:45px; height:45px; display:flex; align-items:center; justify-content:center;"><i data-lucide="instagram" style="width:18px;"></i></a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-6">
                    <form action="/contact" method="POST" id="contactForm">
                        <div class="row g-3">
                            <div class="col-md-6">
                                <input type="text" class="form-control" name="name" placeholder="Name" required>
                            </div>
                            <div class="col-md-6">
                                <input type="email" class="form-control" name="email" placeholder="Email" required>
                            </div>
                            <div class="col-12">
                                <textarea class="form-control" name="message" rows="5" placeholder="Your Message" required></textarea>
                            </div>
                            <div class="col-12">
                                <button type="submit" class="btn-premium w-100 py-3 mt-3">Send Message</button>
                            </div>
                        </div>
                        <div id="formStatus" class="mt-3 text-center small fw-bold"></div>
                    </form>
                </div>
            </div>
        </div>
    </section>
"""

# IMPROVEMENT: New Portfolio Body Section
PORTFOLIO_BODY = """
    <div class="container py-5 mt-5">
        <div class="text-center mb-5 reveal">
            <p class="small fw-bold text-uppercase" style="color: var(--accent-primary); letter-spacing: 1px;">Portfolio</p>
            <h1 class="display-4 fw-bold">All Projects</h1>
            <p class="lead text-muted mx-auto" style="max-width: 600px;">
                A complete collection of my work. Filter by category or view live demos.
            </p>
        </div>

        <!-- Filter Buttons (Restored functionality on Portfolio page) -->
        <div class="filter-wrapper">
            <div class="filter-container">
                <button class="filter-btn active" onclick="filterProjects('all')">All Work</button>
                <button class="filter-btn" onclick="filterProjects('SAAS')">SAAS</button>
                <button class="filter-btn" onclick="filterProjects('Mobile')">Mobile</button>
                <button class="filter-btn" onclick="filterProjects('Web')">Web</button>
            </div>
        </div>

        <div class="row g-4" id="projectGrid">
            {% for project in PROJECTS %}
            <div class="col-md-6 col-lg-4 project-item" data-category="{{ project.category }}">
                <div class="project-card h-100">
                    <div class="overflow-hidden">
                        <img src="{{ project.image }}" class="project-img" alt="{{ project.title }}">
                    </div>
                    <div class="p-4 flex-grow-1 d-flex flex-column">
                        <span class="small text-uppercase fw-bold" style="color: var(--accent-secondary); letter-spacing: 1px; opacity: 0.7;">{{ project.category }}</span>
                        <h3 class="h4 mt-2 mb-3">{{ project.title }}</h3>
                        <p class="text-muted small mb-4">{{ project.description }}</p>
                        
                        <div class="mt-auto d-flex flex-column gap-3">
                            <div class="d-flex gap-2">
                                {% for t in project.tech[:2] %}
                                <span class="badge bg-light border border-secondary text-muted">{{ t }}</span>
                                {% endfor %}
                            </div>
                            <!-- IMPROVEMENT: Enhanced Live Demo Button -->
                            <div class="d-flex justify-content-between align-items-center mt-2">
                                <button onclick="openLiveDemo('{{ project.title }}', '{{ project.description }}', '{{ project.live_url }}', '{{ project.github_url }}', {{ project.tech }})" 
                                    class="btn-live-demo">
                                    <i data-lucide="play-circle" style="width: 18px;"></i> Live Demo
                                </button>
                                <button class="btn btn-link text-decoration-none p-0 fw-bold small" 
                                        style="color: var(--accent-primary)"
                                        data-bs-toggle="modal" 
                                        data-bs-target="#modal-{{ project.id }}">
                                    Details <i data-lucide="arrow-right" class="d-inline-block ms-1" style="width: 14px;"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        
        <div class="text-center mt-5 pt-5">
            <div class="p-5" style="background: var(--card-bg); border-radius: 2rem; border: 1px solid var(--border-light);">
                <h3 class="fw-bold mb-3">Looking for a custom solution?</h3>
                <a href="/#contact" class="btn-premium">Get a Quote</a>
            </div>
        </div>
    </div>
"""

SHARED_FOOTER_AND_SCRIPTS = """
    <!-- Modals Section -->
    <div id="modalsContainer">
        <!-- Original Case Study Modals (Unchanged) -->
        {% for project in PROJECTS %}
        <div class="modal fade" id="modal-{{ project.id }}" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-dialog-centered modal-lg">
                <div class="modal-content border-0 shadow-lg" style="background: var(--bg-body); border-radius: 2rem;">
                    <div class="modal-header border-0 p-4">
                        <h5 class="modal-title fw-bold">{{ project.title }}</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body p-4 p-md-5 pt-0">
                        <div class="row">
                            <div class="col-lg-5 mb-4 mb-lg-0">
                                <img src="{{ project.image }}" class="img-fluid rounded-4 shadow-sm" alt="">
                                <div class="mt-4 d-flex flex-wrap gap-2">
                                    {% for t in project.tech %}
                                    <span class="badge bg-light border border-secondary text-dark">{{ t }}</span>
                                    {% endfor %}
                                </div>
                            </div>
                            <div class="col-lg-7">
                                <div class="mb-4">
                                    <label class="text-uppercase small fw-bold mb-2 d-block" style="color: var(--accent-primary)">The Challenge</label>
                                    <p class="text-muted">{{ project.challenge }}</p>
                                </div>
                                <div class="mb-4">
                                    <label class="text-uppercase small fw-bold mb-2 d-block" style="color: var(--accent-primary)">The Solution</label>
                                    <p class="text-muted">{{ project.solution }}</p>
                                </div>
                                <div class="p-3 rounded-4" style="background: rgba(14, 165, 233, 0.05); border-left: 4px solid var(--accent-secondary)">
                                    <label class="text-uppercase small fw-bold mb-1 d-block" style="color: var(--accent-secondary)">Final Result</label>
                                    <p class="mb-0 fw-bold">{{ project.result }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        {% endfor %}

        <!-- IMPROVEMENT: New Live Demo Modal -->
        <div class="modal fade modal-live-view" id="liveDemoModal" tabindex="-1" aria-hidden="true">
            <div class="modal-dialog modal-xl modal-dialog-centered">
                <div class="modal-content">
                    <div class="modal-header border-bottom-0 pb-0">
                        <h5 class="modal-title fw-bold" id="liveDemoTitle">Project Title</h5>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body p-0 mt-3">
                        <div class="iframe-container">
                            <div id="iframeLoader" class="d-flex align-items-center justify-content-center h-100 bg-light text-muted">
                                Loading Preview...
                            </div>
                            <iframe id="liveDemoFrame" src="" allowfullscreen onload="document.getElementById('iframeLoader').style.display='none'"></iframe>
                            <div id="iframeFallback" class="iframe-fallback" style="display:none;">
                                <div class="p-4">
                                    <i data-lucide="external-link" style="width: 48px; height: 48px; color: var(--accent-primary);" class="mb-3"></i>
                                    <h5>External Preview Required</h5>
                                    <p class="text-muted">This project does not support embedded previews due to security headers.</p>
                                    <a href="#" id="liveDemoFallbackLink" target="_blank" class="btn-premium mt-2">Open in New Tab</a>
                                </div>
                            </div>
                        </div>
                        <div class="p-4 bg-white">
                            <div class="row align-items-center">
                                <div class="col-lg-8">
                                    <h6 class="fw-bold mb-2">Tech Stack</h6>
                                    <div id="liveDemoTech" class="d-flex flex-wrap gap-2 mb-3"></div>
                                    <p id="liveDemoDesc" class="text-muted small mb-0">Description goes here.</p>
                                </div>
                                <div class="col-lg-4 text-lg-end mt-3 mt-lg-0">
                                    <a href="#" id="liveDemoFullBtn" target="_blank" class="btn btn-dark btn-sm rounded-pill px-4 me-2">Full Site <i data-lucide="external-link" style="width:14px;"></i></a>
                                    <a href="#" id="liveDemoGithubBtn" target="_blank" class="btn btn-outline-dark btn-sm rounded-pill px-4">GitHub <i data-lucide="github" style="width:14px;"></i></a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <footer class="container py-5 text-center text-muted small border-top border-light mt-5">
        <p>© 2025 SanNeo | Created by Vish</p>
    </footer>

    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    
    <script>
        // Navbar Scroll Effect (Original)
        const navbar = document.getElementById('mainNavbar');
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // --- Standard UI Logic (Original) ---
        lucide.createIcons();

        function filterProjects(category) {
            const items = document.querySelectorAll('.project-item');
            const btns = document.querySelectorAll('.filter-btn');
            btns.forEach(btn => {
                btn.classList.remove('active');
                if(btn.textContent.toLowerCase().includes(category.toLowerCase())) btn.classList.add('active');
                if(category === 'all' && btn.textContent.toLowerCase().includes('all')) btn.classList.add('active');
            });
            items.forEach(item => {
                const itemCat = item.getAttribute('data-category');
                if (category === 'all' || itemCat === category) {
                    item.style.display = 'block';
                    setTimeout(() => { item.style.opacity = '1'; item.style.transform = 'translateY(0) scale(1)'; }, 10);
                } else {
                    item.style.opacity = '0';
                    item.style.transform = 'translateY(20px) scale(0.95)';
                    setTimeout(() => { item.style.display = 'none'; }, 300);
                }
            });
        }

        // --- Robust Scroll Reveal Fix (Original) ---
        function reveal() {
            var reveals = document.querySelectorAll(".reveal");
            var windowHeight = window.innerHeight;
            reveals.forEach(function(element) {
                var elementTop = element.getBoundingClientRect().top;
                var elementVisible = 80; 
                if (elementTop < windowHeight - elementVisible) {
                    element.classList.add("active");
                }
            });
        }
        window.addEventListener("scroll", reveal);
        window.addEventListener("resize", reveal);
        
        document.addEventListener("DOMContentLoaded", function() {
            setTimeout(reveal, 200); 
            setTimeout(function() {
                document.querySelectorAll(".reveal").forEach(el => {
                    if (!el.classList.contains('active')) {
                        el.classList.add('active');
                    }
                });
            }, 1500);

            // FIX: Manual close logic for modals (Original)
            document.querySelectorAll('[data-bs-dismiss="modal"]').forEach(button => {
                button.addEventListener('click', function() {
                    const modalEl = this.closest('.modal');
                    const modalInstance = bootstrap.Modal.getInstance(modalEl);
                    if (modalInstance) {
                        modalInstance.hide();
                    } else {
                        new bootstrap.Modal(modalEl).hide();
                    }
                });
            });
        });

        // Form Handling (Original)
       
       document.getElementById('contactForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const status = document.getElementById('formStatus');
    status.innerHTML = '<span class="text-info">Sending message...</span>';

    const formData = new FormData(e.target);

    try {
        const response = await fetch('/contact', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (result.success) {
            status.innerHTML = '<span class="text-success">Message sent successfully!</span>';
            e.target.reset();
        } else {
            throw new Error("Failed");
        }
    } catch (err) {
        status.innerHTML = '<span class="text-danger">Oops! Something went wrong.</span>';
    }
});

        // --- IMPROVEMENT: NEW LIVE DEMO LOGIC ---
        function openLiveDemo(title, description, url, github, techArray) {
            document.getElementById('liveDemoTitle').innerText = title;
            document.getElementById('liveDemoDesc').innerText = description;
            
            // Tech Badges
            const techContainer = document.getElementById('liveDemoTech');
            techContainer.innerHTML = '';
            techArray.forEach(t => {
                techContainer.innerHTML += `<span class="badge bg-light border border-secondary text-dark">${t}</span>`;
            });

            // Links
            document.getElementById('liveDemoFullBtn').href = url;
            document.getElementById('liveDemoGithubBtn').href = github;
            document.getElementById('liveDemoFallbackLink').href = url;

            // Iframe Logic
            const iframe = document.getElementById('liveDemoFrame');
            const loader = document.getElementById('iframeLoader');
            const fallback = document.getElementById('iframeFallback');

            loader.style.display = 'flex';
            iframe.style.display = 'block';
            fallback.style.display = 'none';

            // Check for valid URL (Simulated check)
            if(url && url !== '#') {
                iframe.src = url;
            } else {
                iframe.style.display = 'none';
                loader.style.display = 'none';
                fallback.style.display = 'flex';
            }

            const modal = new bootstrap.Modal(document.getElementById('liveDemoModal'));
            modal.show();
        }
    </script>
</body>
</html>
"""

# --- ROUTES --- & ----- Render Templates -----




@app.route('/')
def index():
    # Renders the original Home page layout
    full_html = SHARED_HEAD + SHARED_NAV + HOME_BODY_START + SHARED_FOOTER_AND_SCRIPTS
    return render_template_string(full_html, PROJECTS=PROJECTS, CLIENTS=CLIENTS, TESTIMONIALS=TESTIMONIALS)
  
  

@app.route('/portfolio')
def portfolio():
    # Renders the new Portfolio layout reusing the original styles
    full_html = SHARED_HEAD + SHARED_NAV + PORTFOLIO_BODY + SHARED_FOOTER_AND_SCRIPTS
    return render_template_string(full_html, PROJECTS=PROJECTS)
  
  

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    print(f"New Contact: {name} ({email}) - {message}")
    return jsonify({"success": True})


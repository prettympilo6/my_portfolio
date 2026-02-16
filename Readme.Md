# 🌟 Nompilo's Professional Portfolio

A modern, elegant portfolio website showcasing ICT skills, projects, and professional experience. Built with Flask (Python), HTML, CSS, and JavaScript with a beautiful grey-white light theme.

[![Live Demo](https://img.shields.io/badge/Live-Demo-success?style=for-the-badge)](https://my-portfolio-sigma-self.vercel.app)
[![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-lightgrey?style=for-the-badge&logo=flask)](https://flask.palletsprojects.com/)
[![Vercel](https://img.shields.io/badge/Deployed%20on-Vercel-black?style=for-the-badge&logo=vercel)](https://vercel.com)

---

## 🚀 Live Website

**Portfolio URL:** [https://my-portfolio-ten-tau-67.vercel.app/](https://my-portfolio-ten-tau-67.vercel.app/)


---

## ✨ Features

### 🎨 Design & UI
- ✅ **Professional Grey-White Theme** - Elegant, warm off-white backgrounds
- ✅ **Fully Responsive** - Perfect on desktop, tablet, and mobile
- ✅ **Smooth Animations** - Professional transitions and scroll effects
- ✅ **Modern Typography** - Cormorant Garamond + DM Sans fonts
- ✅ **Mobile-First Design** - Optimized for all screen sizes

### ⚙️ Functionality
- ✅ **Working Contact Form** - Flask-Mail integration with Gmail SMTP
- ✅ **Email Notifications** - Receive contact form submissions via email
- ✅ **Social Media Integration** - LinkedIn, GitHub, Instagram with brand colors
- ✅ **Project Showcases** - Direct links to GitHub repositories
- ✅ **Dynamic Content** - Easy to update via `app.py` data structure
- ✅ **Form Validation** - Client and server-side validation
- ✅ **Smooth Navigation** - Single-page feel with multi-page structure

### 📱 Pages
- 🏠 **Home** - Hero with photo, skills overview, featured projects
- 👤 **About** - Professional summary, skills grid, education
- 💼 **Projects** - Project showcase with GitHub links
- 📧 **Contact** - Professional contact form with social media

---

## 🛠 Technology Stack

### Backend
- **Flask** - Python web framework
- **Flask-Mail** - Email integration
- **Jinja2** - Template engine
- **Gunicorn** - Production server

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Custom styling with variables
- **JavaScript** - Interactive features
- **Font Awesome** - Icon library
- **Google Fonts** - Custom typography

### Deployment
- **Vercel** - Serverless hosting
- **Git/GitHub** - Version control
- **Environment Variables** - Secure configuration

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Development

```bash

# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Visit in browser
http://localhost:5000
```

---

## 📧 Contact Form Configuration

### Gmail SMTP Setup

pp-password'
```The contact form uses Gmail SMTP. Configuration is in `app.py`:

```python
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'prettynompilo6@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-a

### Email Features
- ✅ Real-time form validation
- ✅ Success/error messages
- ✅ HTML email formatting
- ✅ Reply-to functionality
- ✅ Timestamp on submissions


## 🌐 Deployment Guide

### Deploy to Vercel

#### 1. Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/prettympilo6/my_portfolio.git
git push -u origin main
```

#### 2. Deploy on Vercel

1. Visit [vercel.com](https://vercel.com) and sign in
2. Click **"New Project"**
3. **Import** your GitHub repository
4. Vercel auto-detects `vercel.json` configuration
5. Add **Environment Variables**:
   - `MAIL_USERNAME` = `prettynompilo6@gmail.com`
   - `MAIL_PASSWORD` = `your-gmail-app-password`
6. Click **Deploy**
7. Wait 2-3 minutes for deployment
8. Your site is live! 🎉

---

## 📁 Project Structure

```
my_portfolio/
│
├── app.py                      # Flask application + all data
├── requirements.txt            # Python dependencies
├── vercel.json                # Vercel deployment config
├── README.md                  # This file
│
├── templates/                 # HTML templates (Jinja2)
│   ├── base.html             # Base layout (navbar + footer)
│   ├── home.html             # Homepage with hero section
│   ├── about.html            # About page
│   ├── projects.html         # Projects showcase
│   └── contact.html          # Contact form
│
└── static/                    # Static assets
    ├── css/                   # Stylesheets
    │   ├── global.css        # Global styles + variables
    │   ├── home.css          # Homepage styles
    │   ├── about.css         # About page styles
    │   ├── projects.css      # Projects page styles
    │   └── contact.css       # Contact form styles
    │
    ├── js/
    │   └── main.js           # Navigation + animations
    │
    └── Nompilo.jpeg          # Profile photo
```

---

## 🔧 Environment Variables

For production deployment on Vercel:

| Variable | Description | Example |
|----------|-------------|---------|
| `MAIL_USERNAME` | Gmail address for sending emails | `prettynompilo6@gmail.com` |
| `MAIL_PASSWORD` | Gmail app password (not regular password)

**⚠️ Important:**
- Never commit passwords to Git
- Use environment variables in production
- Generate Gmail App Password from Google Account settings

---

## 🎯 Features Breakdown


## 🐛 Troubleshooting

### Contact Form Not Working

**Issue:** Form submits but no email received

**Solutions:**
1. Check spam folder
2. Verify Gmail app password in environment variables
3. Check Vercel logs for errors
4. Test locally first

### Images Not Loading

**Issue:** Profile photo not displaying

**Solutions:**
1. Ensure image is named exactly `Nompilo.jpeg`
2. Place in `static/` folder (not in subdirectories)
3. Check file permissions
4. Clear browser cache (Ctrl+Shift+R)

### Deployment Failures

**Issue:** Vercel deployment fails

**Solutions:**
1. Check `vercel.json` is in root directory
2. Verify `requirements.txt` has all dependencies
3. Review Vercel build logs
4. Ensure Python version compatibility (3.8+)

### Styling Issues

**Issue:** Page looks broken or unstyled

**Solutions:**
1. Verify CSS files are in `static/css/` folder
2. Check file names match exactly in templates
3. Clear browser cache
4. Check browser console for 404 errors

---

## 📱 Responsive Design

### Breakpoints

- **Desktop:** 1100px+
- **Tablet:** 768px - 1100px
- **Mobile:** 480px - 768px
- **Small Mobile:** <480px

### Mobile Features

✅ Photo visible on all screen sizes
✅ Touch-friendly buttons
✅ Optimized font sizes
✅ Stacked navigation
✅ Full-width forms
✅ Smooth scrolling

---

## 🚀 Performance

- ⚡ Fast page loads
- 📱 Mobile-optimized
- 🎨 Optimized images
- 💨 Minimal JavaScript
- 🔄 Smooth animations
- 📊 SEO-friendly URLs

---

## 📞 Support & Contact

**Portfolio Owner:** Nompilo  
**Email:** prettynompilo6@gmail.com  
**GitHub:** [@prettympilo6](https://github.com/prettympilo6)  
**Live Site:** [https://my-portfolio-sigma-self.vercel.app](https://my-portfolio-sigma-self.vercel.app)

---

## ✅ Pre-Launch Checklist

Before going live, verify:

- [ ] Updated all personal information in `app.py`
- [ ] Added LinkedIn profile URL
- [ ] Added GitHub username
- [ ] Added Instagram handle
- [ ] Updated project GitHub repository links
- [ ] Added professional photo (`Nompilo.jpeg`)
- [ ] Tested contact form locally
- [ ] Pushed all changes to GitHub
- [ ] Set environment variables on Vercel
- [ ] Deployed successfully to Vercel
- [ ] Tested live website (all pages)
- [ ] Verified contact form works on live site
- [ ] Tested all social media links
- [ ] Checked mobile responsiveness
- [ ] Verified GitHub project links work

---

## 📄 License

This portfolio is for personal use. Feel free to use as inspiration for your own portfolio.

---

## 🎉 Acknowledgments

**Built with:** Flask, Python, HTML, CSS, JavaScript  
**Hosted on:** Vercel  
**Icons:** Font Awesome  
**Fonts:** Google Fonts (Cormorant Garamond, DM Sans, Playfair Display)  
**Design:** Custom professional grey-white theme

---

## 🔄 Version History

### v1.0.0 - February 2025
- ✅ Initial release
- ✅ Full responsive design
- ✅ Working contact form
- ✅ Social media integration
- ✅ GitHub project links
- ✅ Mobile-optimized photo display
- ✅ Professional grey-white theme
- ✅ Deployed on Vercel

---

**⭐ If you like this portfolio, give it a star on GitHub!**

**Made with ❤️ by Nompilo**

*Last Updated: February 2025*
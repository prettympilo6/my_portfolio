/* ===========================
   MAIN.JS — Global JavaScript
   =========================== */

// --- Navbar scroll effect ---
const navbar = document.getElementById('navbar');

function handleNavScroll() {
    if (window.scrollY > 60) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
}

window.addEventListener('scroll', handleNavScroll, { passive: true });
handleNavScroll(); // Run on load

// --- Mobile nav toggle ---
const navToggle = document.getElementById('navToggle');
const navLinks = document.getElementById('navLinks');

if (navToggle && navLinks) {
    navToggle.addEventListener('click', () => {
        const isOpen = navLinks.classList.toggle('open');
        navToggle.innerHTML = isOpen
            ? '<i class="fas fa-times"></i>'
            : '<i class="fas fa-bars"></i>';
        navToggle.setAttribute('aria-expanded', isOpen);
    });

    // Close nav when link is clicked
    navLinks.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('open');
            navToggle.innerHTML = '<i class="fas fa-bars"></i>';
            navToggle.setAttribute('aria-expanded', false);
        });
    });

    // Close on outside click
    document.addEventListener('click', (e) => {
        if (!navbar.contains(e.target)) {
            navLinks.classList.remove('open');
            navToggle.innerHTML = '<i class="fas fa-bars"></i>';
        }
    });
}

// --- Scroll-reveal animation for cards ---
function initScrollReveal() {
    const cards = document.querySelectorAll('.card--animate');
    if (!cards.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const card = entry.target;
                const delay = parseInt(card.dataset.index || 0) * 120;
                setTimeout(() => {
                    card.classList.add('visible');
                }, delay);
                observer.unobserve(card);
            }
        });
    }, {
        threshold: 0.15,
        rootMargin: '0px 0px -40px 0px'
    });

    cards.forEach(card => observer.observe(card));
}

// --- Stagger-animate any element with [data-reveal] ---
function initRevealElements() {
    const elements = document.querySelectorAll('[data-reveal]');
    if (!elements.length) return;

    const observer = new IntersectionObserver((entries) => {
        entries.forEach((entry, i) => {
            if (entry.isIntersecting) {
                const el = entry.target;
                const delay = parseInt(el.dataset.revealDelay || i * 100);
                setTimeout(() => {
                    el.style.opacity = '1';
                    el.style.transform = 'translateY(0)';
                }, delay);
                observer.unobserve(el);
            }
        });
    }, { threshold: 0.1 });

    elements.forEach(el => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(20px)';
        el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(el);
    });
}

// --- Smooth page transition ---
function initPageTransitions() {
    document.querySelectorAll('a[href]').forEach(link => {
        const href = link.getAttribute('href');
        if (
            href &&
            !href.startsWith('#') &&
            !href.startsWith('mailto:') &&
            !href.startsWith('http') &&
            link.target !== '_blank'
        ) {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                document.body.style.opacity = '0';
                document.body.style.transition = 'opacity 0.25s ease';
                setTimeout(() => {
                    window.location.href = href;
                }, 250);
            });
        }
    });
}

// Fade in on page load
function initPageLoad() {
    document.body.style.opacity = '0';
    document.body.style.transition = 'opacity 0.4s ease';
    requestAnimationFrame(() => {
        requestAnimationFrame(() => {
            document.body.style.opacity = '1';
        });
    });
}

// --- Init on DOM ready ---
document.addEventListener('DOMContentLoaded', () => {
    initScrollReveal();
    initRevealElements();
    initPageTransitions();
    initPageLoad();
});
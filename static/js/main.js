// ============================================================================
// NAVIGATION INTERACTIONS
// ============================================================================

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Navigation Toggle
    const navToggle = document.getElementById('navToggle');
    const navMenu = document.getElementById('navMenu');
    
    if (navToggle && navMenu) {
        navToggle.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Animate hamburger icon
            const spans = navToggle.querySelectorAll('span');
            if (navMenu.classList.contains('active')) {
                spans[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
                spans[1].style.opacity = '0';
                spans[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';
            } else {
                spans[0].style.transform = 'none';
                spans[1].style.opacity = '1';
                spans[2].style.transform = 'none';
            }
        });
    }
    
    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    let lastScroll = 0;
    
    window.addEventListener('scroll', function() {
        const currentScroll = window.pageYOffset;
        
        if (currentScroll > 50) {
            navbar.style.background = 'rgba(255, 255, 255, 0.95)';
            navbar.style.boxShadow = '0 4px 20px rgba(59, 130, 246, 0.15)';
        } else {
            navbar.style.background = 'rgba(255, 255, 255, 0.8)';
            navbar.style.boxShadow = '0 8px 32px rgba(59, 130, 246, 0.1)';
        }
        
        lastScroll = currentScroll;
    });
});

// ============================================================================
// SMOOTH SCROLL FOR ANCHOR LINKS
// ============================================================================

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ============================================================================
// INTERSECTION OBSERVER FOR SCROLL ANIMATIONS
// ============================================================================

const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animated');
            // Optional: unobserve after animation
            // observer.unobserve(entry.target);
        }
    });
}, observerOptions);

// Observe all elements with animation classes
document.querySelectorAll('.slide-up, .fade-in').forEach(el => {
    observer.observe(el);
});

// ============================================================================
// FORM INPUT ANIMATIONS
// ============================================================================

document.querySelectorAll('.form-input').forEach(input => {
    // Add floating label effect
    input.addEventListener('focus', function() {
        this.parentElement.classList.add('focused');
    });
    
    input.addEventListener('blur', function() {
        if (!this.value) {
            this.parentElement.classList.remove('focused');
        }
    });
    
    // Add ripple effect on input
    input.addEventListener('click', function(e) {
        const ripple = document.createElement('span');
        ripple.classList.add('ripple-effect');
        ripple.style.left = e.offsetX + 'px';
        ripple.style.top = e.offsetY + 'px';
        this.appendChild(ripple);
        
        setTimeout(() => ripple.remove(), 600);
    });
});

// ============================================================================
// BUTTON HOVER EFFECTS
// ============================================================================

document.querySelectorAll('.submit-btn, .cta-btn').forEach(button => {
    button.addEventListener('mouseenter', function(e) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        this.style.setProperty('--x', x + 'px');
        this.style.setProperty('--y', y + 'px');
    });
});

// ============================================================================
// GLASSMORPHISM CARD TILT EFFECT
// ============================================================================

document.querySelectorAll('.glass-card, .metric-card').forEach(card => {
    card.addEventListener('mousemove', function(e) {
        const rect = this.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        
        const centerX = rect.width / 2;
        const centerY = rect.height / 2;
        
        const rotateX = (y - centerY) / 20;
        const rotateY = (centerX - x) / 20;
        
        this.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-4px)`;
    });
    
    card.addEventListener('mouseleave', function() {
        this.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) translateY(0)';
    });
});

// ============================================================================
// NUMBER COUNTER ANIMATION
// ============================================================================

function animateCounter(element, target, duration = 1000) {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= target) {
            current = target;
            clearInterval(timer);
        }
        element.textContent = current.toFixed(6) + ' ms';
    }, 16);
}

// ============================================================================
// PARTICLE EFFECT ON MOUSE MOVE (Optional Enhancement)
// ============================================================================

let particlesEnabled = false; // Set to true to enable particles

if (particlesEnabled) {
    document.addEventListener('mousemove', function(e) {
        if (Math.random() > 0.95) { // Only create particles 5% of the time
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = e.pageX + 'px';
            particle.style.top = e.pageY + 'px';
            particle.style.width = Math.random() * 5 + 2 + 'px';
            particle.style.height = particle.style.width;
            
            document.body.appendChild(particle);
            
            setTimeout(() => particle.remove(), 1000);
        }
    });
}

// ============================================================================
// UTILITY FUNCTIONS
// ============================================================================

function showLoading() {
    document.getElementById('loadingOverlay').classList.add('active');
}

function hideLoading() {
    document.getElementById('loadingOverlay').classList.remove('active');
}

function showAlert(message, type = 'info') {
    const alert = document.createElement('div');
    alert.className = `alert-box ${type}-alert`;
    alert.innerHTML = `
        <i class="fas fa-info-circle"></i>
        <span>${message}</span>
    `;
    
    document.querySelector('.main-content .container').insertBefore(
        alert,
        document.querySelector('.main-content .container').firstChild
    );
    
    // Auto remove after 5 seconds
    setTimeout(() => {
        alert.style.animation = 'slideUp 0.5s ease reverse';
        setTimeout(() => alert.remove(), 500);
    }, 5000);
}

// ============================================================================
// PERFORMANCE MONITORING (Optional - for development)
// ============================================================================

if (window.performance && window.performance.timing) {
    window.addEventListener('load', function() {
        const perfData = window.performance.timing;
        const pageLoadTime = perfData.loadEventEnd - perfData.navigationStart;
        console.log('Page Load Time:', pageLoadTime + 'ms');
    });
}

// ============================================================================
// CHART.JS GLOBAL CONFIGURATION
// ============================================================================

if (typeof Chart !== 'undefined') {
    Chart.defaults.font.family = "'Plus Jakarta Sans', sans-serif";
    Chart.defaults.color = '#CBD5E1';
    Chart.defaults.animation.duration = 1500;
    Chart.defaults.animation.easing = 'easeOutQuart';
}

// ============================================================================
// KEYBOARD SHORTCUTS (Optional Enhancement)
// ============================================================================

document.addEventListener('keydown', function(e) {
    // Ctrl/Cmd + K: Focus on first input
    if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
        e.preventDefault();
        const firstInput = document.querySelector('.form-input');
        if (firstInput) firstInput.focus();
    }
    
    // ESC: Close mobile menu
    if (e.key === 'Escape') {
        const navMenu = document.getElementById('navMenu');
        if (navMenu && navMenu.classList.contains('active')) {
            navMenu.classList.remove('active');
        }
    }
});

// ============================================================================
// DARK MODE TOGGLE (Optional - Future Enhancement)
// ============================================================================

// Uncomment to enable dark mode toggle
/*
const darkModeToggle = document.createElement('button');
darkModeToggle.innerHTML = '<i class="fas fa-moon"></i>';
darkModeToggle.className = 'dark-mode-toggle';
darkModeToggle.onclick = function() {
    document.body.classList.toggle('light-mode');
    const icon = this.querySelector('i');
    icon.className = document.body.classList.contains('light-mode') 
        ? 'fas fa-sun' 
        : 'fas fa-moon';
};
document.body.appendChild(darkModeToggle);
*/

// ============================================================================
// COPY TO CLIPBOARD FUNCTIONALITY
// ============================================================================

function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(() => {
        showAlert('Disalin ke clipboard!', 'success');
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// ============================================================================
// EXPORT DATA FUNCTIONALITY (Optional)
// ============================================================================

function exportToCSV(tableId, filename = 'data.csv') {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    let csv = [];
    const rows = table.querySelectorAll('tr');
    
    rows.forEach(row => {
        const cols = row.querySelectorAll('td, th');
        const rowData = Array.from(cols).map(col => col.textContent);
        csv.push(rowData.join(','));
    });
    
    const csvContent = csv.join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    window.URL.revokeObjectURL(url);
}

// ============================================================================
// CONSOLE WELCOME MESSAGE
// ============================================================================

console.log('%c🚀 Analisis Kompleksitas Algoritma', 'font-size: 20px; font-weight: bold; color: #3B82F6;');
console.log('%cTugas Besar AKA - Babass & Gathfann © 2025', 'font-size: 12px; color: #94A3B8;');
console.log('%cBuilt with Flask, Chart.js, and lots of ☕', 'font-size: 10px; color: #06B6D4;');

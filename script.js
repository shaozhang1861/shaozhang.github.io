// Mobile menu toggle
const mobileToggle = document.querySelector('.mobile-menu');
const menu = document.querySelector('.menu');
if (mobileToggle && menu) {
  mobileToggle.addEventListener('click', () => {
    menu.classList.toggle('open');
  });
}

// Smooth scroll for internal links
document.querySelectorAll('a[href^="#"]').forEach(link => {
  link.addEventListener('click', e => {
    const targetId = link.getAttribute('href');
    if (targetId && targetId.length > 1) {
      const target = document.querySelector(targetId);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
        menu && menu.classList.remove('open');
      }
    }
  });
});

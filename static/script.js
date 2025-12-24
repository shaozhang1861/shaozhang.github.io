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

// Personal images slider - rotate every 0.8 seconds with click to pause/resume
(function() {
  const sliderContainer = document.querySelector('.image-slider-container');
  const sliderImages = document.querySelectorAll('.slider-image');
  if (sliderImages.length <= 1) return; // No need to rotate if only one image
  
  let currentIndex = 0;
  let isPaused = false;
  let intervalId = null;
  
  function showNextImage() {
    if (isPaused) return;
    
    // Hide current image (no transition)
    sliderImages[currentIndex].classList.remove('active');
    
    // Move to next image
    currentIndex = (currentIndex + 1) % sliderImages.length;
    
    // Show next image (no transition)
    sliderImages[currentIndex].classList.add('active');
  }
  
  function togglePause() {
    isPaused = !isPaused;
    if (isPaused) {
      // Paused - clear interval
      if (intervalId) {
        clearInterval(intervalId);
        intervalId = null;
      }
    } else {
      // Resumed - restart interval
      if (!intervalId) {
        intervalId = setInterval(showNextImage, 800);
      }
    }
  }
  
  // Add click event to container
  if (sliderContainer) {
    sliderContainer.addEventListener('click', togglePause);
  }
  
  // Start rotation every 0.8 seconds
  intervalId = setInterval(showNextImage, 800);
})();

document.addEventListener('DOMContentLoaded', function () {
    console.log("Carousel script loaded!");
  
    // Select all carousel containers
    const carousels = document.querySelectorAll('.grid-text-carousel');
  
    // Initialize each carousel
    carousels.forEach((carousel) => {
      const carouselItems = carousel.querySelectorAll('.grid-carousel-item');
      let currentIndex = 0;
  
      // Function to show the next item
      function showNextItem() {
        // Hide the current item
        carouselItems[currentIndex].classList.remove('active');
  
        // Move to the next item
        currentIndex = (currentIndex + 1) % carouselItems.length;
  
        // Show the next item
        carouselItems[currentIndex].classList.add('active');
      }
  
      // Start the carousel
      setInterval(showNextItem, 3000);
    });
  });
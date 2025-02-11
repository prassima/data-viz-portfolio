document.querySelectorAll('.accordion-header').forEach(header => {
    header.addEventListener('click', () => {
        const clickedItem = header.parentElement;
        const allItems = document.querySelectorAll('.accordion-item');

        // Close all other accordion items and remove bounce effects
        allItems.forEach(item => {
            if (item !== clickedItem) {
                item.querySelector('.accordion-content').classList.remove('open');
                item.querySelector('.arrow').classList.remove('rotate');
                item.querySelector('.accordion-header').classList.remove('open'); // Remove open class from other headers
                item.classList.remove('bounce-neighbor');
            }
        });

        // Toggle the clicked item
        const content = header.nextElementSibling;
        const arrow = header.querySelector('.arrow');
        content.classList.toggle('open');
        header.classList.toggle('open'); // Toggle open class on the header
        arrow.classList.toggle('rotate');

        // Apply bounce effect to neighboring sections
        if (content.classList.contains('open')) {
            allItems.forEach(item => {
                if (item !== clickedItem) {
                    item.classList.add('bounce-neighbor');
                    // Remove the bounce class after the animation ends
                    item.addEventListener('animationend', () => {
                        item.classList.remove('bounce-neighbor');
                    }, { once: true });
                }
            });
        }
    });
});
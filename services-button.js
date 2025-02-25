function toggleServices() {
    const section = document.getElementById('servicesSection');
    const button = document.querySelector('.expand-button');
    
    if(section.classList.contains('expanded')) {
        section.classList.remove('expanded');
        button.textContent = 'Explore my services';
    } else {
        section.classList.add('expanded');
        button.textContent = 'Services';
    }
}
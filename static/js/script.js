document.addEventListener('DOMContentLoaded', function() {
    const backToTopLinks = document.querySelectorAll('.btt-link');

    backToTopLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault(); // Prevents jump 
            window.scrollTo({
                top: 0,
                behavior: 'smooth' // Adds smooth scrolling
            });
        });
    });
});



document.addEventListener('DOMContentLoaded', function() {
    const selector = document.getElementById('sort-selector');

    selector.addEventListener('change', function() {
        const selectedVal = this.value;
        const currentUrl = new URL(window.location);

        if (selectedVal !== "reset") {
            const [sort, direction] = selectedVal.split("_");
            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
        }

        window.location.replace(currentUrl);
    });
});
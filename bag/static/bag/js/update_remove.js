    /**
     *  Updating Item Quantity: Clicking an element with the class `.update-link` will
     *  submit the corresponding quantity update form.
     *  Removing an Item from the Bag: Clicking an element with the class `.remove-item` 
     *  sends a POST request (with CSRF token) to remove that item. If the server 
     *  responds successfully, the page reloads to reflect updated bag contents.
     */
    
    document.addEventListener("DOMContentLoaded", () => {

        // Submit update form
        document.querySelectorAll('.update-link').forEach(link => {
            link.addEventListener('click', () => {
                link.closest('td').querySelector('.update-form').submit();
            });
        });

        // Remove item
        document.querySelectorAll('.remove-item').forEach(link => {
            link.addEventListener('click', () => {
                const itemId = link.id.replace("remove_", "");
                // Get CSRF token from meta tag
                const csrfToken = document.querySelector('meta[name="csrf-token"]').content;


                fetch(`/bag/remove/${itemId}/`, {
                    method: "POST",
                    headers: {
                        "X-CSRFToken": csrfToken
                    }
                }).then(response => {
                    // If removal was successful, reload the page
                    if (response.ok) location.reload();
                });
            });
        });
    });
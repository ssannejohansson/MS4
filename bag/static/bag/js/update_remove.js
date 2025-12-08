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
            link.closest('.bag-item-row').querySelector('.update-form').submit();
        });
    });

    // Remove item
    document.querySelectorAll('.remove-item').forEach(link => {
        link.addEventListener('click', () => {
            const itemId = link.dataset.item_id;
            const csrfToken = document.querySelector('meta[name="csrf-token"]').content;

            fetch(`/bag/remove/${itemId}/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken
                }
            }).then(response => {
                if (response.ok) location.reload();
            });
        });
    });

});

    /**
     * Handles quantity input buttons in the shopping bag.
     * - Prevents values below 1 or above 99 and disables minus/plus buttons at limits.
     * - Updates on page load, manual change, or button click. Elements are matched via data-item_id attribute.
     */
document.addEventListener("DOMContentLoaded", () => {

    function handleEnableDisable(container) {
        const input = container.querySelector('.qty_input');
        const minusButton = container.querySelector('.decrement-qty');
        const plusButton = container.querySelector('.increment-qty');

        const value = parseInt(input.value) || 1;

        minusButton.disabled = value <= 1;
        plusButton.disabled = value >= 99;
    }

    document.querySelectorAll('.bag-item-row, .table .bag-table tr').forEach(container => {
        const input = container.querySelector('.qty_input');
        if (!input) return;

        handleEnableDisable(container);

        input.addEventListener('change', () => handleEnableDisable(container));

        // Plus button
        const plusButton = container.querySelector('.increment-qty');
        plusButton.addEventListener('click', (e) => {
            e.preventDefault();
            input.value = Math.min(99, parseInt(input.value) + 1);
            handleEnableDisable(container);
        });

        // Minus button
        const minusButton = container.querySelector('.decrement-qty');
        minusButton.addEventListener('click', (e) => {
            e.preventDefault();
            input.value = Math.max(1, parseInt(input.value) - 1);
            handleEnableDisable(container);
        });
    });

});

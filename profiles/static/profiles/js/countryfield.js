/**
 * Updates the text color of the country select field.
 */

const countrySelect = document.getElementById('id_default_country');

function updateColor() {
    const value = countrySelect.value;
    countrySelect.style.color = value ? '#232120' : '#81726c';
}

updateColor();
countrySelect.addEventListener('change', updateColor);
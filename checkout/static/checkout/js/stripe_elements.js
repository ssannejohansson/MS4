/**
 * Retrieves the Stripe public key and client secret values that were injected
 * into the template using Django's `json_script` tag. The values are stored in
 * hidden script elements and must be extracted using `.textContent.slice(1, -1)`
 * to remove surrounding quotation marks.
 */
const stripePublicKey = document.getElementById('id_stripe_public_key')
    .textContent.slice(1, -1);

const clientSecret = document.getElementById('id_client_secret')
    .textContent.slice(1, -1);

 /**
 * Initializes the Stripe client using the public key provided by the backend.
 * Creates an instance of Stripe Elements for rendering the card input field.
 */
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

/**
 * Defines custom styling for the Stripe card element, including base text
 * appearance and styling for invalid input states.
 */
const style = {
    base: {
        color: '#F1E9E4',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#b42e02',
        iconColor: '#b42e02'
    }
};

/**
 * Creates and mounts the Stripe card element into the DOM. This securely
 * collects card details and handles all sensitive card data on Stripe’s side
 * rather than within the application.
 */
const card = elements.create('card', { hidePostalCode: true, style: style });
card.mount('#card-element');

/**
 * Registers a real-time validation handler on the card element.
 * 
 * - Displays Stripe-generated validation errors inside the #card-errors div.
 * - Clears the error message when the card element becomes valid again.
 **/
card.addEventListener('change', function (event) {
    const errorDiv = document.getElementById('card-errors');

    if (event.error) {
        const html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        errorDiv.innerHTML = html;  
    } else {
        errorDiv.textContent = '';        
    }
});

/**
NEW DOCSTRING! 
 */
const form = document.getElementById('payment-form');
const submitButton = document.getElementById('submit-button');
const loadingOverlay = document.getElementById('loading-overlay');

form.addEventListener('submit', function (ev) {
    ev.preventDefault();

    // Disable inputs during payment attempt
    card.update({ disabled: true });
    submitButton.disabled = true;

    // Fade out form / fade in loading
    form.classList.add('hidden');
    loadingOverlay.classList.remove('hidden');
    const saveInfoCheckbox = document.getElementById('id-save-info');
    const saveInfo = saveInfoCheckbox ? saveInfoCheckbox.checked : false;
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    const postData = new URLSearchParams();
    postData.append('csrfmiddlewaretoken', csrfToken);
    postData.append('client_secret', clientSecret);
    postData.append('save_info', saveInfo);

    const url = '/checkout/cache_checkout_data/';

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        body: postData.toString()
    })
    .then(function(response) {
        if (!response.ok) {
            throw new Error('Network error saving checkout data');
        }

        // --- Only continue to payment after Django accepts POST ---
        return stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.street_address1.value.trim(),
                        line2: form.street_address2.value.trim(),
                        city: form.town_or_city.value.trim(),
                        country: form.country.value.trim(),
                        state: form.county.value.trim(),
                    }
                }
            },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.street_address1.value.trim(),
                    line2: form.street_address2.value.trim(),
                    city: form.town_or_city.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    state: form.county.value.trim(),
                }
            }
        });
    })
    .then(function(result) {
        const errorDiv = document.getElementById('card-errors');

        if (result.error) {
            // Show Stripe error
            errorDiv.innerHTML = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>
            `;

            // Restore form / hide loader
            form.classList.remove('hidden');
            loadingOverlay.classList.add('hidden');

            card.update({ disabled: false });
            submitButton.disabled = false;

        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    })
    .catch(function() {
        location.reload();
    });

});
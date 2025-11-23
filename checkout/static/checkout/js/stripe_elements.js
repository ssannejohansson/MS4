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
 * Handles the Stripe payment form submission process.
 *
 * - Prevents the default form submit behavior.
 * - Disables the card element and submit button to prevent duplicate submissions.
 * - Sends the payment details to Stripe using confirmCardPayment().
 * - If Stripe returns an error, it displays the error message and re-enables the form.
 * - If the payment succeeds, the form is submitted normally to the server.
 *
 * This function handles both real-time error display and the secure confirmation
 * of card payment intent using the client secret provided by the backend.
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

    stripe.confirmCardPayment(clientSecret, {
        payment_method: { card: card }
    }).then(function (result) {
        const errorDiv = document.getElementById('card-errors');

        if (result.error) {
            errorDiv.innerHTML = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>
            `;

            // Show form again / hide loading
            form.classList.remove('hidden');
            loadingOverlay.classList.add('hidden');

            card.update({ disabled: false });
            submitButton.disabled = false;
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});

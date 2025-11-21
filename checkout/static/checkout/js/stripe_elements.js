const stripePublicKey = document.getElementById('id_stripe_public_key')
    .textContent.slice(1, -1);

const clientSecret = document.getElementById('id_client_secret')
    .textContent.slice(1, -1);

const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

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

const card = elements.create('card', { style: style });
card.mount('#card-element');

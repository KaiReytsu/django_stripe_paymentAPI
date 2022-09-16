var stripe = Stripe('your stripe public key');


function buy(){
    let item_id = document.URL.split('/').slice(-2)[0];
    fetch(`/buy/${item_id}`, {method: 'GET'})
        .then(response => response.json())
            .then(session => stripe.redirectToCheckout({ sessionId: session.sessionid }));
}
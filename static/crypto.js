async function fetchCrypto(crypto) {
    let endpoint = `/api/${crypto}_price`; 
    let output = document.getElementById('crypto-output');
    let cryptoImage = ''; 
    
    // Map cryptocurrency names to their corresponding images
    const cryptoImages = {
        bitcoin: '/static/crypto-images/bitcoin-icon.png',
        ethereum: '/static/crypto-images/ethereum-logo.png',
        solana: '/static/crypto-images/sol-icon.png',
        cardano: '/static/crypto-images/ada-icon.png',
        monero: '/static/crypto-images/monero-icon.png'
    };

    // Assign the correct image based on the crypto name
    cryptoImage = cryptoImages[crypto] || '/static/crypto-images/default-icon.png';

    try {
        // Fetch data from the API
        const response = await fetch(endpoint);
        if (!response.ok) throw new Error('Network response was not ok');
        
        const data = await response.json();
        
        // Handle API success response
        if (data.status === 'success') {
            output.innerHTML = `
                <h2>${crypto.charAt(0).toUpperCase() + crypto.slice(1)} Price</h2>
                <p>Current Price (USD): $${data.current_price_usd}</p>
                <p>Last Saved Price (USD): $${data.last_saved_price_usd || 'N/A'}</p>
                <img src="${cryptoImage}" alt="${crypto} icon" class="crypto-icon">
            `;
        } else {
            // Handle API error response
            output.innerHTML = `
                <p>Error fetching ${crypto} price: ${data.message}</p>
            `;
        }
    } catch (error) {
        // Handle network or other unexpected errors
        output.innerHTML = `
            <p>Error fetching ${crypto} price: ${error.message}</p>
        `;
    }
}

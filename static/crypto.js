async function fetchCrypto(crypto) {
    let endpoint = `/api/${crypto}_price`; 
    let output = document.getElementById('crypto-output');
    let cryptoImage = ''; 
    
    if (crypto === 'bitcoin') {
        cryptoImage = '/static/crypto-images/bitcoin-icon.png';
    } else if (crypto === 'ethereum') {
        cryptoImage = '/static/crypto-images/ethereum-logo.png';
    } else if (crypto === 'solana') {
        cryptoImage = '/static/crypto-images/sol-icon.png';
    } else if (crypto === 'cardano') {
        cryptoImage = '/static/crypto-images/ada-icon.png';
    } else if (crypto === 'monero') {
        cryptoImage = '/static/crypto-images/monero-icon.png';  // Add a Monero icon if available
    }

    try {
        const response = await fetch(endpoint);
        if (!response.ok) throw new Error('Network response was not ok');
        
        const data = await response.json();
        
        
        output.innerHTML = `
            <h2>${crypto.charAt(0).toUpperCase() + crypto.slice(1)} Price</h2>
            <p>Current Price (USD): $${data[`${crypto}_price_usd`]}</p>
            <img src="${cryptoImage}" alt="${crypto} icon" class="crypto-icon">
        `;
    } catch (error) {
        output.innerHTML = `<p>Error fetching ${crypto} price: ${error.message}</p>`;
    }
}

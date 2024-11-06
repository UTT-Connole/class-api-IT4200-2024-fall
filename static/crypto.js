
async function fetchCrypto(crypto) {
    let endpoint = `/api/${crypto}_price`; 
    let output = document.getElementById('crypto-output');
    
    try {
        const response = await fetch(endpoint);
        if (!response.ok) throw new Error('Network response was not ok');
        
        const data = await response.json();
        
        output.innerHTML = `
            <h2>${crypto.charAt(0).toUpperCase() + crypto.slice(1)} Price</h2>
            <p>Current Price (USD): $${data[`${crypto}_price_usd`]}</p>
        `;
    } catch (error) {
        output.innerHTML = `<p>Error fetching ${crypto} price: ${error.message}</p>`;
    }
}

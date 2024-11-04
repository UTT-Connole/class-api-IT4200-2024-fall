function fetchColorHex() {
    const colorName = document.getElementById("colorNameInput").value;
    const resultDiv = document.getElementById("result");
    
    fetch(`/get_color_hex?color=${colorName}`)
        .then(response => response.json())
        .then(data => {
            if (data.hex_code) {
                resultDiv.innerHTML = `The hex code for ${colorName} is <strong>${data.hex_code}</strong>`;
            } else {
                resultDiv.innerHTML = `<span style="color: red;">${data.error}</span>`;
            }
        })
        .catch(error => {
            resultDiv.innerHTML = `<span style="color: red;">Error fetching data. Please try again.</span>`;
            console.error("Error:", error);
        });
}
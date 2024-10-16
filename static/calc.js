function toggleYField() {
    const op = document.getElementById('op').value;
    const yField = document.getElementById('y-field');
    yField.style.display = (op === 'square' || op === 'sqrt' || op === 'binary' || op === 'decimal' || op === 'cube') ? 'none' : 'block';
}

document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();
    const form = event.target;
    const x = form.x.value;
    const y = form.y.value;
    const op = form.op.value;
    const response = await fetch(`/calc?x=${x}&y=${y}&op=${op}`);
    const data = await response.json();
    document.getElementById('result').textContent = data.result || data.error;
});
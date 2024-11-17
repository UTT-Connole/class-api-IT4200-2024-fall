function submitGuess() {
    const userInput = document.getElementById('guessInput').value;
    const userId = 'default_user'; // You can customize this or generate a unique user ID if needed

    fetch(`/guessAnimal?user_id=${userId}&guess=${userInput}`)
        .then(response => response.json())
        .then(data => {
            const feedbackElement = document.getElementById('feedback');
            if (data.error) {
                feedbackElement.textContent = data.error;
            } else if (data.result === "Correct! You guessed the animal!") {
                feedbackElement.textContent = `🎉 ${data.result}`;
            } else if (data.result === "Game Over!") {
                feedbackElement.textContent = `😞 ${data.result} The correct animal was: ${data.correct_animal}`;
            } else {
                feedbackElement.textContent = `${data.result}. Hint: ${data.hint}. Attempts left: ${data.attempts_left}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('feedback').textContent = "An error occurred. Please try again.";
        });
}
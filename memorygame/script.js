let gameBoard = document.getElementById("game-board");
let movesCount = document.getElementById("moves");
let timerDisplay = document.getElementById("timer");
let highScoreDisplay = document.getElementById("high-score");
let timer;
let matchedCards = 0;
let totalMoves = 0;
let flippedCards = [];
let gameDifficulty = 4;
let gameTime = 0;

// Initialize the game
function initializeGame() {
    gameBoard.innerHTML = "";
    matchedCards = 0;
    totalMoves = 0;
    gameTime = 0;
    flippedCards = [];

    movesCount.textContent = totalMoves;
    timerDisplay.textContent = "00:00";

    let cardsArray = generateCardPairs(gameDifficulty);
    shuffleArray(cardsArray);

    // Create the cards
    cardsArray.forEach(card => {
        let cardElement = document.createElement("div");
        cardElement.classList.add("card");
        cardElement.innerHTML = `
            <div class="card-inner">
                <div class="card-front">?</div>
                <div class="card-back">${card}</div>
            </div>
        `;
        cardElement.addEventListener("click", () => flipCard(cardElement));
        gameBoard.appendChild(cardElement);
    });

    startTimer();
}

// Generate an array of card pairs based on difficulty
function generateCardPairs(difficulty) {
    let pairs = [];
    let totalCards = difficulty * difficulty;

    // Use emojis for card pairs
    let emojiArray = ["🐱", "🐶", "🐭", "🐰", "🦁", "🐯", "🐨", "🐸", "🦄", "🐷", "🐻", "🐧", "🦉", "🦄", "🐯"];

    for (let i = 0; i < totalCards / 2; i++) {
        pairs.push(emojiArray[i]);
        pairs.push(emojiArray[i]);
    }

    return pairs;
}

// Shuffle the cards
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // Swap elements
    }
}

// Start the timer
function startTimer() {
    if (timer) {
        clearInterval(timer);
    }

    timer = setInterval(() => {
        gameTime++;
        let minutes = Math.floor(gameTime / 60);
        let seconds = gameTime % 60;
        timerDisplay.textContent = `${padZero(minutes)}:${padZero(seconds)}`;
    }, 1000);
}

// Pad single digit numbers with a leading zero
function padZero(num) {
    return num < 10 ? "0" + num : num;
}

// Flip the card
function flipCard(cardElement) {
    if (flippedCards.length === 2 || cardElement.classList.contains("flipped")) return;

    cardElement.classList.add("flipped");
    flippedCards.push(cardElement);

    if (flippedCards.length === 2) {
        totalMoves++;
        movesCount.textContent = totalMoves;

        let [firstCard, secondCard] = flippedCards;
        let firstCardValue = firstCard.querySelector(".card-back").textContent;
        let secondCardValue = secondCard.querySelector(".card-back").textContent;

        if (firstCardValue === secondCardValue) {
            matchedCards++;
            flippedCards = [];

            if (matchedCards === gameDifficulty * gameDifficulty / 2) {
                clearInterval(timer);
                alert(`You win! Time: ${timerDisplay.textContent} Moves: ${totalMoves}`);
                updateHighScore();
            }
        } else {
            setTimeout(() => {
                firstCard.classList.remove("flipped");
                secondCard.classList.remove("flipped");
                flippedCards = [];
            }, 1000);
        }
    }
}

// Update the high score
function updateHighScore() {
    let currentHighScore = parseInt(highScoreDisplay.textContent);
    if (currentHighScore === 0 || totalMoves < currentHighScore) {
        highScoreDisplay.textContent = totalMoves;
    }
}

// Start the game when the page loads
window.onload = initializeGame;

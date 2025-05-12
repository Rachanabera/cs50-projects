Memory Matching Game
Video Demo: https://youtu.be/kLI8fe4_HmQ
Description:
The Memory Matching Game is a fun and engaging web-based game designed to challenge players' memory and concentration. The objective of the game is simple: flip two cards at a time to match pairs of cards with identical values. The player must try to match all the pairs while keeping track of their moves and time. The game ends when all card pairs are successfully matched, and the player's performance is displayed, showcasing the total moves and the time taken to finish the game.

Gameplay Mechanics:
Grid of Cards: Upon starting the game, the player is presented with a grid of face-down cards. Each card has a corresponding pair with the same value hidden behind it. The game is played by clicking on the cards to flip them over, one at a time.
Flipping Cards: When a card is flipped, it reveals the value on the back. The player then needs to find another card with the same value. If the two flipped cards match, they remain face-up, otherwise, they are flipped back over after a brief moment.
Moves Counter: Every time a card is flipped, it counts as a "move," and the game keeps track of the number of moves taken by the player. This feature adds an element of strategy, as fewer moves lead to a better score.
Timer: The game has a built-in timer that tracks how long it takes the player to match all the pairs. The timer starts as soon as the game begins and stops once all the matches are found.
End of Game: When the game is completed, the player is presented with a summary showing how much time was spent and how many moves it took to finish the game. This feature encourages the player to try again and improve their score by matching all pairs in fewer moves and less time.
High Score Feature:
A key feature of the Memory Matching Game is the high score system. At the end of each game, the number of moves is compared to the best score recorded in the session. If the player matches all the pairs in fewer moves than their previous best, the new score is saved. The high score is visible on the main game screen, motivating players to improve their performance and attempt to beat their record each time they play.

Design and Visuals:
Card Design: The cards are visually appealing, with a simple back and a hidden symbol (emojis in this case). Upon clicking, the cards flip over, revealing the symbol. The matching pairs are randomized and shuffled each time the game starts, providing a new challenge with every playthrough.
Animations: To enhance the user experience, smooth flip animations are applied to the cards as they turn over. This adds a layer of polish and makes the game visually satisfying to play.
Responsive Layout: The game is fully responsive, meaning it adapts well to different screen sizes. Whether playing on a desktop computer, tablet, or mobile phone, the game remains playable with the same experience.
Technologies Used:
HTML: The HTML structure lays the foundation for the game's layout, including the game board, the moves counter, the timer, and the high score display.
CSS: The game’s visual design is created using CSS. The cards, grid, and various UI components are styled with responsive design principles. CSS animations are used for the flipping effect, creating a smooth and enjoyable user experience.
JavaScript: JavaScript handles the game logic, such as managing the moves counter, timer, card flips, and matching logic. The cards are dynamically created and shuffled using JavaScript, and event listeners track user interactions with the cards.
Key Features:
Interactive Gameplay: Players can interact with the game board by flipping cards and trying to match pairs.
Timer and Move Tracker: Players are encouraged to improve their efficiency, with a timer counting down and moves being recorded.
High Score Tracking: A high score system that keeps track of the best performance to encourage players to play again and improve.
Smooth Animations: The card flipping animation adds a layer of visual engagement to the game.
Responsive Design: The game can be played on various devices, including desktops, tablets, and smartphones.
Randomized Pairs: Every time the game is played, the card pairs are shuffled, making each session unique.
Why I Built This Game:
The Memory Matching Game was developed as part of the CS50x final project. It combines essential programming concepts such as DOM manipulation, event handling, time management, and game logic into one fun and interactive application. The project not only challenges the player’s memory but also helped me strengthen my skills in JavaScript, HTML, and CSS.

This project was created to demonstrate the use of logic to create an interactive web game, showcasing the ability to manage timers, animate elements, and track user interactions in a seamless and user-friendly way. Additionally, it allows me to explore concepts like randomization, state tracking, and performance optimization, all of which are important when building more complex web applications.
The Memory Matching Game is a simple yet engaging game where players need to match pairs of cards. The objective is to flip two cards at a time and find matching pairs of cards (represented by emojis). The game tracks the number of moves and the time it takes to finish. Let's break down each file and explain how everything works together.

1. index.html: The Main Game Page
The index.html file is the main webpage where your game is hosted. It contains the structure and layout of the page, defining how the game board and other elements are displayed.

Explanation of Key Sections:
HTML Structure:
The <!DOCTYPE html> declaration specifies that this is an HTML5 document, ensuring that modern features and elements are supported by the browser.
<html lang="en">: This tag defines the language of the page as English, which helps search engines and browsers understand the content.
<head>: This section includes metadata about the page, such as the character encoding (UTF-8), viewport settings (to make the page responsive), the page title (which appears in the browser tab), and a link to the external CSS stylesheet (style.css).
<body>: The main content of the page is within the <body> tag:
<header>: Contains the main title of the game ("Memory Matching Game"). There's also a navigation link that allows users to go to the Project Presentation page (presentation.html), where you can showcase your project in detail.
<div id="game-container">: The container holds the actual game board (#game-board) and an information panel (#info) that shows the current number of moves, the timer, and the high score.
<script src="script.js"></script>: Links the JavaScript file that handles the game logic (explained below). This is included at the end of the <body> section to ensure the DOM elements are loaded before the script runs.
2. style.css: Game Styling
The style.css file is responsible for the visual appearance and layout of the game. It uses CSS Grid to display the cards and ensures that they have proper styling for the user interface.

Explanation of Key Sections:
Game Board Layout:

#game-board: This uses CSS Grid to create a grid of cards. The grid-template-columns: repeat(4, 100px) property creates a 4x4 grid with 100px wide columns. The grid-gap: 10px property adds spacing between the cards.
margin: 20px auto: Centers the grid on the page and adds a 20px margin around it.
Card Styling:

.card: Defines the appearance of each card. It is a square (100x100px) with a background color (#4CAF50) and rounded corners (border-radius: 5px). The cursor: pointer indicates that the cards are clickable.
.card-inner: This element holds both the front and back faces of the card and is styled to allow for a 3D flip effect. The position: absolute ensures that the card’s front and back are layered on top of each other.
.card.flipped .card-inner: This class applies the 3D rotation when the card is flipped. It transforms the .card-inner element to rotate 180 degrees on the Y-axis, flipping the card.
Card Front and Back Styling:

.card-front: This is the front face of the card, which initially displays a question mark (?), indicating that the card is face-down.
.card-back: This is the back face of the card, which contains the emoji (e.g., 🐱, 🐶). The transform: rotateY(180deg) ensures that the card’s back face is initially hidden.
Game Info Section:

#info: This section centers the game stats (moves, time, high score) and adjusts the font size to ensure the information is clear and readable.
3. script.js: Game Logic
The script.js file contains the JavaScript that controls the functionality of the game. It manages the game flow, including initializing the game, flipping the cards, checking for matches, and tracking the timer and score.

Explanation of Key Functions:
Game Initialization (initializeGame):

This function is called when the page loads and sets up the game state.
It clears the game board and resets the counters for matched cards, moves, and game time.
It generates the card pairs and shuffles them randomly using shuffleArray().
For each card pair, it creates a new div element with the class card, and the card faces are created inside it (with the front face showing a ? and the back showing the emoji).
Event listeners are added to each card to handle card flips.
Card Pair Generation (generateCardPairs):

This function generates an array of card pairs based on the game difficulty. It fills the array with emoji pairs (e.g., 🐱, 🐶) that will be shown on the cards. The number of pairs depends on the difficulty level (for example, a 4x4 grid would generate 8 pairs of cards).
Card Shuffling (shuffleArray):

This function randomizes the order of the cards by swapping elements in the card array. It ensures that the card positions are different each time the game is played.
Card Flip (flipCard):

When the player clicks a card, the flipCard() function is called.
If two cards are already flipped, the function prevents any further flips until one pair is matched or turned back over.
The card is visually flipped using the CSS class flipped. The value of the card (the emoji) is revealed on the back.
After flipping two cards, the function compares their values. If they match, the cards remain flipped; otherwise, they are turned back after a brief delay using setTimeout().
Timer (startTimer):

The startTimer() function starts the game timer when the game begins. It increments the time every second and updates the display.
The time is displayed in mm:ss format using padZero() to ensure single-digit minutes and seconds are shown with leading zeros.
Moves Counter:

Each time the player flips a pair of cards, the number of moves (totalMoves) is incremented, and the display is updated.
Match Checking and Game End:

If all card pairs are matched, the game ends and displays an alert congratulating the player.
The updateHighScore() function checks if the current score (number of moves) is better than the previous high score and updates it if necessary.
High Score:

The high score is stored in the high-score span and is updated if the player completes the game with fewer moves than the previous best score.
Game Flow:
Start the Game: The game initializes automatically when the page is loaded. Cards are displayed face-down in a grid, and the moves counter and timer are reset.
Flip Cards: The player clicks on cards to flip them. If two cards match, they remain flipped over; otherwise, they flip back after a brief delay.
Track Progress: The number of moves and the time taken to complete the game are tracked in real-time.
Game Over: Once all pairs are matched, the game congratulates the player and shows the time and number of moves. If this is the best performance, the high score is updated.
Restart: To play again, the player can refresh the page.
Conclusion
This project combines HTML, CSS, and JavaScript to create a simple but engaging Memory Matching Game. The game's logic is cleanly separated into different functions, making it easy to maintain and modify. The user interface is styled to be responsive and visually appealing, ensuring a good user experience. This game is a great way to demonstrate basic web development skills and understanding of DOM manipulation, event handling, and game logic.

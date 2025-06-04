import streamlit as st

st.set_page_config(
    page_title="Awesome Game Hub",
    layout="wide",  # Use 'wide' layout for more space
    initial_sidebar_state="collapsed", # Collapse sidebar by default
    page_icon="🎮"
)

# --- Custom CSS for a modern, game-like look ---
st.markdown("""
<style>
    /* Overall App Styling */
    .stApp {
        background: linear-gradient(to right, #4facfe, #00f2fe); /* Light blue gradient */
        color: #333333; /* Darker text for contrast */
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Header Styling */
    .stApp > header {
        display: none; /* Hide Streamlit header */
    }
    .stApp [data-testid="stHeader"] {
        background-color: rgba(0,0,0,0); /* Make header transparent */
    }

    /* --- HEADER CONTAINER STYLING --- */
    .header-container {
        background-color: rgba(0, 0, 0, 0.2); /* Semi-transparent dark background */
        padding: 2.5rem 1.5rem; /* More padding */
        border-radius: 15px;
        margin-bottom: 3rem; /* More space below header */
        animation: fadeIn 1.5s ease-out; /* Apply fade-in animation */
        border-bottom: 3px solid rgba(255, 255, 255, 0.5); /* Subtle white underline */
        box-shadow: 0 5px 15px rgba(0,0,0,0.3); /* Add a subtle shadow */
        text-align: center; /* Center content within the container */
    }

    /* Main Title inside header container */
    .header-container h1 {
        color: #ffffff; /* White color for main title */
        text-shadow: 3px 3px 6px rgba(0,0,0,0.5); /* Stronger shadow */
        margin-top: 0; /* Remove default top margin from h1 */
        margin-bottom: 1rem; /* Space between title and subtitle */
        font-size: 4.5em; /* Even larger font */
        letter-spacing: 2px; /* Add letter spacing */
        font-weight: 900; /* Bolder font */
        line-height: 1.1; /* Adjust line height */
    }

    /* Subtitle/Description inside header container */
    .header-container p {
        color: #f0f0f0; /* Slightly lighter color for description */
        font-size: 1.4em; /* Larger font for subtitle */
        font-weight: 300; /* Lighter font weight */
        line-height: 1.5;
        margin-bottom: 0; /* Remove default bottom margin from p */
    }
    /* --- END HEADER CONTAINER STYLING --- */


    /* Game Card Styling */
    .game-card {
        background-color: rgba(255, 255, 255, 0.95); /* Slightly transparent white background */
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2); /* Stronger shadow */
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 180px; /* Ensure consistent height for cards */
        text-align: center; /* IMPORTANT: Ensure all text inside the card is centered */
    }

    .game-card:hover {
        transform: translateY(-10px) scale(1.02); /* Lift and slightly enlarge on hover */
        box-shadow: 0 12px 24px rgba(0, 0, 0, 0.3); /* Even stronger shadow on hover */
    }

    /* --- GAME CARD TITLE (H3) ALIGNMENT FIXES --- */
    .game-card h3 {
        color: #2c3e50; /* Dark blue for game titles */
        font-size: 1.8em;
        margin: 0.5rem 0; /* Adjust vertical margin, remove default horizontal */
        padding: 0; /* Remove default padding */
        display: flex; /* Keep flex for emoji alignment */
        align-items: center; /* Center items vertically in the flex line */
        justify-content: center; /* Center items horizontally in the flex line */
        flex-wrap: wrap; /* Allow content to wrap if it's too long */
        line-height: 1.2; /* Tighter line spacing for multiline titles */
        min-height: 2.4em; /* Ensure consistent height for titles even if one line */
        /* text-align is not needed here as flexbox handles centering its children */
    }

    .game-card h3 .emoji {
        font-size: 1.2em; /* Slightly larger emoji */
        margin-right: 8px; /* Slightly reduce margin between emoji and text */
        flex-shrink: 0; /* Prevent emoji from shrinking */
    }
    /* --- END GAME CARD TITLE (H3) ALIGNMENT FIXES --- */

    .game-card p {
        color: #555555; /* Medium gray for descriptions */
        font-size: 1em;
        flex-grow: 1; /* Allow description to take available space */
        margin-bottom: 1rem;
    }

    .game-card .play-button {
        display: inline-block;
        background-color: #007bff; /* Vibrant blue for button */
        color: white;
        padding: 0.8rem 1.5rem;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        transition: background-color 0.3s ease, transform 0.2s ease;
        border: none;
        cursor: pointer;
        font-size: 1.1em;
    }

    .game-card .play-button:hover {
        background-color: #0056b3; /* Darker blue on hover */
        transform: translateY(-2px); /* Slight lift on hover */
    }

    /* Footer styling */
    .footer {
        text-align: center;
        margin-top: 3rem;
        color: #eeeeee;
        font-size: 0.9em;
    }

    /* Animation definition */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
</style>
""", unsafe_allow_html=True)

# --- HEADER CONTENT ---
st.markdown("""
<div class="header-container">
    <h1>🎮 The Ultimate Game Arcade! 🚀</h1>
    <p>Feel like having some fun? Dive into our collection of exciting games!</p>
</div>
""", unsafe_allow_html=True)
# --- END HEADER CONTENT ---


# Data structure for games
game_info = [
    {"name": "2048 Puzzle", "url": "https://2048-puzzle-h9e.streamlit.app/", "emoji": "🔢", "desc": "Slide tiles to merge numbers and reach 2048 in this classic puzzle game!"},
    {"name": "Memory Game", "url": "https://match-cards.streamlit.app/", "emoji": "🧠", "desc": "Test your memory by flipping cards to find matching emoji pairs."},
    {"name": "Candy Crush Mini", "url": "https://candycrush-wtf.streamlit.app/", "emoji": "🍬", "desc": "Match 3 or more sweet candies to score points and clear the board."},
    {"name": "Rock Paper Scissors", "url": "https://rockpaperdk.streamlit.app/", "emoji": "✊", "desc": "Challenge the computer in the classic hand game of Rock, Paper, Scissors."},
    {"name": "Snake Game", "url": "https://snakesgamee.streamlit.app/", "emoji": "🐍", "desc": "Guide your snake to eat food, grow longer, and avoid hitting walls or yourself."},
    {"name": "Space Rocket", "url": "https://space-rocket-snnn.streamlit.app/", "emoji": "🚀", "desc": "Pilot your rocket, dodge alien invaders, and shoot them down in this arcade shooter!"},
    {"name": "Sudoku", "url": "https://sudoku-dvl.streamlit.app/", "emoji": "9️⃣", "desc": "Challenge your logic with the timeless number-placement puzzle, Sudoku."},
    {"name": "Tic-Tac-Toe", "url": "https://tic-tac-toe-ucd.streamlit.app/", "emoji": "❌", "desc": "Play a quick game of X's and O's against a friend or the computer."},
    {"name": "Word Scramble", "url": "https://wordscramble-dvl.streamlit.app/", "emoji": "🔠", "desc": "Unscramble the jumbled letters to guess the correct word before time runs out!"}
]

# Create columns for a grid layout
num_columns = 3 # You can change this to 2, 3, or 4 based on your preference
cols = st.columns(num_columns)

for i, game in enumerate(game_info):
    with cols[i % num_columns]: # Distribute cards across columns
        st.markdown(
            f"""
            <div class="game-card">
                <h3><span class="emoji">{game["emoji"]}</span> {game["name"]}</h3>
                <p>{game["desc"]}</p>
                <a href="{game["url"]}" target="_blank" class="play-button">Play Now!</a>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("<div class='footer'>Created with ❤️ using Streamlit</div>", unsafe_allow_html=True)
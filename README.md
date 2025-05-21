# Dictionary Game

A browser-based game where players are shown a random Wikipedia article title and must guess the first paragraph. Built in Python using Flask.

## How it works

- The game fetches a random Wikipedia article.
- Players see the article title and try to write the article's first paragraph.
- On submission, the game compares the player's answer to the actual paragraph and gives feedback.

## Getting Started

### Prerequisites

- Python 3.8+
- pip

### Setup

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://127.0.0.1:5000/` in your browser.

## License

This project is licensed under the GPLv3 - see the LICENSE file for details.
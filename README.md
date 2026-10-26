# 🤖 Rule-Based Chatbot in Python (AlphaBot)

A simple, robust, and extensible **Rule-Based Chatbot** built purely in Python using pattern matching, regular expressions (`re`), and dynamic intent handlers.

---

## 📌 What is a Rule-Based Chatbot?

A **Rule-Based Chatbot** operates on predefined rules, patterns, and logic maps:
1. **Input Parsing & Cleaning**: Strips whitespace and normalizes text.
2. **Pattern Matching & Intent Recognition**: Uses regular expressions (`re`) with word boundaries (`\b`) to match keywords, questions, or user statements regardless of case.
3. **Entity Extraction**: Extracts variables directly from the input (e.g., user's name or mathematical numbers/operators).
4. **Dynamic Handling & Fallbacks**: Routes queries either to randomized response banks or dynamic calculation methods (e.g., system clock, math computations), with a graceful fallback for unrecognized inputs.

---

## ✨ Features

- **🗣️ Natural Greetings & Pleasantries**: Responds to `"hi"`, `"hello"`, `"good morning"`, `"how are you"`, etc.
- **👤 Name Recognition & Memory**: Remembers the user's name when they say *"My name is Alex"* or *"I am Maria"*.
- **🕒 Real-Time Clock & Date**: Gives the accurate local time (`"what time is it?"`) and current date (`"what is today's date?"`).
- **🧮 Math Calculator**: Evaluates arithmetic expressions safely without `eval()`, supporting `+`, `-`, `*`, `/`, `%`, `^` (e.g. *"calculate 25 * 4"*, *"what is 100 / 5"*).
- **😄 Humor & Trivia**:
  - Programming and general jokes (*"tell me a joke"*)
  - Educational fun facts (*"tell me a fun fact"*)
- **🎲 Interactive Mini-Utilities**:
  - Coin toss: `"flip a coin"` (Heads / Tails)
  - Dice roll: `"roll a die"` (1 to 6)
- **❓ Comprehensive Help Menu**: Type `"help"` or `"what can you do"` at any time.
- **👋 Graceful Session Exit**: Type `"bye"`, `"quit"`, or `"exit"`.
- **🛡️ Cross-Platform & Zero Dependencies**: Uses standard Python libraries only. Automatically configures UTF-8 encoding for Windows consoles.

---

## 🚀 How to Run

### Requirements
- Python 3.7+ installed. No `pip install` required!

### Running the Chatbot
Open your terminal or command prompt in this directory and run:

```bash
# On Windows
py chatbot.py
# or
python chatbot.py
```

### Running the Automated Tests
```bash
py test_chatbot.py
```

---

## 💬 Sample Conversation

```text
============================================================
       🤖 Welcome to AlphaBot - Rule-Based Python Chatbot
============================================================
Type 'help' to see what I can do, or 'exit' to quit.
------------------------------------------------------------

You: hello
AlphaBot: Hello there! How can I help you today?

You: my name is Priya
AlphaBot: Nice to meet you, Priya! I'll remember your name for this session.

Priya: what can you do?
AlphaBot: 
Here are some things you can ask me:
  • Say hello: 'Hi', 'Hello', 'Good morning'
  • Introduce yourself: 'My name is Alex'
  • Ask who I am: 'Who are you?'
  • Check the clock: 'What time is it?'
  • Check the calendar: 'What is today's date?'
  • Do quick math: 'Calculate 45 * 12' or '25 + 75'
  • Ask for a joke: 'Tell me a joke'
  • Learn a fact: 'Tell me a fun fact'
  • Coin & Dice: 'Flip a coin' or 'Roll a die'
  • How are you / Mood: 'How are you?', 'I am happy'
  • Exit: 'bye', 'quit', or 'exit'

Priya: what time is it?
AlphaBot: 🕒 The current time is 09:05:12 PM.

Priya: calculate 15 * 8
AlphaBot: 🧮 Result: 15 * 8 = 120

Priya: tell me a joke
AlphaBot: 😄 Why do programmers prefer dark mode? Because light attracts bugs!

Priya: bye
AlphaBot: Goodbye Priya! Have a wonderful day ahead! 👋
```

---

## 🛠️ How to Add Your Own Rules

Open [chatbot.py](file:///c:/Users/my/OneDrive/Desktop/codealpha2/chatbot.py) and locate the `_initialize_rules` method. Add a new tuple containing a regex pattern and either a list of responses or a method handler:

```python
(
    r"\b(favorite color|best color)\b",
    [
        "My favorite color is terminal green!",
        "I love electric blue and cyber magenta!"
    ]
)
```

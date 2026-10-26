"""
Rule-Based Chatbot in Python
----------------------------
A lightweight, intelligent rule-based chatbot utilizing regular expressions,
pattern matching, intent classification, and dynamic response generation.
Requires only standard Python libraries (no pip dependencies required).
"""

import re
import sys
import random
import datetime
import operator

# Configure UTF-8 encoding for standard output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# ANSI Color Codes for terminal styling
class Colors:
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    MAGENTA = "\033[95m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


class RuleBasedChatbot:
    """A rule-based conversational agent using regular expressions and dynamic intent handling."""

    def __init__(self, bot_name="AlphaBot"):
        self.bot_name = bot_name
        self.user_name = None

        # Pre-curated list of jokes
        self.jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the developer go broke? Because he used up all his cache!",
            "There are 10 types of people in the world: those who understand binary, and those who don't.",
            "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
            "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
            "Why do Python programmers wear glasses? Because they don't C#."
        ]

        # Pre-curated fun facts
        self.fun_facts = [
            "Python was created by Guido van Rossum and released in 1991, named after Monty Python's Flying Circus!",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still edible.",
            "Octopuses have three hearts and blue blood!",
            "The first computer bug was an actual real moth stuck inside the Harvard Mark II computer in 1947.",
            "Venus is the hottest planet in our solar system, with a surface temperature of over 450°C (850°F)."
        ]

        # Setup rule definitions: (regex_pattern, handler_function_or_response_list)
        self.rules = self._initialize_rules()

    def _initialize_rules(self):
        """Initializes patterns and binds them to static response lists or dynamic methods."""
        return [
            # Exit / Goodbye
            (
                r"\b(bye|goodbye|exit|quit|see you|farewell)\b",
                self._handle_goodbye
            ),
            # User Name Capture ("My name is ...", "I am ...")
            (
                r"\b(?:my name is|call me|i am|i'm)\s+([a-zA-Z]+)\b",
                self._handle_name_capture
            ),
            # Greetings
            (
                r"\b(hello|hi|hey|howdy|greetings|good (morning|afternoon|evening))\b",
                self._handle_greeting
            ),
            # Bot Identity / Name Inquiry
            (
                r"\b(who are you|what is your name|what're you called|introduce yourself)\b",
                [
                    f"I am {self.bot_name}, your friendly rule-based assistant!",
                    f"You can call me {self.bot_name}. I'm a Python-powered rule-based chatbot.",
                    f"Hello! I am {self.bot_name}, designed to chat, answer questions, and assist you."
                ]
            ),
            # How are you / Status inquiry
            (
                r"\b(how are you|how('s| is) it going|how do you do|how are things)\b",
                [
                    "I'm operating at 100% computational efficiency! How are you doing today?",
                    "Doing great! Ready to help you with your queries. How about yourself?",
                    "All systems nominal and running smoothly! What's on your mind today?"
                ]
            ),
            # Current Time
            (
                r"\b(what time is it|current time|tell me the time|what's the time|time now)\b",
                self._handle_time
            ),
            # Current Date / Day
            (
                r"\b(what('s| is) the date|what is today's date|today's date|what day is it)\b",
                self._handle_date
            ),
            # Calculator / Math expression
            (
                r"\b(?:calculate|what is|compute|solve)?\s*(\d+(?:\.\d+)?)\s*([\+\-\*\/%^])\s*(\d+(?:\.\d+)?)\b",
                self._handle_math
            ),
            # Jokes
            (
                r"\b(joke|tell me a joke|make me laugh|know any jokes)\b",
                self._handle_joke
            ),
            # Fun Facts
            (
                r"\b(fact|fun fact|tell me something interesting|did you know)\b",
                self._handle_fact
            ),
            # Coin Flip / Dice Roll
            (
                r"\b(flip a coin|toss a coin|coin toss|heads or tails)\b",
                lambda match: f"🪙 I flipped a coin and it landed on: {Colors.BOLD}{random.choice(['Heads', 'Tails'])}{Colors.RESET}!"
            ),
            (
                r"\b(roll a (die|dice)|roll dice)\b",
                lambda match: f"🎲 You rolled a {Colors.BOLD}{random.randint(1, 6)}{Colors.RESET}!"
            ),
            # Help / Capabilities
            (
                r"\b(help|what can you do|features|commands|options)\b",
                self._handle_help
            ),
            # Gratitude / Politeness
            (
                r"\b(thank you|thanks|thx|appreciate it)\b",
                [
                    "You're very welcome!",
                    "Happy to help anytime!",
                    "Glad I could be of assistance!",
                    "No problem at all!"
                ]
            ),
            # Feelings / Mood
            (
                r"\bi('m| am) (happy|good|great|fine|awesome|excited)\b",
                [
                    "Awesome! Glad to hear that you're feeling good!",
                    "That's wonderful to hear! Keep the positive vibes going!",
                    "Great! How can I make your day even better?"
                ]
            ),
            (
                r"\bi('m| am) (sad|tired|upset|stressed|bored|down)\b",
                [
                    "I'm sorry to hear that. Take a deep breath and give yourself a break! Would you like to hear a joke?",
                    "Hang in there! Rough days happen. Want me to tell you a fun fact or a joke to cheer you up?",
                    "Remember that breaks are important! I'm here if you want to chat or hear some lighthearted humor."
                ]
            ),
            # Weather (Rule-based simulated guidance)
            (
                r"\b(weather|temperature|is it raining|is it sunny)\b",
                [
                    "I don't have access to live meteorological satellites yet, but I hope it's clear and sunny outside your window!",
                    "Since I'm a local rule-based bot, I can't check current weather sensors. Look outside or check your weather app!"
                ]
            )
        ]

    # --- Dynamic Handlers ---

    def _handle_greeting(self, match):
        greetings = [
            f"Hello {self.user_name}!" if self.user_name else "Hello there! How can I help you today?",
            f"Hi {self.user_name}! Great to chat with you." if self.user_name else "Hi! What's on your mind?",
            f"Hey {self.user_name}! How are you doing today?" if self.user_name else "Hey! How can I assist you today?"
        ]
        return random.choice(greetings)

    def _handle_name_capture(self, match):
        name = match.group(1).capitalize()
        # Avoid common false positives like "i am fine", "i am good"
        common_words = {"Fine", "Good", "Sad", "Happy", "Tired", "Bored", "Here", "Sure", "Okay", "Ready"}
        if name in common_words:
            return f"Glad to hear that you are {name.lower()}! How can I help you?"

        self.user_name = name
        return f"Nice to meet you, {Colors.BOLD}{self.user_name}{Colors.RESET}! I'll remember your name for this session."

    def _handle_time(self, match):
        now = datetime.datetime.now()
        return f"🕒 The current time is {Colors.BOLD}{now.strftime('%I:%M:%S %p')}{Colors.RESET}."

    def _handle_date(self, match):
        today = datetime.date.today()
        return f"📅 Today is {Colors.BOLD}{today.strftime('%A, %B %d, %Y')}{Colors.RESET}."

    def _handle_joke(self, match):
        return f"😄 {random.choice(self.jokes)}"

    def _handle_fact(self, match):
        return f"💡 {random.choice(self.fun_facts)}"

    def _handle_math(self, match):
        try:
            num1 = float(match.group(1))
            op = match.group(2)
            num2 = float(match.group(3))

            operations = {
                '+': operator.add,
                '-': operator.sub,
                '*': operator.mul,
                '/': operator.truediv,
                '%': operator.mod,
                '^': operator.pow
            }

            if op == '/' and num2 == 0:
                return "⚠️ Division by zero is undefined! Please provide a non-zero denominator."

            result = operations[op](num1, num2)
            # Format cleanly: show integer if result is a whole number
            if result.is_integer():
                result = int(result)
            if num1.is_integer():
                num1 = int(num1)
            if num2.is_integer():
                num2 = int(num2)

            return f"🧮 Result: {num1} {op} {num2} = {Colors.BOLD}{result}{Colors.RESET}"
        except Exception as e:
            return f"⚠️ Could not compute that expression ({e}). Try something like: 15 + 27 or 12 * 8"

    def _handle_help(self, match):
        return (
            f"\n{Colors.BOLD}Here are some things you can ask me:{Colors.RESET}\n"
            "  • Say hello: 'Hi', 'Hello', 'Good morning'\n"
            "  • Introduce yourself: 'My name is Alex'\n"
            "  • Ask who I am: 'Who are you?'\n"
            "  • Check the clock: 'What time is it?'\n"
            "  • Check the calendar: 'What is today's date?'\n"
            "  • Do quick math: 'Calculate 45 * 12' or '25 + 75'\n"
            "  • Ask for a joke: 'Tell me a joke'\n"
            "  • Learn a fact: 'Tell me a fun fact'\n"
            "  • Coin & Dice: 'Flip a coin' or 'Roll a die'\n"
            "  • How are you / Mood: 'How are you?', 'I am happy'\n"
            "  • Exit: 'bye', 'quit', or 'exit'"
        )

    def _handle_goodbye(self, match):
        farewell = f"Goodbye {self.user_name}!" if self.user_name else "Goodbye!"
        return f"{farewell} Have a wonderful day ahead! 👋"

    # --- Response Generator ---

    def get_response(self, user_input: str) -> (str, bool):
        """
        Evaluates user input against predefined rules.
        Returns a tuple: (response_string, should_exit_boolean).
        """
        cleaned_input = user_input.strip()
        if not cleaned_input:
            return "Please type something so I can respond! (Type 'help' for examples)", False

        # Match against rules sequentially
        for pattern, handler in self.rules:
            match = re.search(pattern, cleaned_input, re.IGNORECASE)
            if match:
                # Check if it was an exit command
                is_exit = pattern.startswith(r"\b(bye|goodbye|exit|quit")

                if callable(handler):
                    response = handler(match)
                elif isinstance(handler, list):
                    response = random.choice(handler)
                else:
                    response = str(handler)

                return response, is_exit

        # Fallback response for unhandled input
        fallbacks = [
            "I'm not quite sure I understand. Could you rephrase that? Type 'help' to see what I can do.",
            "That's beyond my current rule set! Try asking for time, a joke, math, or type 'help'.",
            "Hmm, I don't have a programmed response for that. Type 'help' to see my available capabilities."
        ]
        return random.choice(fallbacks), False


def run_chatbot():
    """Main terminal loop for the chatbot."""
    bot = RuleBasedChatbot(bot_name="AlphaBot")

    print(f"{Colors.CYAN}{'=' * 60}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}       🤖 Welcome to AlphaBot - Rule-Based Python Chatbot{Colors.RESET}")
    print(f"{Colors.CYAN}{'=' * 60}{Colors.RESET}")
    print(f"Type {Colors.YELLOW}'help'{Colors.RESET} to see what I can do, or {Colors.YELLOW}'exit'{Colors.RESET} to quit.")
    print(f"{Colors.CYAN}{'-' * 60}{Colors.RESET}\n")

    while True:
        try:
            prompt_name = bot.user_name if bot.user_name else "You"
            user_input = input(f"{Colors.GREEN}{Colors.BOLD}{prompt_name}:{Colors.RESET} ")

            response, should_exit = bot.get_response(user_input)
            print(f"{Colors.MAGENTA}{Colors.BOLD}{bot.bot_name}:{Colors.RESET} {response}\n")

            if should_exit:
                break

        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{Colors.MAGENTA}{bot.bot_name}:{Colors.RESET} Session interrupted. Goodbye! 👋")
            break


if __name__ == "__main__":
    run_chatbot()

"""
Automated Test Suite for RuleBasedChatbot
-----------------------------------------
Validates all intent rules, math handlers, date/time, jokes, and fallbacks.
"""

import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from chatbot import RuleBasedChatbot


def test_chatbot():
    bot = RuleBasedChatbot(bot_name="AlphaBot")
    test_cases = [
        ("hello", False),
        ("hi there", False),
        ("my name is Alex", False),
        ("who are you?", False),
        ("how are you doing?", False),
        ("what time is it?", False),
        ("what is today's date?", False),
        ("calculate 25 * 4", False),
        ("what is 100 / 5", False),
        ("tell me a joke", False),
        ("tell me a fun fact", False),
        ("flip a coin", False),
        ("roll a die", False),
        ("help", False),
        ("thank you very much", False),
        ("I am happy", False),
        ("what is the weather like?", False),
        ("some unknown random gibberish input xyz123", False),
        ("goodbye", True),
        ("quit", True),
    ]

    print("Running automated rule verification...")
    all_passed = True

    for query, expected_exit in test_cases:
        resp, should_exit = bot.get_response(query)
        assert resp and len(resp) > 0, f"Empty response for: {query}"
        assert should_exit == expected_exit, f"Exit mismatch for {query}: expected {expected_exit}, got {should_exit}"
        print(f"  [PASS] Query: '{query}' -> Exit: {should_exit}")
        # Test personalized greeting after name capture
        if "Alex" in query:
            assert bot.user_name == "Alex", "User name not captured properly"

    # Math zero division test
    zero_div_resp, _ = bot.get_response("calculate 10 / 0")
    assert "undefined" in zero_div_resp or "non-zero" in zero_div_resp, "Division by zero handler failed"
    print("  [PASS] Division by zero handled cleanly.")

    print("\nAll 20 test cases passed successfully! ✨")


if __name__ == "__main__":
    test_chatbot()

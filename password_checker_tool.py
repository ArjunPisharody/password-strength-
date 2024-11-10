import re

def password_checker(password):
    rules = [
        (r'.{12,}', "Length is good (12+ characters)."),
        (r'[A-Z]', "Contains uppercase letters."),
        (r'[a-z]', "Contains lowercase letters."),
        (r'[0-9]', "Contains digits."),
        (r'[@$!%*?&#]', "Contains special characters."),
        (r'(?!.*(.)\1{2,})', "No repetitive sequences.")
    ]

    feedback=[msg if re.search(pattern,password) else f"No {msg.lower()}" for pattern,msg in rules]
    score=sum(1 for pattern, _ in rules if re.search(pattern, password))
    strength_levels=['weak','very weak','moderate','strong','very strong']
    strength=strength_levels[min(score, len(strength_levels) - 1)]

    return{
        'strength':strength,
        'score': score,
        'feedback':feedback
    }

password=input("enter a password: ")
result=password_checker(password)
print("\nPassword Strength:", result["strength"])
print("Score:", result["score"])
print("Feedback:")
for tip in result["feedback"]:
    print("-", tip)
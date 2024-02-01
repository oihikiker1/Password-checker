import re
def pass_strength(password):
    score = 0
    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    common_patterns = ["password", "123456", "qwerty", "admin"]
    if password.lower() not in common_patterns:
        score += 1
    return score
def password_recommendations(score):
    if score < 3:
        return "Weak password. Please improve for better security."
    elif score >= 3 and score < 6:
        return "Moderate password. Consider adding more complexity."
    else:
        return "Strong password! Keep it up!"
def main():
    print("Password Strength Evaluator")
    print("===========================")
    password = input("Enter your password: ")
    strength_score = pass_strength(password)
    print("\nPassword Strength Score:", strength_score)
    print("Recommendation:", password_recommendations(strength_score))
if __name__ == "__main__":
    main()
def check_password(password):
    score = 0
    feedback = []

    try:
        if not isinstance(password, str):
            raise ValueError

        if len(password) >= 8:
            score += 2
        else:
            feedback.append("Too short")

        if any(ch.isupper() for ch in password):
            score += 2
        else:
            feedback.append("Add uppercase letter")

        if any(ch.islower() for ch in password):
            score += 2
        else:
            feedback.append("Add lowercase letter")

        if any(ch.isdigit() for ch in password):
            score += 2
        else:
            feedback.append("Add a number")

        if any(not ch.isalnum() for ch in password):
            score += 2
        else:
            feedback.append("Add special character")

        if score <= 4:
            strength = "Weak"
        elif 5 <= score <= 7:
            strength = "Medium"
        else:
            strength = "Strong"

        return strength, score, feedback

    except ValueError:
        return "Invalid", 0, ["Password must be text only"]


while True:
    try:
        password = input("Enter password: ")

        strength, score, feedback = check_password(password)

        print("Strength:", strength)
        print("Score:", score, "/10")

        for f in feedback:
            print("-", f)

        if strength == "Strong":
            break

    except Exception:
        print("Unexpected error")
        break
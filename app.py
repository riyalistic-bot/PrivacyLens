from flask import Flask, render_template, request

app = Flask(__name__)


# -------------------------------
# HOME PAGE
# -------------------------------
@app.route('/')
def home():
    return render_template("index.html")


# -------------------------------
# ASSESSMENT PAGE
# -------------------------------
@app.route('/assessment')
def assessment():
    return render_template("assessment.html")


# -------------------------------
# RESULT PAGE
# -------------------------------
@app.route('/result', methods=['POST'])
def result():

    score = 100

    strengths = []
    weaknesses = []
    recommendations = []

    # -------------------------------
    # Password Reuse
    # -------------------------------
    answer = request.form.get("password_reuse")

    if answer == "always":
        score -= 10
        weaknesses.append("You reuse passwords across multiple accounts.")
        recommendations.append("Use a unique password for every account.")
    elif answer == "sometimes":
        score -= 5
    else:
        strengths.append("You use unique passwords.")

    # -------------------------------
    # Password Manager
    # -------------------------------
    answer = request.form.get("password_manager")

    if answer == "no":
        score -= 10
        weaknesses.append("You don't use a password manager.")
        recommendations.append("Consider using a password manager.")
    elif answer == "some":
        score -= 5
    else:
        strengths.append("You use a password manager.")

    # -------------------------------
    # Password Strength
    # -------------------------------
    answer = request.form.get("password_strength")

    if answer == "weak":
        score -= 10
        weaknesses.append("Your passwords are weak.")
        recommendations.append("Use passwords with at least 12 unique characters.")
    elif answer == "medium":
        score -= 5
    else:
        strengths.append("You use strong passwords.")

    # -------------------------------
    # Two Factor Authentication
    # -------------------------------
    answer = request.form.get("twofa")

    if answer == "none":
        score -= 10
        weaknesses.append("Two-Factor Authentication is disabled.")
        recommendations.append("Enable 2FA on all important accounts.")
    elif answer == "some":
        score -= 5
    else:
        strengths.append("Two-Factor Authentication is enabled.")

    # -------------------------------
    # Recovery Information
    # -------------------------------
    answer = request.form.get("recovery")

    if answer == "never":
        score -= 10
        recommendations.append("Review your recovery email and phone number regularly.")
    elif answer == "rarely":
        score -= 5
    else:
        strengths.append("Recovery information is updated.")

    # -------------------------------
    # Social Media Privacy
    # -------------------------------
    answer = request.form.get("social")

    if answer == "public":
        score -= 10
        weaknesses.append("Your social media profiles are public.")
        recommendations.append("Set your profiles to Private.")
    elif answer == "mixed":
        score -= 5
    else:
        strengths.append("Your social media profiles are private.")

    # -------------------------------
    # Location Sharing
    # -------------------------------
    answer = request.form.get("location")

    if answer == "often":
        score -= 10
        recommendations.append("Avoid sharing your live location publicly.")
    elif answer == "sometimes":
        score -= 5
    else:
        strengths.append("You protect your location privacy.")

    # -------------------------------
    # Privacy Settings
    # -------------------------------
    answer = request.form.get("privacy")

    if answer == "never":
        score -= 10
        recommendations.append("Review your privacy settings every few months.")
    elif answer == "rarely":
        score -= 5
    else:
        strengths.append("You regularly review privacy settings.")

    # -------------------------------
    # Phishing Awareness
    # -------------------------------
    answer = request.form.get("phishing")

    if answer == "click":
        score -= 10
        weaknesses.append("You may click suspicious links.")
        recommendations.append("Always verify unknown emails and messages.")
    elif answer == "careful":
        score -= 5
    else:
        strengths.append("You avoid suspicious links.")

    # -------------------------------
    # Public Wi-Fi
    # -------------------------------
    answer = request.form.get("wifi")

    if answer == "login":
        score -= 10
        recommendations.append("Avoid logging into accounts on public Wi-Fi.")
    elif answer == "careful":
        score -= 5
    else:
        strengths.append("You use public Wi-Fi safely.")

    # -------------------------------
    # Device Security
    # -------------------------------
    answer = request.form.get("device")

    if answer == "none":
        score -= 10
        weaknesses.append("Your device is not protected with a lock.")
        recommendations.append("Use a PIN, password, fingerprint or Face ID.")
    elif answer == "pin":
        score -= 5
    else:
        strengths.append("Your device is protected.")

    # -------------------------------
    # Software Updates
    # -------------------------------
    answer = request.form.get("updates")

    if answer == "never":
        score -= 10
        recommendations.append("Install security updates regularly.")
    elif answer == "later":
        score -= 5
    else:
        strengths.append("You keep your software updated.")

    # -------------------------------
    # Risk Level
    # -------------------------------
    if score >= 85:
        risk = "Low"
        persona = "🛡 Privacy Guardian"
        persona_description = "Excellent! Your online privacy habits are strong."

    elif score >= 65:
        risk = "Medium"
        persona = "🧭 Cautious Explorer"
        persona_description = "You're doing well, but a few improvements can strengthen your privacy."

    else:
        risk = "High"
        persona = "📢 Open Book"
        persona_description = "Your online privacy needs improvement to reduce security risks."

    return render_template(
        "result.html",
        score=score,
        risk=risk,
        persona=persona,
        persona_description=persona_description,
        strengths=strengths,
        weaknesses=weaknesses,
        recommendations=recommendations
    )


# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
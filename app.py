
import streamlit as st

def check_password(password):
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append(" 🔵 Use at least 8 characters.") 
    if any(c.isupper() for c in password):
        score += 1
    else:
        tips.append(" 🔴 Include an uppercase letter.")    
    if any(c.islower() for c in password):
        score += 1
    else:
        tips.append(" ⚫ Include a lowercase letter.")   
    if any(c.isdigit() for c in password):
        score += 1
    else:
        tips.append(" 🟢 Add a number (0-9).")   
    if any(c in "!@#$%^&*" for c in password):
        score += 1
    else:
        tips.append(" 🟤 Use a special character (!@#$%^&*).")

    return score, tips

def main():
    st.set_page_config(page_title=" Password Strength Meter", layout="centered")
    st.title("🔐 Password Strength Meter")

    password = st.text_input("Enter Password 🔑", type="password")

    if password:
        score, tips = check_password(password)

        strength_labels = {
            0: "Very Weak",
            1: "Weak",
            2: "Fair",
            3: "Moderate",
            4: "Good",
            5: "Strong"
        }

        st.markdown(f"*Strength:* {strength_labels[score]}")
        st.progress(score / 5)

        if score == 5:
            st.success(" ✅ Great! Your password is strong and secure.")
        elif 3 <= score < 5:
            st.warning(" ⚠️Your password is okay, but could be improved:")
            for tip in tips:
                st.write(f"- {tip}")
        else:
            st.error(" ❌ Your password is weak. Here's how to improve it:")
            for tip in tips:
                st.write(f"- {tip}")

main()


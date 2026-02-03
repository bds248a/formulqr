import streamlit as st

st.title("🌍 Geography Quiz")

score = 0


st.write("1. What is the capital of Bulgaria?")
q1 = st.text_input("Your answer:")
if q1:
    if q1.lower() == "sofia":
        score += 1
        st.write("Correct")
    else:
        st.write("Wrong")


st.write("2. Which continent is Germany in?")
q2 = st.text_input("Your answer:")
if q2:
    if q2.lower() == "europe":
        score += 1
        st.write("Correct")
    else:
        st.write("Wrong")


st.write("3. What is the largest ocean?")
q3 = st.text_input("Your answer:")
if q3:
    if q3.lower() == "pacific":
        score += 1
        st.write("Correct")
    else:
        st.write("Wrong")


st.write("4. Which desert is the largest in the world?")
q4 = st.text_input("Your answer:")
if q4:
    if q4.lower() == "sahara":
        score += 1
        st.write("Correct")
    else:
        st.write("Wrong")


st.write("5. What is the longest river in the world?")
q5 = st.text_input("Your answer:")
if q5:
    if q5.lower() == "nile":
        score += 1
        st.write("Correct")
    else:
        st.write("Wrong")


st.write("Your score is", score)

if score == 5:
    st.write("Excellent")
else:
    st.write("Try again")


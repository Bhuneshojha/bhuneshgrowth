import streamlit as st

st.set_page_config(page_title= "Growth Mindset App", project_icon="★")
st.title("Growth Mindset App🛠️")

st.header("Ready to grow? 🚀")
st.write("Welcome to the Growth Mindset App! This app is designed to help you develop a growth mindset, which is the belief that you can improve your abilities through hard work and dedication. Research shows that people with a growth mindset are more likely to succeed in school, work, and life. So let's get started!")

st.header("Today's Quote 🌟")
st.write(" “Focus on your actions, not the results.”-Lord Krishna")

st.header("What's your goal for today? 🎯")
user_input = st.text_input("Enter your goal for today:")


if user_input:
    st.success(f"your goal for today is: {user_input} keep up the good work! 👍")
else:
    st.warning("Tell us about your goal to get started!")

st.header("Daily Reflection on your learning 🤔")    
reflection = st.text_area("what did you learn today? write here.")
if reflection:
    st.success(f"✨Great! you learned: {reflection} keep up the good work!")
else:
    st.info("Reflect on your past experiences to grow better! share your hard ships and success stories here.")    


    # Achievements
st.header("Celebrate your achievements 🎉🏆 ")
achievement = st.text_input("share something you recently accomplished!")
if achievement:
    st.success(f"Amazing! you achieved: {achievement} ")
   
else:
    st.info("😊Big or small, every achievement matters! share your success stories here💫")


st.write("- - -")
st.write("🙏 Remember, developing a growth mindset is a journey! stay positive, and never give up! ❤️")
st.write("**💻💡Developed by Bhunesh Kumar ")

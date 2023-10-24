import streamlit as st
from st_pages import Page, show_pages
import base64

# should be

st.set_page_config(
    page_title="Mental Health Prediction",
    page_icon="🎃",
    layout="wide",
    initial_sidebar_state="expanded",
)

# bottom code is for injecting image in side bar

# @st.cache_data
# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


# image = get_img_as_base64("brain2.png")


page_bg_img_link = f"""
<style>
[data-testid="stAppViewContainer"]> .main{{

# background-image: url(https://www.orfonline.org/wp-content/uploads/2022/10/mental-health-wellness-during-covid-19.jpg);
# background-size:cover;
# background-position: left;
# background-repeat:no-repeat;
# background-attachment:local;
background-color: #FFDEE9;
background-image: linear-gradient(0deg, #FFDEE9 0%, #B5FFFC 100%);




}}


[data-testid="stHeader"]{{
background-color: rgba(0,0,0,0)

}}

[data-testid="stToolbar"]{{
right : 2 rem;
}}

[data-testid="stSidebar"] > div:first-child{{


background: linear-gradient(to right bottom,
                 rgba(255,225,225,0.7),
                 rgba(255,225,225,0.3));
}}


</style>
"""
st.markdown(page_bg_img_link, unsafe_allow_html=True)

with st.sidebar:
    st.image("image\Mental-Health-Status.png")
    st.image(
        "https://png.pngtree.com/png-vector/20230728/ourmid/pngtree-ask-clipart-cartoon-character-illustration-student-cartoon-of-young-boy-in-vector-png-image_6797449.png"
    )
show_pages(
    [
        Page(r"app.py", "Home", "🏠"),
        Page(r"Pages/Prediction.py", "Have your Psychopathology test!", "💥"),
        Page(r"Pages/Introduction.py", "Introduction", "🧠"),
        Page(r"Pages/Dashboard.py", "Dashboard", "⌨"),
        Page(r"Pages/About.py", "About Us", "🦾"),
    ]
)


# Display the main page of the app with instructions on how to use it
def main():
    title = st.image("image\Mental-health-status1.png")
    st.markdown(
        '<div style=" font-family: Mali, cursive; font-size:20px;">Mental health includes our emotional, psychological, and social well-being. It affects how we think, feel, and act. It also helps determine how we handle stress, relate to others, and make choices. Mental health is important at every stage of life, from childhood and adolescence through adulthood.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("""""")
    st.markdown(
        '<div style=" font-family: Mali, cursive; font-size:20px;">Over the course of your life, if you experience mental health problems, your thinking, mood, and behavior could be affected. Many factors contribute to mental health problems, we aim to find those factors.</div>',
        unsafe_allow_html=True,
    )
    st.markdown("""""")
    st.markdown("""""")
    st.markdown("""""")

    cols = st.columns([1, 1])
    with st.container():
        with cols[0]:
            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:30px;">How to use this app:</div>',
                unsafe_allow_html=True,
            )
            st.markdown("""""")
            st.markdown("""""")

            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:25px;">👉 To know your Psychopathology condition!</div>',
                unsafe_allow_html=True,
            )
            st.markdown("""""")
            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:18px;">1. Select the Psychopathology Test from the sidebar.</div>',
                unsafe_allow_html=True,
            )
            st.markdown("""""")
            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:18px;">2. Fill and choose all asked question after reading .</div>',
                unsafe_allow_html=True,
            )
            st.markdown("""""")
            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:18px;">3. Attemp all questions of five section and then click on predict button.</div>',
                unsafe_allow_html=True,
            )
            st.markdown("""""")
            st.markdown("""""")
            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:25px;">👉 To see visualization and analysis of our surveyed data!</div>',
                unsafe_allow_html=True,
            )
            st.markdown("""""")
            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:18px;">1. Select the Dashboard page.</div>',
                unsafe_allow_html=True,
            )
            st.markdown("""""")
            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:25px;">👉 To see detailed explanations of our project!</div>',
                unsafe_allow_html=True,
            )
            st.markdown("""""")
            st.markdown(
                '<div style=" font-family: Mali, cursive; font-size:18px;">1. Select the Introduction page.</div>',
                unsafe_allow_html=True,
            )

        with cols[1]:
            st.image(
                "https://png.pngtree.com/png-vector/20230728/ourmid/pngtree-adolescence-clipart-the-character-of-guy-who-is-carrying-a-backpack-vector-png-image_6792587.png",
                width=550,
            )


if __name__ == "__main__":
    main()

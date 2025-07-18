import streamlit as st
from utils import generate_action_plan # Make sure utils.py exists with this function

# --- Page Configuration ---
st.set_page_config(
    page_title="SDG Personalized Action Plan Chatbot",
    page_icon="🌍", # A nice globe icon
    layout="centered", # Can be "wide" for more space
    initial_sidebar_state="collapsed" # Starts collapsed for a cleaner look
)

# --- Header Section ---
st.markdown(
    """
    <div style='text-align: center;'>
        <h1><span style='color:#4CAF50;'>🌱</span> SDG Personalized Action Plan Chatbot</h1>
        <p style='font-size: 1.1em; color: #555;'>
            Get tailored action plans to contribute to the Sustainable Development Goals.
            Just tell us a bit about yourself!
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("---") # A horizontal line for separation

# --- Input Form ---
st.header("Tell Us About Your SDG Focus")

# Using session state to persist inputs across reruns (useful if you add more complex logic later)
if 'goal' not in st.session_state:
    st.session_state.goal = "Climate Action"
if 'lifestyle' not in st.session_state:
    st.session_state.lifestyle = ""
if 'work_area' not in st.session_state:
    st.session_state.work_area = ""
if 'time_available' not in st.session_state:
    st.session_state.time_available = 5 # Default to 5 hours

col1, col2 = st.columns(2)

with col1:
    st.session_state.goal = st.selectbox(
        "Select Your SDG Focus Goal:",
        [
            "Climate Action",
            "Quality Education",
            "No Poverty",
            "Good Health and Well-being",
            "Gender Equality",
            "Clean Water and Sanitation",
            "Affordable and Clean Energy",
            "Sustainable Cities and Communities",
            "Responsible Consumption and Production",
        ],
        key="sdg_goal_selector" # Unique key for the widget
    )

with col2:
    st.session_state.time_available = st.slider(
        "How Many Hours Per Week Can You Dedicate?",
        1, 40, st.session_state.time_available,
        key="time_slider"
    )

st.session_state.lifestyle = st.text_area(
    "Describe Your Lifestyle (e.g., vegetarian, gym-goer, student, working professional, parent, active traveler, etc.):",
    value=st.session_state.lifestyle,
    height=100, # Increased height for better input experience
    placeholder="e.g., I'm a student who enjoys cycling and cooking at home. I'm mindful of my waste but often use public transport.",
    key="lifestyle_input"
)

st.session_state.work_area = st.text_input(
    "Your Work/Study Area/Field of Expertise (e.g., software engineering, healthcare, marketing, retired, etc.):",
    value=st.session_state.work_area,
    placeholder="e.g., healthcare, currently working as a nurse.",
    key="work_area_input"
)

# --- Action Buttons ---
st.write("") # Add some vertical space
col_btn1, col_btn2, col_btn3 = st.columns([1, 1, 2]) # Adjust column ratios for button placement

with col_btn1:
    generate_button = st.button("✨ Generate Plan ✨", use_container_width=True)
with col_btn2:
    clear_button = st.button("Clear Inputs", use_container_width=True)

if clear_button:
    # Reset session state variables to clear inputs
    st.session_state.lifestyle = ""
    st.session_state.work_area = ""
    st.session_state.time_available = 5
    st.session_state.goal = "Climate Action" # Reset to default
    st.experimental_rerun() # Rerun to reflect cleared inputs

# --- Plan Generation Logic ---
if generate_button:
    if not st.session_state.lifestyle or not st.session_state.work_area:
        st.error("Please fill in both *Lifestyle* and *Work/Study Area* to generate your plan.")
    else:
        with st.spinner("Crafting your personalized SDG action plan... This might take a moment!"):
            try:
                # Call your external function
                plan_result = generate_action_plan(
                    st.session_state.goal,
                    st.session_state.lifestyle,
                    st.session_state.work_area,
                    st.session_state.time_available
                )
                st.success("Your personalized action plan is ready! 🎉")

                # Using an expander for better readability of the long text result
                with st.expander("View Your Action Plan", expanded=True):
                    st.markdown(plan_result) # Assuming generate_action_plan returns markdown formatted text

                st.write("---")
                st.info("💡 *Tip:* You can adjust your inputs and generate a new plan!")

            except Exception as e:
                st.error(f"An error occurred during plan generation: {e}")
                st.info("Please try again or refine your inputs.")

st.write("---")
st.caption("Powered by Streamlit and your commitment to a better world! 🌍")

import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()


def generate_action_plan(user_goal, user_lifestyle, work_area, available_time):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    model = genai.GenerativeModel("gemini-2.0-flash")

    prompt = f"""
    I want you to act as an SDG Action Plan Creator.
    SDG Focus: {user_goal}
    User Lifestyle: {user_lifestyle}
    Work/Study Area: {work_area}
    Available Time Per Week: {available_time}

    Please generate a customized, realistic step-by-step action plan with specific tasks for the week.
    """
    response = model.generate_content(prompt)

    return response.text

import streamlit as st
import requests
import os
from dotenv import load_dotenv


load_dotenv()


API_SERVER_URL = os.getenv('API_SERVER_URL')


st.title("Github User Details 🦄")


username = st.text_input("Enter GitHub Username")


if st.button("Fetch Details"):
    if username:

        response = requests.post(f"{API_SERVER_URL}/user-details", json={"username": username})

        if response.status_code == 200:
            user_data = response.json()
            st.write("### User Details")
            st.write(f"**Name:** {user_data.get('name', 'N/A')}")
            st.write(f"**Number of Public Repos:** {user_data.get('public_repos', 'N/A')}")
            st.write(f"**Company:** {user_data.get('company', 'N/A')}")
            st.write(f"**Location:** {user_data.get('location', 'N/A')}")
            st.write(f"**Email:** {user_data.get('email', 'N/A')}")
            st.write(f"**Twitter Username:** {user_data.get('twitter_username', 'N/A')}")
        else:
            st.error("Failed to fetch user details.")
    else:
        st.error("Please enter a GitHub username.")

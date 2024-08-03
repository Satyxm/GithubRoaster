from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv


load_dotenv()

app = Flask(__name__)


GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_API_URL = "https://api.github.com/users/"


def get_github_profile(username):
    headers = {
        'Authorization': f'token {GITHUB_TOKEN}',
    }
    response = requests.get(f"{GITHUB_API_URL}{username}", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None


@app.route('/user-details', methods=['POST'])
def user_details():
    data = request.json
    username = data.get('username')

    if not username:
        return jsonify({'error': 'No username provided'}), 400

    profile = get_github_profile(username)

    if not profile:
        return jsonify({'error': 'User not found'}), 404

    user_info = {
        'name': profile.get('name'),
        'public_repos': profile.get('public_repos'),
        'company': profile.get('company'),
        'location': profile.get('location'),
        'email': profile.get('email'),
        'twitter_username': profile.get('twitter_username')
    }

    return jsonify(user_info)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
from flask_wtf import CSRFProtect
from flask_session import Session
from app_data.modules.chatbot_module import initialize_chatbot, train_chatbot, get_best_match
from app_data.modules.web_module import main_route, home_route, get_response_route, log_interaction

app = Flask(__name__, static_url_path='/app_data/website/', static_folder='app_data/website/')

# Set a secret key for CSRF protection
app.secret_key = 'your_secret_key_here'  # Replace with a strong, random secret key

# Initialize CSRF protection
csrf = CSRFProtect(app)

# Set the session type to filesystem
app.config['SESSION_TYPE'] = 'filesystem'

# Initialize the session
Session(app)

# Initialize and train the chatbot
azerothcore_bot, trainer, coral_data, team_data = initialize_chatbot()

# Route for the home page
@app.route('/')
def main():
    return main_route()

# Route for the AI
@app.route("/app")
def home():
    return home_route()

@app.route("/get_response", methods=["POST"])
@csrf.exempt
def get_response():
    return get_response_route(request, azerothcore_bot, trainer, coral_data, team_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)

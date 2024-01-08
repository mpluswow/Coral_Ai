from flask import render_template, jsonify
from app_data.modules.chatbot_module import get_best_match
from app_data.modules.user_logs import log_interaction

def main_route():
    return render_template('/home/index.html')

def home_route():
    return render_template("/app/index.html")

def get_response_route(request, azerothcore_bot, trainer, coral_data, team_data):
    user_input = request.form.get("user_input")
    responses = get_best_match(user_input, coral_data, team_data)
    response_text = ' '.join(responses)
    log_interaction(user_input, responses)
    return jsonify(response_text)


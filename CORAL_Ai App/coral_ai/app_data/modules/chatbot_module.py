from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from fuzzywuzzy import fuzz
import json
from app_data.modules.user_logs import log_interaction

def initialize_chatbot():
    # Create a ChatBot instance named 'Coral Ai'
    azerothcore_bot = ChatBot('Coral Ai')

    # Create a trainer for the chatbot
    trainer = ListTrainer(azerothcore_bot)

    # Load existing training data for coral reefs from JSON file
    coral_data = train_chatbot(trainer, 'app_data/training_data/coral_reefs_data.json')

    # Load existing training data for the team from JSON file
    team_data = train_chatbot(trainer, 'app_data/training_data/team_data.json')

    return azerothcore_bot, trainer, coral_data, team_data

def train_chatbot(trainer, file_path):
    try:
        with open(file_path, 'r') as data_file:
            data = json.load(data_file)
            # Train the chatbot with the loaded data
            for item in data:
                input_data = item['input']
                output_data = item['output'] if isinstance(item['output'], list) else [item['output']]
                trainer.train([input_data] + output_data)

        return data

    except FileNotFoundError as file_not_found_error:
        print(f"Error: {file_not_found_error}")

    except json.JSONDecodeError as json_error:
        print(f"Error decoding JSON in data file: {json_error}")

def get_best_match(user_input, coral_data, team_data):
    max_similarity = 0
    best_responses = []

    try:
        # Iterate through the data for fuzzy matching
        for pair in coral_data + team_data:
            question = pair['input']
            similarity = fuzz.ratio(user_input.lower(), question.lower())

            if similarity > max_similarity:
                max_similarity = similarity
                responses = pair['output'] if isinstance(pair['output'], list) else [pair['output']]
                best_responses = responses
            elif similarity == max_similarity:
                responses = pair['output'] if isinstance(pair['output'], list) else [pair['output']]
                best_responses.extend(responses)

    except Exception as e:
        # Print an error message if there's an issue with fuzzy matching
        print(f"Error in fuzzy matching: {e}")
        return ["An error occurred in fuzzy matching"]

    return best_responses

def log_interaction(user_input, bot_responses):
    with open('interaction_log.txt', 'a') as log_file:
        log_file.write(f'[Q] {user_input}\n')
        log_file.write(f'[A] {" ".join(bot_responses)}\n')

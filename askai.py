#!/usr/bin/python3
import openai
import random
import os
import configparser


def get_api_key():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    # Retrieve the API key
    openai.api_key = config.get('config', 'api_key')


def get_quit_response():
    responses = ["Bye :(", "See you later!", "Goodbye!", "Sorry to see you leave :(", 
            "Ciao!", "Adios amigo!", "Hasta la vista, baby!", "Farewell!"]
    return random.choice(responses)

def chat_loop():
    model_engine = "text-davinci-003"
    history = ""
    
    while True:
        try: 
            # Get input from the user
            prompt = input("\033[36m<User> \033[0m")
            
            # Strip leading and trailing whitespace from the user's input
            stripped_prompt = prompt.strip()
            
            # Check if the user wants to quit
            if stripped_prompt.lower() == "/quit":
                print(f"\033[95m<AI> \033[33m{get_quit_response()}")
                break
            
            # Concatenate the previous conversation history with the current prompt
            prompt = history + prompt
          
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=3072,
                n=1,
                stop=None,
                temperature=0.5,
            )

            # Get the response from the model
            message = completions.choices[0].text.strip()
                             
            # Print the model's response in blue
            print(f"\033[95m<AI>\033[33m {message}\033[0m")

            # Update the conversation history
            history = prompt + message
        
        except KeyboardInterrupt:
            # Handle the KeyboardInterrupt exception
            print(f"\n\033[95m<AI>\033[33m {get_quit_response()}\033[0m")
            break


def main():
    print("Welcome to askAI v1.0\n")
    
    # Fine-tune the chatgpt model
    get_api_key()
    
    chat_loop()

if __name__ == "__main__":
    main()


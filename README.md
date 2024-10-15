# Memory App: Elderly Care Chatbot with LLM and TTS

This project is a web-based application designed to assist elderly users in nursing homes by offering conversational support through a chatbot. The chatbot leverages Large Language Models (LLMs) and Text-to-Speech (TTS) technologies to create engaging, voice-enabled conversations for the elderly. The app provides a platform where users can listen to generated stories, family memories, and other interactions with the chatbot.

## Features

- **Text-to-Speech (TTS) Integration:** Converts text-based stories and chatbot conversations into audio files.
- **Chatbot using LLMs:** A conversational agent that responds to user prompts.
- **User-Friendly Interface:** A simple and accessible web interface tailored to the elderly.
- **Flask Backend:** A lightweight web server powered by Flask to handle requests and responses.

## Structure

The app is organized into several key modules and routes:

### Backend (Flask)
- **`app.py`**: The main Flask application that initializes and runs the web server. This file manages the routing between different pages and handles the logic for the chatbot and TTS functionalities.
- **`llm_module.py`**: Handles interactions with the Large Language Model (LLM), generating responses based on user input.
- **`tts_module.py`**: Converts generated stories or responses from text into speech using a TTS engine.
- **`routes.py`**: Defines the routes for the web application, linking the different HTML pages and managing the flow of user requests.

### Frontend (HTML & CSS)
- **`home.html`**: The landing page where users are welcomed and guided to the story archive or chatbot interaction.
- **`family.html`**: A page where users can create and store family stories. The page also offers a form to generate chatbot conversations based on user prompts.
- **`audio.html`**: Displays the generated audio file for a story and offers playback functionality.
- **`text.html`**: Shows the text version of the generated story, with the option to convert it into an audio file.

## Installation

To get started with this project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/your-repo/memory-app.git
    cd memory-app
    ```

2. Set up a virtual environment and install dependencies:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Run the Flask server:

    ```bash
    flask run
    ```

4. Access the application by visiting `http://127.0.0.1:5000` in your web browser.

## Usage

### Home Page
- Users are welcomed and can navigate to the **Family Story Archive** to interact with the chatbot.

### Family Story Archive
- Users can input their name and a prompt for the chatbot to generate a response. The generated text response can then be turned into an audio file.

### Audio Playback
- Once the story has been generated, users can either view the text version or listen to the audio version directly through the web interface.

## Technologies Used

- **Flask**: Web framework for handling backend logic and routing.
- **Large Language Model (LLM)**: To generate chatbot responses based on user inputs.
- **Text-to-Speech (TTS)**: Converts generated stories into audio for the elderly to listen to.
- **HTML/CSS**: For building the user-friendly web interface.

## Future Enhancements

- **Multilingual Support**: Expanding the chatbot's capabilities to support multiple languages.
- **Voice Input**: Adding voice recognition for elderly users to interact with the chatbot using speech.
- **Personalized Stories**: Providing more personalized experiences based on user history.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

# Guru AI Assistant

A voice-controlled AI assistant with web interface support.

## Project Structure

- **backend.py**: FastAPI backend server for the web interface
- **guru.html**: Web interface frontend
- **guru.py**: Standalone voice assistant script (alternative to web interface)
- **test_gemini.py**: Test script for Gemini API

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

#### For Web Interface (backend.py):
Create a `.env` file in the project root:
```
GEMINI_API_KEY=your-gemini-api-key-here
```

Or set it as an environment variable:
```bash
export GEMINI_API_KEY=your-gemini-api-key-here
```

**Note**: The backend.py currently has a default API key, but it's recommended to use your own key via .env file.

#### For Standalone Script (guru.py):
The script uses `google-genai` package which may require separate authentication setup.

### 3. Run the Web Interface

1. Start the backend server:
```bash
python backend.py
```

2. Open `guru.html` in a web browser (double-click the file or use a local server)

The backend will run on `http://127.0.0.1:8000`

### 4. Run Standalone Voice Assistant (Alternative)

```bash
python guru.py
```

This script listens for the wake word "Guru" and responds to voice commands.

## Features

### Web Interface:
- Voice commands via browser speech recognition
- Quick command buttons
- Real-time chat interface
- Text-to-speech responses
- Web navigation commands (Google, YouTube, Instagram)
- AI-powered responses via Gemini

### Standalone Script:
- Wake word activation ("Guru")
- Voice command processing
- Web browser control
- Text-to-speech with edge-tts
- Gemini AI integration

## Troubleshooting

- **Speech recognition not working**: Make sure you're using a modern browser (Chrome, Edge) and grant microphone permissions
- **Backend connection error**: Ensure backend.py is running before using the web interface
- **API key errors**: Verify your Gemini API key is correctly set in the .env file
- **Audio playback issues (guru.py)**: Ensure your system has audio output configured


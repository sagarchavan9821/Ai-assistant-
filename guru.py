import asyncio
import edge_tts
import speech_recognition as sr
import webbrowser
import uuid
import os
from playsound import playsound
from google import genai
client = genai.Client()





async def speak(text):
    print(f"guru: {text}")

    file = f"{uuid.uuid4()}.mp3"
    communicate = edge_tts.Communicate(
        text=text,
        voice="en-IN-PrabhatNeural",
        rate="+10%"
    )
    await communicate.save(file)
    playsound(file)
    # Clean up audio file after playing
    try:
        os.remove(file)
    except:
        pass



def ask_gemini(prompt):
    try:
        response = client.models.generate_content(
            model="openai/gpt-4o-mini",
            contents=prompt
        )
        return response.text
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I am facing a problem."

async def processCommand(command):
    command = command.lower()

    if "open google" in command:
        await speak("opening google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        await speak("opening youtube")
        webbrowser.open("https://www.youtube.com")

    elif "open instagram" in command:
        await speak("opening instagram")
        webbrowser.open("https://www.instagram.com")

    elif "open flipkart" in command:
        await speak("opening flipkart")
        webbrowser.open("https://www.flipkart.com")

    elif "play music" in command:
        await speak("playing music")
        webbrowser.open("https://www.youtube.com/results?search_query=shape+of+you")
    
    else:
        await speak("let me think ")
        answer= ask_gemini(command)
        await speak (answer)

        


async def main():
    recognizer = sr.Recognizer()
    await speak("initializing guru")

    while True:
        try:
            with sr.Microphone() as source:
                print("listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)

            word = recognizer.recognize_google(audio).lower()
            print("heard:", word)

            if "guru" in word:
                await speak("yes sir")

                with sr.Microphone() as source:
                    print("guru active...")
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                print("command:", command)

                await processCommand(command)

        except sr.UnknownValueError:
            pass
        except Exception as e:
            print("error:",e)

                  
if __name__ == "__main__":

    asyncio.run(main())
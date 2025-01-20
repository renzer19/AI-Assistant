import openai
import pyttsx3
import speech_recognition as sr
import datetime

openai.api_key = "" # ganti dengan api token chatgpt

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak now...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio, language='id')
            print(f"you said : {query}")
            return query.lower()
        except:
            print("Sorry, I did not get that. Please try again.")
            return None

def chat_with_gpt(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # Ganti dengan model yang akan digunakan
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ]
        )
        answer = response['choices'][0]['message']['content']
        return answer.strip()
    except Exception as e:
        return f"error{str(e)}"

def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

def main():
    speak("Hello, I am your AI Assistant. How can I help you?")
    
    while True:
        query = listen()
        if query:
            if 'time' in query:
                time = get_time()
                speak(f"The current time is {time}")
            else:
                speak('let me think about that.')
                answer = chat_with_gpt(query)
                print(f"assistant: {answer}")
                speak(answer)
                
            if 'exit' in query:
                speak("Goodbye!")
                break

if __name__ == "__main__":
    main()
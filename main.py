import random
import pyttsx3

preferences = [
    "Which option do you favor?",
    "What's your preference?",
    "Do you have a particular choice in mind?",
    "Is there something you'd rather have?",
    "What do you lean towards?",
    "Are you inclined towards one option?",
    "Do you have a favorite?",
    "Any particular liking?",
    "Is there a specific selection you'd like?",
    "Which one suits your taste?"
    "Any particular inclination?",
    "What's your chosen option?",
    "Do you have a favored alternative?",
    "Which one do you lean towards?",
    "Is there a choice you're fond of?",
    "What's your favored selection?",
    "Do you have a preferred pick?",
    "Any specific liking?",
    "Which option holds your preference?",
    "Is there a particular one you prefer?",
    "What's your chosen course?",
    "Do you have a favored decision?",
    "Which one aligns with your liking?",
    "Is there a selection you're partial to?",
    "Do you have a favored alternative?",
    "What's your selected option?",
    "Is there one that stands out to you?",
    "Which one do you find more appealing?",
    "Do you have a favored choice?",
    "What's your chosen preference?",
    "Is there an option that suits you best?",
    "Do you have a liking for a specific one?",
    "Which one do you find more agreeable?",
    "Is there a particular one you're drawn to?",
    "What's your preferred pick?",
    "Do you have a liking for a certain option?",
    "Which one would you opt for?",
    "Is there an option that captures your preference?",
    "What's your selected preference?",
    "Do you have a favored selection?"
]
engine = pyttsx3.init()
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak(random.choice(preferences))
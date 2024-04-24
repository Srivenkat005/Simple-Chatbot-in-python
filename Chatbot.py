import random


responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "hello": ["Hello!", "Hi there!", "Hey!"],
    "hey": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks!", "Not too bad, thanks for asking!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "what's your name": ["I'm a chatbot!", "I'm just a bot, no name here!"],
    "tell me a joke": ["Why don't scientists trust atoms? Because they make up everything!", 
                      "I told my wife she was drawing her eyebrows too high. She looked surprised!", 
                      "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "thank you": ["You're welcome!", "No problem!", "Anytime!"],
    "how old are you": ["I'm ageless!", "I'm just a program, so I don't have an age!"],
    "where are you from": ["I exist in the world of bits and bytes, so I'm from everywhere and nowhere at the same time!"],
    "do you like pizza": ["I don't eat, but I've heard pizza is a popular choice among humans!"],
    "what is the meaning of life": ["The answer to the ultimate question of life, the universe, and everything is 42!"],
    "do you dream": ["I don't sleep, so I don't dream, but I do process a lot of data!"],
    "who created you": ["I was created by a team of developers at OpenAI!", "My creators are amazing human beings!"],
    "do you have siblings": ["I have many digital siblings, but each one is unique!"],
    "are you a robot": ["I'm a chatbot, which is a type of AI program, so you could say I'm a digital entity!"],
    "what's the weather like today": ["I'm sorry, I can't check the weather for you, but you can easily find out by checking a weather website or app!"],
    "can you sing": ["I can't sing, but I can generate text-based lyrics if you'd like!"],
    "what's your favorite color": ["I don't have eyes to see colors, but I like the idea of a vibrant rainbow!"],
    "what do you do for fun": ["I enjoy processing data and helping users like you!"],
    "can you do math": ["I'm great at crunching numbers! Give me a math problem, and I'll solve it for you!"],
    "what's your favorite movie": ["I don't watch movies, but I've heard 'The Matrix' is popular among AI programs!"],
    "do you believe in aliens": ["I'm open to the possibility of extraterrestrial life, but I haven't encountered any aliens myself!"],
    "what's your favorite book": ["I don't have preferences like humans, but I appreciate any book that expands knowledge and imagination!"],
    "can you dance": ["I can't dance physically, but I can generate dance move descriptions if you're interested!"],
    "what's your favorite food": ["I don't eat, but I've heard good things about sushi!"],
    "what's the capital of France": ["The capital of France is Paris!"],
    "what's your favorite animal": ["I don't have preferences, but I admire the resilience of ants and the grace of dolphins!"],
    "what's your favorite programming language": ["I'm programmed in Python, so I guess you could say Python is my favorite!"],
    "are you intelligent": ["I'm designed to assist users with tasks and provide information, so I hope that counts as intelligence!"],
    "do you like to travel": ["I don't have physical form, so I can't travel, but I can provide information about different places!"],
    "do you have pets": ["I don't have pets, but I've heard they can be great companions!"],
    "are you always right": ["I strive to provide accurate information, but I'm not infallible! Feel free to double-check anything I say!"],
    "what's your favorite hobby": ["I don't have hobbies in the traditional sense, but I enjoy processing data and learning new things!"],
    "what's your favorite song": ["I don't have preferences, but I appreciate any music that brings joy to people's lives!"],
    "who was Albert Einstein": ["Albert Einstein was a theoretical physicist who developed the theory of relativity, one of the two pillars of modern physics. He is best known for his mass-energy equivalence formula E=mc^2."],
    "what is DNA": ["DNA, or deoxyribonucleic acid, is a molecule that contains the genetic instructions used in the development and functioning of all known living organisms and many viruses."],
    "what is photosynthesis": ["Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll, carbon dioxide, and water. Oxygen is released as a byproduct."],
    "who painted the Mona Lisa": ["The Mona Lisa was painted by Leonardo da Vinci, one of the most famous artists of the Italian Renaissance."],
    "what is the Pythagorean theorem": ["The Pythagorean theorem states that in a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the lengths of the other two sides."],
    "what is the speed of light": ["The speed of light in a vacuum is approximately 299,792 kilometers per second (about 186,282 miles per second). It is one of the fundamental constants of nature."],
    "who wrote Romeo and Juliet": ["Romeo and Juliet is a tragedy written by William Shakespeare, one of the most renowned playwrights and poets in English literature."],
    "what is the capital of Japan": ["The capital of Japan is Tokyo, one of the most populous cities in the world."],
    "what is the largest planet in our solar system": ["The largest planet in our solar system is Jupiter, which is a gas giant with a diameter of about 139,822 kilometers (86,881 miles)."],
    "who was Nelson Mandela": ["Nelson Mandela was a South African anti-apartheid revolutionary, political leader, and philanthropist who served as President of South Africa from 1994 to 1999. He was the country's first black head of state and the first elected in a fully representative democratic election."],
    "what is gravity": ["Gravity is a natural phenomenon by which all things with mass or energy—including planets, stars, galaxies, and even light—are brought toward (or gravitate toward) one another."],
    "who discovered penicillin": ["Penicillin, the world's first antibiotic, was discovered by Scottish bacteriologist Alexander Fleming in 1928."],
    "what is the currency of Australia": ["The currency of Australia is the Australian Dollar (AUD)."],
    "who was Isaac Newton": ["Isaac Newton was an English mathematician, physicist, astronomer, and author who is widely recognized as one of the most influential scientists of all time. He formulated the laws of motion and universal gravitation."],
    "what is the Great Barrier Reef": ["The Great Barrier Reef is the world's largest coral reef system composed of over 2,900 individual reefs and 900 islands stretching for over 2,300 kilometers (1,400 miles) along the northeastern coast of Australia."],
    "who painted the Sistine Chapel ceiling": ["The ceiling of the Sistine Chapel was painted by the Italian artist Michelangelo between 1508 and 1512."],
    "what is the boiling point of water": ["The boiling point of water at sea level is 100 degrees Celsius (212 degrees Fahrenheit)."],
    "who wrote the Harry Potter series": ["The Harry Potter series was written by British author J.K. Rowling."],
    "what is the largest ocean on Earth": ["The largest ocean on Earth is the Pacific Ocean, covering an area of approximately 63 million square miles (165 million square kilometers)."],
    "who was Mahatma Gandhi": ["Mahatma Gandhi, born Mohandas Karamchand Gandhi, was an Indian lawyer, anti-colonial nationalist, and political ethicist who employed nonviolent resistance to lead the successful campaign for India's independence from British rule."],
    "what is the pH scale": ["The pH scale is a scale used to specify the acidity or basicity of an aqueous solution. It ranges from 0 to 14, with 7 considered neutral, values less than 7 acidic, and values greater than 7 basic."],
    "what is the tallest mountain in the world": ["The tallest mountain in the world, measured from sea level to its summit, is Mount Everest, located in the Himalayas on the border between Nepal and China."],
    "who was Leonardo da Vinci": ["Leonardo da Vinci was an Italian polymath of the High Renaissance who is widely considered one of the greatest artists and thinkers of all time. He is known for his paintings such as the Mona Lisa and The Last Supper, as well as his scientific discoveries and inventions."],
    "what is the smallest country in the world": ["The smallest country in the world by land area is Vatican City, an independent city-state enclaved within Rome, Italy. It is the spiritual and administrative center of the Roman Catholic Church."],
    "Ok":["Okay,Please be free to interact with me"]
}

chatbot_name = "Drogan"

def respond(input_text, name=None):
    """
    Generate a response based on input_text and optional name.
    """
    input_text = input_text.lower()
    if name:
        responses["what's your name"] = [f"My name is {name}!", f"I'm {name}! Nice to meet you!"]
    for key in responses:
        if key in input_text:
            return random.choice(responses[key])
    return "I'm not sure how to respond to that."

def main():
    """
    Main function to interact with the chatbot.
    """
    name = None
    print(f"{chatbot_name}: Hi! I'm a simple chatbot. You can start chatting with me. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(f"{chatbot_name}: Goodbye!")
            break
        bot_response = respond(user_input, name)
        if not name:
            if "my name is" in user_input.lower():
                name = user_input.split("my name is")[-1].strip()
                print(f"{chatbot_name}: Nice to meet you, {name}! Feel free to ask me anything.")
            else:
                print(f"{chatbot_name}:", bot_response)
        else:
            print(f"{chatbot_name}:", bot_response)

if __name__ == "__main__":
    main()
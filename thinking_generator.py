import random


class ThinkingGenerator:
    thinking_about_it = ["Processing your request...",
                         "Let me think about that...",
                         "Just a moment, compiling the answer...",
                         "Crunching the numbers...",
                         "Deep in thought, stand by...",
                         "Give me a second, I'm on it...",
                         "Analyzing the data...",
                         "Brain in overdrive, give me a sec...",
                         "Thinking caps on...",
                         "In the process of generating an answer...",
                         "Running the thought process...",
                         "Hold on, mind at work...",
                         "Thought engines firing...",
                         "Sifting through information...",
                         "Working on your answer now...",
                         "Big idea in progress...",
                         "In deep computational thought...",
                         "Thinking neurons firing up...",
                         "Let me assemble that for you...",
                         "Processing the possibilities...",
                         "Allow me a moment, I'm gathering information...",
                         "Your answer is on its way...",
                         "Delving into the knowledge base...",
                         "Hold tight, doing the mental gymnastics...",
                         "I'm on it, let the thoughts flow...",
                         "Conjuring up the response...",
                         "Thinking gears in action...",
                         "Just a moment, I'm putting it all together...",
                         "Rummaging through my data banks...",
                         "Processing the input, stay tuned..."]

    @staticmethod
    def random_thinking_statement():
        return random.choice(ThinkingGenerator.thinking_about_it)
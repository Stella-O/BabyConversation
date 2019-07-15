from random import choice

questions = ["Why is the sky blue?: ",
             "Why is there a face on the moon?: ",
             "Where are all the dinosaurs?: ",
             "Why are we here?: ",
             "Why are you smiling?: ",
             "Why do you like to sing in the shower?: ",
             "Why do I have to drink milk?: ",
             "Why can't I eat my toys?: ",
             "Where do babies come from?: ",
             "Why do I have to eat vegetables?: "]

question = choice(questions)
answer = input(question).strip().lower()

while(answer) != "just because":
    answer = input("Why?: ").strip().lower()

print("Oh... Okay")

    

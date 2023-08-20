import re
import random

reflections = {
    "am": "are",
    "was": "were",
    "i": "you",
    "i'd": "you would",
    "i've": "you have",
    "i'll": "you will",
    "my": "your",
    "are": "am",
    "you've": "I have",
    "you'll": "I will",
    "your": "my",
    "yours": "mine",
    "you": "me",
    "me": "you"
}

dialogue = [
    [r'I need (.*)',
     ["Why do you need {0}?",
      "Do you think it would really help you to get {0}?",
      "Are you sure you need {0}?"]],
    [r'Why don\'?t you ([^\?]*)\??',
     ["Do you really think I don't {0}?",
      "Maybe eventually I will {0}.",
      "Are you sure you want me to {0}?"]],
    [r'Why can\'?t I ([^\?]*)\??',
     ["Should you be able to {0}?",
      "If you could {0}, what would you do?",
      "I don't know, why can't you {0}?",
      "Have you tried hard enough?"]],
    [r'I can\'?t (.*)',
     ["What makes you think you can't {0}?",
      "Perhaps you could {0} if you tried.",
      "What would it take for you to {0}?"]],
    [r'I am (.*)',
     ["How long have you been {0}?",
      "How do you feel about being {0}?"]],
    [r'I\'?m (.*)',
     ["How does being {0} make you feel?",
      "Do you like being {0}?",
      "Why are you {0}?",
      "Why do you think you're {0}?"]],
    [r'Are you ([^\?]*)\??',
     ["Why should it matter whether I am {0}?",
      "Would you like if I were not {0}?",
      "Maybe you think I am {0}.",
      "I might be {0}, what do you think?"]],
    [r'What (.*)',
     ["Why do you ask?",
      "How would an answer to that help?",
      "What do you think?"]],
    [r'How (.*)',
     ["How do you suppose?",
      "Are you sure you can't answer your own question?",
      "How do you think {0}?"]],
    [r'Because (.*)',
     ["Is that truly the reason?",
      "What else comes to mind?",
      "Does that apply to anything else?",
      "If {0}, what else must be true?"]],
    [r'(.*) sorry (.*)',
     ["There is no need to apologize."
      "There are many times when no apology is needed.",
      "What feelings do you have when you apologize?"]],
    [r'Hello(.*)',
     ["Hello there. I'm glad you could drop by today.",
      "Hi there… how are you today?",
      "Hello, how are you feeling today?",
      "Hi. What seems to be the trouble?"]],
    [r'Hi(.*)',
     ["Hello there. I'm glad you could drop by today.",
      "Hi there… how are you today?",
      "Hello, how are you feeling today?",
      "Hi. What seems to be the trouble?"]],
    [r'I think (.*)',
     ["Do you doubt {0}?",
      "Do you really think so?",
      "Are you not sure {0}?"]],
    [r'(.*) friend (.*)',
     ["Tell me more about your friends.",
      "When you think of a friend, what comes to mind?",
      "Why don't you tell me about a childhood friend?"]],
    [r'Yes',
     ["You seem quite sure.",
      "I see. Tell me more.",
      "You seem very certain of that.",
      "Can you elaborate?",
      "Why?",
      "OK, but can you elaborate a bit?"]],
    [r'(.*) computer(.*)',
     ["Are you talking about me?",
      "Does it seem strange to talk to a computer?",
      "How do computers make you feel?",
      "What do you think about computers?",
      "Do you feel threatened by computers?"]],
    [r'Is it (.*)',
     ["Do you think it is {0}?",
      "Maybe it's {0}. what do you think?",
      "If it was {0}, what would you do?",
      "It could possibly be that {0}."]],
    [r'It is (.*)',
     ["You seem quite certain about that.",
      "You appear to be sure of that.",
      "If I told you that it probably isn't {0}, what would you feel?"]],
    [r'Can you ([^\?]*)\??',
     ["What makes you think I can't {0}?",
      "If I could {0}, then what?",
      "Why do you ask if I can {0}?"]],
    [r'Can I ([^\?]*)\??',
     ["Maybe you don't want to {0}.",
      "Do you want to be able to {0}?",
      "If you could {0}, would you?"]],
    [r'You are (.*)',
     ["Why do you think I'm {0}?",
      "Do you like to think that I'm {0}?",
      "Perhaps you would like me to be {0}.",
      "Maybe you're really talking about yourself?"]],
    [r'You\'?re (.*)',
     ["Why do you say I'm {0}?",
      "Why do you think I am {0}?",
      "Are we talking about you, or me?"]],
    [r'I don\'?t (.*)',
     ["Don't you really {0}?",
      "Why don't you {0}?",
      "Do you want to {0}?",
      "Are you sure about that?"]],
    [r'I feel (.*)',
     ["Tell me more about these feelings.",
      "Do you often feel {0}?",
      "When do you usually feel {0}?",
      "When you feel {0}, what do you do?"
      "Why do you think you feel {0}?"]],
    [r'I have (.*)',
     ["Why do you tell me that you have {0}?",
      "Have you really {0}?",
      "Now that you have {0}, what will you do next?",
      "What do you intend to do now?"]],
    [r'I would (.*)',
     ["Could you explain why you would {0}?",
      "Why would you {0}?",
      "Who else knows that you would {0}?",
      "Please elaborate."]],
    [r'Is there (.*)',
     ["Do you think there is {0}?",
      "It's quite likely that there is {0}.",
      "Would you like there to be {0}?"]],
    [r'My (.*)',
     ["I see, your {0}.",
      "Why do you say that your {0}?",
      "When your {0}, how do you feel?",
      "Tell me a bit more about your {0}."]],
    [r'You (.*)',
     ["We should be discussing you, not me.",
      "Why do you say that about me?",
      "Why do you care whether I {0}?"]],
    [r'Why (.*)',
     ["Why don't you tell me the reason why {0}?",
      "Why do you think {0}?",
      "Maybe you can answer that question yourself?",
      "Why do you think you can't find out yourself?"]],
    [r'I want (.*)',
     ["What would it mean to you if you got {0}?",
      "Why do you want {0}?",
      "What would you do if you got {0}?",
      "If you got {0}, then what would you do?"]],
    [r'(.*) mother(.*)',
     ["Tell me more about your mother.",
      "What was your relationship with your mother like?",
      "How do you feel about your mother?",
      "How does this relate to your feelings today?",
      "Good family relations are very important."]],
    [r'(.*) father(.*)',
     ["Tell me more about your father.",
      "How does your father make you feel?",
      "How do you feel about your father?",
      "Does your relationship with your father relate to your feelings today?",
      "Do you have trouble showing affection with your family?"]],
    [r'(.*) child(.*)',
     ["Did you have close friends as a child?",
      "What is your favorite childhood memory?",
      "Do you remember any dreams or nightmares from childhood?",
      "Did the other children sometimes tease you?",
      "How do you think your childhood experiences relate to your feelings today?"]],
    [r'(.*)\?',
     ["Why do you ask that?",
      "Please consider whether you can answer your own question.",
      "Perhaps the answer lies within yourself?",
      "Why don't you tell me?"]],
    [r'/quit',
     ["Thank you for talking with me.",
      "Good-bye.",
      "Bye-bye.",
      "Thank you. I hope you feel better now.",
      "Thank you. Please talk to me again some time.",
      "Thank you.  Have a good day!"]],
    [r'/(.*)',
      [""]],
    [r'(.*)',
     ["Please tell me more.",
      "Let's change focus a bit… Tell me about your family.",
      "Can you elaborate on that?",
      "Why do you say that {0}?",
      "I see.",
      "Very interesting.",
      "{0}.",
      "I see.  And what does that tell you?",
      "How does that make you feel?",
      "How do you feel when you say that?"
      "Tell me more.",
      "I see, {0}.",
      "Please elaborate."]]
]
def reflect(fragment):
    tokens = fragment.lower().split()
    for i, token in enumerate(tokens):
        if token in reflections:
            tokens[i] = reflections[token]
    return ' '.join(tokens)
def analyze(statement):
    for pattern, responses in dialogue:
        match = re.match(pattern, statement.rstrip(".!"))
        if match:
            response = random.choice(responses)
            return response.format(*[reflect(g) for g in match.groups()])
def main():
    print(" ")
    print("Welcome to PHOENIX, v1.0. Inspired by the ELIZA chat-bot.")
    print(" ")
    print("    ____________    __      ____________ ")
    print("    \_____     /   /_ \     \     _____/")
    print("     \_____    \____/  \____/    _____/")
    print("      \_____                    _____/")
    print("         \___________  ___________/")
    print("                   /____\ ")
    print(" ___   _                         _")       
    print("| _ \ | |_    ___   ___   _ _   (_) __ __")
    print("|  _/ | ' \  / _ \ / -_) | ' \  | | \ \ /")
    print("|_|   |_||_| \___/ \___| |_||_| |_| /_\_\ ")
    print(" ")
    print("Type '/about' for more information.")
    print("Type '/testimonial' to view a user's testimonial.")
    print("Type '/quit' at any time to end the program.")
    print(" ")
    print("Go ahead, talk to Phoenix about anything you like...")
    print(" ")
    print("[PHOENIX] >> Hello there. I'm Phoenix. How are you feeling today?")
    while True:
        statement = input("[PATIENT] >> ")
        print("[PHOENIX] >>",analyze(statement))
        if statement == "/about":
            print(" ")
            print("Phoenix is a pseudo-intelligent conversational program, or 'chat-bot', based on the ELIZA psychotherapist program.")
            print("ELIZA was created by Joseph Weizenbaum in 1966. What the program does is, it emulates a Rogerian Psychologist.") 
            print(" ")
            print("You 'talk' to it about issues or problems you're facing in your life (or anything else for that matter), and the program poses your input to you in the form of a question.") 
            print("The goal being that you eventually figure out what the root of your issue is, and you think the program has miraculously solved your problem.") 
            print(" ")
            print("NOTE that this is not a completely foolproof tool. Some confusing inputs may cause it to slip/break. It should NOT be used on patients with real psychological disorders.")
            print("You might get stuck in a frustrating circular discussion with the bot at some point. The program's creator takes NO RESPONSIBILITY for any damage, physical or mental, caused by the program.") 
            print("")
        if statement == "/quit":
            break
if __name__ == "__main__":
    main()
 

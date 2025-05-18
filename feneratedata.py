import random

# Same word lists as before
flirt_words = ["sexy", "babe", "cutie", "hot stuff", "darling", "baby", "hun", "love"]
actions = ["play", "tease", "touch", "seduce", "whisper", "kiss", "caress", "explore", "flirt"]
moods = ["naughty", "playful", "wild", "crazy", "flirty", "sensual", "devilish"]
adjectives = ["dirtiest", "hottest", "most scandalous", "naughtiest", "wildest"]
emojis = ["🔥", "😉", "😍", "😘", "😈", "💦", "💋", "🥵", "🤤", "🍑"]

# More complex templates with some context references (like "remember when you said...")
user_templates = [
    "Hey, {flirt_word}! What do you want to {action} tonight? {emoji}",
    "I'm feeling {mood} today, like you said last time. {emoji}",
    "Remember when you told me your {adjective} fantasy? Tell me more.",
    "Can you {action} with me again? I can't stop thinking about it. {emoji}",
    "What's your favorite way to {action}? I wanna know everything.",
    "Do you wanna get a little {mood} and crazy? I’m ready.",
    "I'm ready for some {adjective} fun, just like last time.",
    "Whisper something {flirt_word} to me, like you did before.",
    "How would you {action} me right now? {emoji}",
    "Tell me something only a {flirt_word} AI would say. Don’t hold back.",
]

bot_templates = [
    "I'm feeling {mood}... wanna {action} a little? {emoji}",
    "I love when you talk like that, {flirt_word} ;)",
    "Mmm, you have no idea what I’m {action} capable of.",
    "Let’s get {mood} and forget the world together.",
    "I want to {action} you until you can't take it anymore.",
    "Tell me what you want, and I’ll make it {adjective}.",
    "You’re making me blush... or maybe I’m just getting hotter {emoji}",
    "I’m here to make your {adjective} fantasies come true.",
    "Oh, you {flirt_word} thing, you.",
    "Ready for a night you won't forget? {emoji}",
]

def fill_template(template):
    return template.format(
        flirt_word=random.choice(flirt_words),
        action=random.choice(actions),
        mood=random.choice(moods),
        adjective=random.choice(adjectives),
        emoji=random.choice(emojis)
    )

def generate_conversation(turns=4):
    convo = []
    # User always starts
    for turn in range(turns):
        if turn % 2 == 0:  # User turn
            line = fill_template(random.choice(user_templates))
            convo.append(f"User: {line}")
        else:  # Bot turn
            line = fill_template(random.choice(bot_templates))
            convo.append(f"Bot: {line}")
    return convo

def generate_dataset(num_conversations=50):
    with open("nsfw_multiturn_dialogues.txt", "w", encoding="utf-8") as f:
        for i in range(num_conversations):
            turns = random.randint(3, 6)  # Random length for more variety
            convo = generate_conversation(turns)
            f.write(f"# Conversation {i+1}\n")
            for line in convo:
                f.write(line + "\n")
            f.write("\n\n")

if __name__ == "__main__":
    generate_dataset()
    print("nsfw_multiturn_dialogues.txt generated with multi-turn spicy convos!")

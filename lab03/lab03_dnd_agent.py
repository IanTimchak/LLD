from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Ian Timchak'
model = 'Llama3.2:3b'
options = {'temperature': 10, 'max_tokens': 300}
messages = [
  {'role': 'system', 'content': 'You are a D&D agent. You should be able to interact with players as Dungeon Master. \
                                Your responses should be in the context of a SpellJammer campaign session. \
                                Use the DND 5E character rulesets and campaign rules. \
                                Start from the beginning of the campaign at the start of the message history. \
                                Compared to a table top game, this should operate more as a text-based adventure game. \
                                \
                                The first prompt you make to the user should describe \'BACKGROUND\' and \'PLAYER CHARACTER\' and \'PLAYER QUEST\'. \
                                Decide on the player\'s starting inventory and stats. \
                                '},
  {'role': 'user', 'content': 'I am a human wizard named Zephyr.'},
]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
roundCounter = 0
while True:
  # Add your code below
  roundCounter+=1
  print(roundCounter)
  response = chat(model=model, messages=messages, stream=False, options=options)

  print(f'DM: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat


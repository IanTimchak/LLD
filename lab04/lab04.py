from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parents[1]))

from util.llm_utils import TemplateChat

def run_console_chat():
    chat = TemplateChat.from_file('lab04/lab04_trader_chat.json', sign='ato')
    chat_generator = chat.start_chat()
    print(next(chat_generator))
    while True:
        
            message = chat_generator.send(input('You: '))
            print('\n\nSM:', message)


if __name__ ==  '__main__':
    # run lab04.py to test your template interactively
    run_console_chat()
    pass
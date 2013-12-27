from io import open


class triggerHook:
    def __init__(self, *args):
        with open('text.txt', 'a', encoding='utf-8') as file:
            file.write( str(args) )
import random
from constants import *

def read_poetry(work, session_state):
    poem = session_state['poem'] if 'poem' in session_state else 0
    line_start = session_state['line_start'] if 'line_start' in session_state else 0
    if len(work) == 0:
        poem = random.randint(0, len(poems) - 1)
    elif work == OTHER:
        poem = (poem + 1) if poem + 1 < len(poems) else 0

    with open(poems[poem], 'r') as file:
        lines = [line.rstrip() for line in file]
        if work == NEXT:
            line_start = (line_start + 2) if line_start + 2 < len(lines) else 0

        return ' '.join(lines[line_start:line_start+2]), poem, line_start
            
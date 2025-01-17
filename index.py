from constants import *
from poetry import *

def response_construct(event, resp, session_state = {}):
    return {
        'version': event['version'],
        'session': event['session'],
        'response': resp,
        'session_state': session_state
    }

def build_poetry_response(event, session_state, work = ''):
    resp = poetry_response.copy()

    poem_text, poem, line_start = read_poetry(work, session_state)

    resp['text'] = poem_text + resp['text']
    session_state['poem'] = poem
    session_state['line_start'] = line_start
    return response_construct(event, resp, session_state)

def check_in(text, lst):
    txt = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    return sum(1 for y in txt.split() if y in lst) > 0

def handler(event, context):

    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        
        req_text = event['request']['original_utterance'].lower()
        session_state = {}

        if 'state' in event and 'session' in event['state'] \
            and len(event['state']['session']) > 0:

            session_state = event['state']['session']
        
        if req_text in exit_requests:
            return response_construct(event, exit_response)
        
        if check_in(req_text, yes_request):
            return build_poetry_response(event, session_state)
            
        if check_in(req_text, no_request):
            return response_construct(event, welcome_no_response, session_state)
        
        if check_in(req_text, next_request):
            return build_poetry_response(event, session_state, NEXT)
        
        if check_in(req_text, repeat_request):
            return build_poetry_response(event, session_state, REPEAT)
        
        if check_in(req_text, other_request):
            return build_poetry_response(event, session_state, OTHER)
        
        return response_construct(event, no_way_response, session_state)

    return response_construct(event, welcome_response)
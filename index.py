from constants import *
from poetry import *

def response_construct(event, resp):
    return {
        'version': event['version'],
        'session': event['session'],
        'response': resp,
    }

def poety_response(event):
    resp = poetry_response.copy()
    resp['text'] = read_file() + resp['text']
    return response_construct(event, resp)

def check_in(text, lst):
    txt = text.replace(',', '').replace('.', '').replace('!', '').replace('?', '')
    return sum(1 for y in txt.split() if y in lst) > 0

def handler(event, context):

    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        req_text = event['request']['original_utterance'].lower()
        
        if req_text in exit_requests:
            return response_construct(event, exit_response)
        
        if check_in(req_text, yes_request):
            return poety_response(event)
        
        if check_in(req_text, no_request):
            return response_construct(event, welcome_no_response)
        
        if check_in(req_text, next_request):
            return poety_response(event)
        
        if check_in(req_text, other_request):
            return poety_response(event)
        
        return response_construct(event, no_way_response)

    return response_construct(event, welcome_response)
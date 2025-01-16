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

def handler(event, context):

    if 'request' in event and \
            'original_utterance' in event['request'] \
            and len(event['request']['original_utterance']) > 0:
        req_text = event['request']['original_utterance'].lower()
        # TODO: common method
        if req_text in exit_requests:
            return response_construct(event, exit_response)
        
        if req_text in yes_request:
            return poety_response(event)
        
        if req_text in no_request:
            return response_construct(event, welcome_no_response)
        
        if req_text in next_request:
            return poety_response(event)
        
        if req_text in other_request:
            return poety_response(event)
        
        return response_construct(event, no_way_response)

    return response_construct(event, welcome_response)
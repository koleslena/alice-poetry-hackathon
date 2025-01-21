import unittest
from index import *
from constants import *

class TestSum(unittest.TestCase):

    def setUp(self):
        self.poem = 0
        self.line_start = 0
        self.event = {
                'version': 'version',
                'session': 'session',
            }
        self.session_state = {
                "poem": self.poem,
                "line_start": self.line_start
            }

    def test_check(self):
        self.assertFalse(check_in('уж не жду от жизни ничего я, ', exit_requests))
        self.assertTrue(check_in('выйти', exit_requests))
        self.assertTrue(check_in('учить', yes_request))

    def test_compare(self):
        comp, len_txt = compare('выхожу один я на дорогу; сквозь туман кремнистый путь', self.session_state)
        self.assertTrue(comp > 0)
        self.assertTrue(len_txt > 0)

        comp, len_txt = compare('ups..', self.session_state)
        self.assertFalse(comp > 0)
        self.assertTrue(len_txt > 0)

    def test_build_poetry_response_repeat(self):
        
        response = build_poetry_response(self.event, self.session_state, REPEAT)

        self.assertTrue('session_state' in response)
        self.assertTrue('poem' in response['session_state'])
        self.assertTrue('line_start' in response['session_state'])
        self.assertTrue(response['session_state']['poem'] == self.poem)
        self.assertTrue(response['session_state']['line_start'] == self.line_start)

    
    def test_build_poetry_response_next(self):
        
        response = build_poetry_response(self.event, self.session_state, NEXT)

        self.assertTrue('session_state' in response)
        self.assertTrue('poem' in response['session_state'])
        self.assertTrue('line_start' in response['session_state'])
        self.assertTrue(response['session_state']['poem'] == self.poem)
        self.assertTrue(response['session_state']['line_start'] == self.line_start + 2)

    def test_build_poetry_response_other(self):
        
        response = build_poetry_response(self.event, self.session_state, OTHER)

        self.assertTrue('session_state' in response)
        self.assertTrue('poem' in response['session_state'])
        self.assertTrue('line_start' in response['session_state'])
        self.assertTrue(response['session_state']['poem'] == (self.poem + 1) if self.poem + 1 < len(poems) else 0)
        self.assertTrue(response['session_state']['line_start'] == 0)


if __name__ == '__main__':
    unittest.main()

exit_response = {
            'text': 'Обязательно возращайтесь! Мы продолжим изучение стиха.\nВсего Вам доброго.',
            'end_session': 'true'
        }

welcome_response = {
            'text': 'Добро пожаловать! Приступим к изучению стиха?',
            'end_session': 'false',
            'buttons': [{'title': 'Да', 'hide': True}, {'title': 'Нет', 'hide': True}]
        }

welcome_no_response = {
            'text': 'Хотите выйти?',
            'end_session': 'false',
            'buttons': [{'title': 'Да', 'hide': True}, {'title': 'Учить', 'hide': True}]
        }

poetry_response = {
            'text': '\n Продолжим? Или другой стих?',
            'end_session': 'false',
            'buttons': [{'title': 'Продолжать', 'hide': True}, {'title': 'Другой', 'hide': True}, {'title': 'Выйти', 'hide': True}]
        }

no_way_response = {
            'text': 'Упс! Что-то пошло не так. Хотите выйти?',
            'end_session': 'false',
            'buttons': [{'title': 'Да', 'hide': True}, {'title': 'Учить', 'hide': True}]
        }

exit_requests = ['выход', 'хватит', 'надоело', 'алиса выйди из навыка', 'выйти', 'алиса хватит', 'алиса выйти']

yes_request = ['да', 'давай', 'учить']
no_request = ['нет', 'не надо', 'не']

next_request = ['продолжать', 'продолжи']
other_request = ['другой', 'следующий']
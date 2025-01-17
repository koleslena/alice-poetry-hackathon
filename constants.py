
NEXT = 'next'
OTHER = 'other'
REPEAT = 'repeat'

poems = [
    'texts/lermontov-road.txt',
    'texts/pushkin-k_kern.txt',
]

exit_response = {
            'text': 'Обязательно возращайтесь! Мы продолжим изучение стиха.\nВсего Вам доброго.',
            'end_session': 'true'
        }

welcome_response = {
            'text': 'Добро пожаловать! Приступим к изучению стиха?',
            'end_session': 'false',
            'buttons': [
                {'title': 'Да', 'hide': True}, 
                {'title': 'Нет', 'hide': True}
                ]
        }

welcome_no_response = {
            'text': 'Хотите выйти или будем учить стих?',
            'end_session': 'false',
            'buttons': [
                {'title': 'Выйти', 'hide': True}, 
                {'title': 'Учить', 'hide': True}
                ]
        }

poetry_response = {
            'text': '\n Повторить еще раз или прочитать следующие 2 строчки? Или другой стих?',
            'end_session': 'false',
            'buttons': [
                {'title': 'Продолжать', 'hide': True}, 
                {'title': 'Повторить', 'hide': True}, 
                {'title': 'Другой', 'hide': True}, 
                {'title': 'Выйти', 'hide': True}
                ]
        }

no_way_response = {
            'text': 'Упс! Что-то пошло не так. Хотите выйти или продолжим учить?',
            'end_session': 'false',
            'buttons': [
                {'title': 'Выйти', 'hide': True}, 
                {'title': 'Учить', 'hide': True}
                ]
        }

exit_requests = ['выход', 'хватит', 'надоело', 'алиса выйди из навыка', 'выйти', 'алиса хватит', 'алиса выйти']

yes_request = ['да', 'давай', 'учить']
no_request = ['нет', 'не надо', 'не']

next_request = ['продолжать', 'продолжи', 'продолжим']
repeat_request = ['повтори', 'повторим', 'провторять', 'снова', 'опять', 'еще', 'еще раз']
other_request = ['другой', 'следующий']
import speech_recognition
import webbrowser as wb

sr = speech_recognition.Recognizer()
sr.pause_threshold = 0.8

commands_dict = {
    'commands' : {
        'greeting' : ['привет', 'старт', 'начать', 'хай'],
        'task_create': ['создай задачу', 'создай заметку', '']
    }
}

def voice_listen():
    '''Функция распознавания голоса'''
    try:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration = 0.5)
            audio = sr.listen(source=mic)
            query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
        return query
    except speech_recognition.UnknownValueError:
        return 'Не понял того что ты сказал'

def greeting():
    '''Функция приветствия пользователя'''
    return 'Привет пользователь'
    

def task_create():
    '''Функция создания заметок'''
    print('Что добавить в список?')

    query = voice_listen()

    with open ('todo-list.txt', 'a') as file:
        file.write(f'{query}\n')
    return f'Задача была успешно добавлена в список'

def main():
    query = voice_listen()
    if query == 'привет':
        print(greeting())
    elif query == 'поиск':
        print(poisk())
    elif query == 'добавь задачу':
        print(task_create())
    else:
        print(query)
        print('Вас не слышно, либо такого запроса нет')

def poisk():
    print('Что нужно найти в интернете?')

    query = voice_listen()

    wb.open_new_tab(f'https://www.google.com/search?q={query}')
if __name__ == '__main__':
    main()
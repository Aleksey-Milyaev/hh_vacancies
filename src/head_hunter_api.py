from abc import ABC, abstractmethod


class HeadHunter(ABC):

    @abstractmethod
    def load_vacancies(self):
        pass


class HeadHunterApi(HeadHunter):

    def __init__(self, user_request):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.user_request = {'text': user_request, 'page': 0, 'per_page': 100}

    def load_vacancies(self):
        pass

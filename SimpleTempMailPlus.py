import requests
import random
import string
import json
from time import sleep


class Tempmail():
    def __init__(self, name, domain, __last_req=None):
        self.name = name
        self.domain = domain
        self.__last_req = __last_req

    def create(self):
        '''Creates mailbox'''
        self.__last_req = requests.get(
            url=f'https://tempmail.plus/api/mails?email={self.name}{self.domain}&limit=20&epin=').json()

    def update(self, timeout=3):
        '''Updates info in json about mailbox'''

        r = requests.get(
            url=f'https://tempmail.plus/api/mails?email={self.name}{self.domain}&first_id=0&epin=')
        if r.status_code != 200:
            raise Exception(
                f'Something went wrong while updating.\nStatus code: {r.status_code}')

        self.__last_req = r.json()
        sleep(timeout)

    def is_empty(self):
        '''Returns True or False if mailbox contains any messages'''
        return self.__last_req.get('count') <= 0

    def first_message(self):
        '''Returns first message text in mailbox'''
        return self.__request_message('last_id')

    def last_message(self):
        '''Returns last message text in mailbox'''
        return self.__request_message('first_id')

    def __request_message(self, position):
        message_id = self.__last_req.get(position)
        r = requests.get(
            url=f'https://tempmail.plus/api/mails/{message_id}?email={self.name}{self.domain}&epin='
        )

        return json.loads(json.dumps(r.json().get('text')))

    def get_domains():
        '''Returns list of all domains'''
        return ['@mailto.plus', '@fexpost.com', '@fexbox.org',
                '@fexbox.ru', '@mailbox.in.ua', '@rover.info',
                '@inpwa.com', '@intopwa.com', '@tofeat.com',
                '@chitthi.in']

    def generate_name(length=16):
        '''Returns randomly generated name'''
        return ''.join(
            random.choice(string.ascii_lowercase + string.digits)
            for _ in range(length)
        )

    def get_random_domain():
        '''Returns random domain'''
        return Tempmail.get_domains()[random.randint(0, 9)]

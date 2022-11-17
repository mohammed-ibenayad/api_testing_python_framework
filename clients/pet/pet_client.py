import json
from uuid import uuid4

from clients.base_client import BaseClient
from config import PET_URI
from utils.request import APIRequest


class PetClient(BaseClient):
    def __init__(self):
        super().__init__()

        self.base_url = PET_URI
        self.request = APIRequest()

    def create_person(self, body=None):
        last_name, response = self.__create_person_with_unique_last_name(body)
        return last_name, response

    def __create_person_with_unique_last_name(self, body=None):
        if body is None:
            last_name = f'User {str(uuid4())}'
            payload = dumps({
                'fname': 'New',
                'lname': last_name
            })
        else:
            last_name = body['lname']
            payload = dumps(body)

        response = self.request.post(self.base_url, payload, self.headers)
        return last_name, response

    def get_pet_by_id(self, pet_id):
        url = f'{self.base_url}/{pet_id}'
        return self.request.get(url)

    def get_pets_by_status(self, status_name):
        url = f'{self.base_url}/findByStatus'
        params = {'status': status_name}
        return self.request.get(url=url, params=params)

    def update_pet(self, payload):
        url = f'{self.base_url}'
        return self.request.put(url=url, payload=json.dumps(payload), headers=self.headers)

    def delete_pet(self, pet_id):
        url = f'{self.base_url}/{pet_id}'
        return self.request.delete(url=url)

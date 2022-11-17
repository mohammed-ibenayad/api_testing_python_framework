import json
from assertpy import assert_that, soft_assertions
from cerberus import Validator
from clients.pet.pet_client import PetClient

pet_client = PetClient()


def test_read_pets_by_status_has_expected_schema():

    schema = {"id": {'type': 'number'},
              "name": {'type': 'string'},
              "status": {'type': 'string', 'allowed': ['sold', 'available', 'pending']},
              "photoUrls": {'type': 'list', 'schema': {'type': 'string'}},
              }

    response = pet_client.get_pets_by_status('available')
    pets = json.loads(response.text)

    validator = Validator(schema, allow_unknown=True)

    with soft_assertions():
        for pet in pets:
            is_valid = validator.validate(pet)
            # Passing the error message raised by the schema validator through description param.
            assert_that(is_valid, description=validator.errors).is_true()

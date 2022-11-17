import requests
from tests.assertions.pet_assertions import *
from tests.assertions.generic_assertions import *
from tests.helpers.pet_helpers import *

client = PetClient()


def test_read_pets_by_status_has_status_field_in_response():
    status = 'available'
    response = client.get_pets_by_status(status)
    assert_api_status_code_as_expected(actual_status_code=response.status_code, expected_status_code=requests.codes.ok)
    assert_get_pets_by_status_have_response_with_status_field(pets=response.as_dict, status=status)


def test_read_pets_by_status_returns_only_valid_status():
    pets = client.get_pets_by_status('pending').as_dict
    assert_get_pets_by_status_response_contains_only_valid_statuses(pets, 'pending')


def test_get_pet_by_id_returning_valid_info():
    pets = client.get_pets_by_status('sold').as_dict
    pet_id = get_pet_id_randomly(pets, "id")

    assert_api_resource_id_exists(pet_id)
    response = client.get_pet_by_id(pet_id)
    assert_api_status_code_as_expected(actual_status_code=response.status_code, expected_status_code=requests.codes.ok)


# Calling a fixture: pet_data
def test_update_pet_with_valid_payload(pet_data):
    response = client.update_pet(pet_data)
    assert_api_status_code_as_expected(actual_status_code=response.status_code, expected_status_code=requests.codes.ok)
    assert_updated_pet_contains_correct_info(pet_uploaded=pet_data, pet_returned=response.as_dict)


def test_delete_pet_with_valid_id():
    pets = client.get_pets_by_status('sold').as_dict
    pet_id = get_pet_id_randomly(pets, "id")
    response = client.delete_pet(pet_id)
    assert_api_status_code_as_expected(actual_status_code=response.status_code, expected_status_code=requests.codes.ok)







"""
def test_read_pets__kent(logger):
    response = client.read_all_persons()

    assert_that(response.status_code).is_equal_to(requests.codes.ok)
    logger.info("User successfully read")
    assert_people_have_person_with_first_name(response, first_name='Kent')


def test_new_person_can_be_added():
    last_name, response = client.create_person()
    assert_that(response.status_code, description='Person not created').is_equal_to(requests.codes.no_content)

    peoples = client.read_all_persons().as_dict
    is_new_user_created = search_created_user_in(peoples, last_name)
    assert_person_is_present(is_new_user_created)


def test_created_person_can_be_deleted():
    persons_last_name, _ = client.create_person()

    peoples = client.read_all_persons().as_dict
    new_person_id = search_created_user_in(peoples, persons_last_name)['person_id']

    response = client.delete_person(new_person_id)
    assert_that(response.status_code).is_equal_to(requests.codes.ok)


def test_person_can_be_added_with_a_json_template(create_data):
    client.create_person(create_data)

    response = client.read_all_persons()
    peoples = response.as_dict

    result = search_nodes_using_json_path(peoples, json_path="$.[*].lname")

    expected_last_name = create_data['lname']
    assert_that(result).contains(expected_last_name)
"""

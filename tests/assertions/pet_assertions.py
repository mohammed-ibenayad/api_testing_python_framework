from assertpy import assert_that
from tests.helpers.pet_helpers import extract_statuses_from_pets_list


def assert_get_pets_by_status_have_response_with_status_field(pets, status):
    assert_that(pets).extracting('status').is_not_empty().contains(status)


def assert_get_pets_by_status_response_contains_only_valid_statuses(pets, status):
    statuses = extract_statuses_from_pets_list(pets)
    assert_that(statuses).contains_only(status)


def assert_updated_pet_contains_correct_info(pet_uploaded, pet_returned):
    assert_that(pet_uploaded).is_equal_to(pet_returned)


from assertpy import assert_that


def assert_api_status_code_as_expected(actual_status_code, expected_status_code):
    assert_that(actual_status_code).is_equal_to(expected_status_code)


def assert_api_resource_id_exists(res_id):
    assert_that(res_id, description=f'Could not find a resource with a valid ID ! - Got {res_id}').is_greater_than(0)

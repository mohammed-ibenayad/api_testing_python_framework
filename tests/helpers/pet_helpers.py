from clients.pet.pet_client import PetClient
from jsonpath_ng import parse
import random

client = PetClient()


def get_pet_id_randomly(pets: list, id_field: str) -> int:
    """
    Returns a random ID of a pet resource from a list of pets
    :param pets: pets list
    :param id_field: the name of the pets ID field (ex: "id")
    :return: int
    """
    ids = [pet[id_field] for pet in pets]
    return ids[random.randrange(0, len(ids)-1)] if ids else -1


def extract_statuses_from_pets_list(pets: list) -> list:
    """
    Extract all pest statuses in a list using Json path parser.
    :param pets: list of pets
    :return: list of statuses
    """
    expr = parse("$.[status]")
    statuses = []
    for pet in pets:
        pet_status = [match.value for match in expr.find(pet)]
        statuses.append(pet_status[0])

    return statuses


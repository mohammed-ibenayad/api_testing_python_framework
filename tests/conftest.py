import logging
import sys

import pytest

# from pytest_reportportal import RPLogger, RPLogHandler

from utils.file_reader import read_file

@pytest.fixture
def pet_data():
    yield read_file('pet_update.json')


@pytest.fixture(scope="session")
def logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    return logger

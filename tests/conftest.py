"""
Run make install before run tests
"""
import pytest
from foodelivery.app import create_app


@pytest.fixture(scope="module")
def app():
    """Instance of Main flask app"""
    return create_app()

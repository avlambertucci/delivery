import pytest
from delivery.app import create_app

# Fixture foi criada para ter o app disponivel na aplicacao de tests toda
@pytest.fixture(scope="module")
def app():
  """Fixtures of main app"""
  return create_app()
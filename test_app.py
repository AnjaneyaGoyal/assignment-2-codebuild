import pytest
from app import add, app

def test_add_success():
    assert add(2, 3) == 5

def test_intentional_failure():
    # Deliberately failing test to prove CI/CD pipeline catches errors
    print("Testing intentional failure detection...")
    assert add(2, 2) == 5, "AssertionError: 2 + 2 does not equal 5!"

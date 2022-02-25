from datetime import datetime

from dirty_equals import Contains, IsPartialDict, IsPositiveInt


def test_partial_dict():
    data = {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'john.doe@example.com',
        'phone_primary': '+1 (555) 555-5555',
        'phone_secondary': None,
        'address': {
            'street_address': '123 Main St',
            'city': 'New York',
            'state': 'NY',
            'zip': '12345',
        },
        'created_at': datetime.now().isoformat(),
        'dob': '28/02/1980',
        'marketing_opt_in': None,
        'tags': ['tag1', 'tag2'],
    }

    assert data == IsPartialDict(id=IsPositiveInt, first_name='John')


def test_not_contains():
    assert range(5) == Contains(-1)

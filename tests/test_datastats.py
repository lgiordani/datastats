import json

from datastats.datastats import DataStats


test_data = [
    {
        "id": 1,
        "name": "Laith",
        "surname": "Simmons",
        "age": 68,
        "salary": "£27888"
    },
    {
        "id": 2,
        "name": "Mikayla",
        "surname": "Henry",
        "age": 49,
        "salary": "£67137"
    },
    {
        "id": 3,
        "name": "Garth",
        "surname": "Fields",
        "age": 70,
        "salary": "£70472"
    }
]


def test_json():

    ds = DataStats()

    assert ds.stats(test_data, 20, 20000) == json.dumps(
        {
            'avg_age': 62,
            'avg_salary': 55165,
            'avg_yearly_increase': 837,
            'max_salary': [{
                "id": 3,
                "name": "Garth",
                "surname": "Fields",
                "age": 70,
                "salary": "£70472"
            }],
            'min_salary': [{
                "id": 1,
                "name": "Laith",
                "surname": "Simmons",
                "age": 68,
                "salary": "£27888"
            }]
        }
    )


def test__stats():

    ds = DataStats()

    assert ds._stats(test_data, 20, 20000) == {
        'avg_age': 62,
        'avg_salary': 55165,
        'avg_yearly_increase': 837,
        'max_salary': [{
            "id": 3,
            "name": "Garth",
            "surname": "Fields",
            "age": 70,
            "salary": "£70472"
        }],
        'min_salary': [{
            "id": 1,
            "name": "Laith",
            "surname": "Simmons",
            "age": 68,
            "salary": "£27888"
        }]
    }


def test__avg_age():

    ds = DataStats()

    assert ds._avg_age(test_data) == 62

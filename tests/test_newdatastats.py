import json

from datastats.datastats import NewDataStats


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


def test_init():

    ds = NewDataStats(test_data)

    assert ds.data == test_data


def test_ages():

    ds = NewDataStats(test_data)

    assert ds._ages == [68, 49, 70]


def test_salaries():

    ds = NewDataStats(test_data)

    assert ds._salaries == [27888, 67137, 70472]


def test__min_salary():

    ds = NewDataStats(test_data)

    assert ds._min_salary() == [{
        "id": 1,
        "name": "Laith",
        "surname": "Simmons",
        "age": 68,
        "salary": "£27888"
    }]


def test__max_salary():

    ds = NewDataStats(test_data)

    assert ds._max_salary() == [{
        "id": 3,
        "name": "Garth",
        "surname": "Fields",
        "age": 70,
        "salary": "£70472"
    }]


def test__avg_age():

    ds = NewDataStats(test_data)

    assert ds._avg_age() == 62


def test__avg_salary():

    ds = NewDataStats(test_data)

    assert ds._avg_salary() == 55165


def test__avg_yearly_increase():

    ds = NewDataStats(test_data)

    assert ds._avg_yearly_increase(20, 20000) == 837


def test__stats():

    ds = NewDataStats(test_data)

    assert ds._stats(20, 20000) == {
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


def test_json():

    ds = NewDataStats(test_data)

    assert ds.stats(20, 20000) == json.dumps(
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

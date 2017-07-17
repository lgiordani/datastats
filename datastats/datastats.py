import math
import json


class DataStats:

    def _salaries(self, data):
        return [int(d['salary'][1:]) for d in data]

    def _ages(self, data):
        return [d['age'] for d in data]

    def _avg_salary(self, data):
        return math.floor(sum(self._salaries(data))/len(data))

    def _avg_age(self, data):
        return math.floor(sum(self._ages(data))/len(data))

    def _avg_yearly_increase(self, data, iage, isalary):
        # iage and isalary are the starting age and salary used to
        # compute the average yearly increase of salary.

        # Compute average yearly increase
        average_age_increase = self._avg_age(data) - iage
        average_salary_increase = self._avg_salary(data) - isalary

        return math.floor(average_salary_increase/average_age_increase)

    def _select_salary(self, data, func):
        threshold = '£{}'.format(str(func(self._salaries(data))))

        return [e for e in data if e['salary'] == threshold]

    def _max_salary(self, data):
        return self._select_salary(data, max)

    def _min_salary(self, data):
        return self._select_salary(data, min)

    def _stats(self, data, iage, isalary):
        return {
            'avg_age': self._avg_age(data),
            'avg_salary': self._avg_salary(data),
            'avg_yearly_increase': self._avg_yearly_increase(
                data, iage, isalary),
            'max_salary': self._max_salary(data),
            'min_salary': self._min_salary(data)
        }

    def stats(self, data, iage, isalary):
        return json.dumps(
            self._stats(data, iage, isalary)
        )

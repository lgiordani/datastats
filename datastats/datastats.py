import math
import json


class DataStats:

    def _avg_salary(self, data):
        return math.floor(sum([int(e['salary'][1:]) for e in data])/len(data))

    def _avg_age(self, data):
        return math.floor(sum([e['age'] for e in data])/len(data))

    def _avg_yearly_increase(self, data, iage, isalary):
        # iage and isalary are the starting age and salary used to
        # compute the average yearly increase of salary.

        # Compute average yearly increase
        average_age_increase = math.floor(
            sum([e['age'] for e in data])/len(data)) - iage
        average_salary_increase = math.floor(
            sum([int(e['salary'][1:]) for e in data])/len(data)) - isalary

        return math.floor(average_salary_increase/average_age_increase)

    def _max_salary(self, data):
        # Compute max salary
        salaries = [int(e['salary'][1:]) for e in data]
        threshold = '£' + str(max(salaries))

        return [e for e in data if e['salary'] == threshold]

    def _min_salary(self, data):
        # Compute min salary
        salaries = [int(d['salary'][1:]) for d in data]
        return [e for e in data if e['salary'] ==
                '£{}'.format(str(min(salaries)))]

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

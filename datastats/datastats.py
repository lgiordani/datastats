import math
import json


class NewDataStats:

    def __init__(self, data):
        self.data = data

    @property
    def _salaries(self):
        return [int(d['salary'][1:]) for d in self.data]

    @property
    def _ages(self):
        return [d['age'] for d in self.data]

    def _select_salary(self, func):
        threshold = '£{}'.format(str(func(self._salaries)))

        return [e for e in self.data if e['salary'] == threshold]

    def _min_salary(self):
        return self._select_salary(min)

    def _max_salary(self):
        return self._select_salary(max)

    def _avg_salary(self):
        return math.floor(sum(self._salaries)/len(self.data))

    def _avg_age(self):
        return math.floor(sum(self._ages)/len(self.data))

    def _avg_yearly_increase(self, iage, isalary):
        # iage and isalary are the starting age and salary used to
        # compute the average yearly increase of salary.

        # Compute average yearly increase
        average_age_increase = self._avg_age() - iage
        average_salary_increase = self._avg_salary() - isalary

        return math.floor(average_salary_increase/average_age_increase)

    def _stats(self, iage, isalary):
        return {
            'avg_age': self._avg_age(),
            'avg_salary': self._avg_salary(),
            'avg_yearly_increase': self._avg_yearly_increase(iage, isalary),
            'max_salary': self._max_salary(),
            'min_salary': self._min_salary()
        }

    def stats(self, iage, isalary):
        return json.dumps(
            self._stats(iage, isalary)
        )


class DataStats:

    def stats(self, data, iage, isalary):
        nds = NewDataStats(data)
        return nds.stats(iage, isalary)

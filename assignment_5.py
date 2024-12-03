import math
from collections import Counter

# Arithmetic class
class Arithmetics:
    def __init__(self, list_data):
        self.list_data = list_data

    def mean(self):
        return sum(self.list_data) / len(self.list_data)

    def median(self):
        sorted_list_data = sorted(self.list_data)
        list_len = len(sorted_list_data)
        mid = list_len // 2
        if list_len % 2 == 0:
            return (sorted_list_data[mid - 1] + sorted_list_data[mid]) / 2
        else:
            return sorted_list_data[mid]

    def mode(self):
        data_count = Counter(self.list_data)
        max_count = max(data_count.values())
        modes = [k for k, v in data_count.items() if v == max_count]
        if len(modes) == 1:
            return modes[0]
        return modes

    def standard_deviation(self):
        mean_value = self.mean()
        variance = sum((x - mean_value) ** 2 for x in self.list_data) / len(self.list_data)
        return math.sqrt(variance)

# Person class
class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def loan_eligibility(self):
        if self.salary < 10000:
            raise LoanEligibilityException(self.salary)
        return True

# Loan eligibility check
class LoanEligibilityChecker:
    def check_eligibility(self, person):
        try:
            if person.loan_eligibility():
                print(f'{person.name} is eligible for loan')
        except LoanEligibilityException as e:
            print(e)

# Custom voter age exception
class VoterAgeException(Exception):
    def __init__(self, age, msg='Voter age is less than 18, not allowed to vote'):
        self.age = age
        self.msg = msg
        super().__init__(self.msg)

# Custom loan exception
class LoanEligibilityException(Exception):
    def __init__(self, salary, msg='Not eligible for loan'):
        self.salary = salary
        self.msg = msg
        super().__init__(self.msg)

# Voter eligibility check
class VotingEligibilityChecker:
    def check_eligibility(self, age):
        try:
            if age < 18:
                raise VoterAgeException(age)
            else:
                print('Voter is allowed to vote')
        except VoterAgeException as e:
            print(e)


# Question 1
data = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]
arithmetics = Arithmetics(data)
print(f'Mean: {arithmetics.mean()}')
print(f'Median: {arithmetics.median()}')
print(f'Mode: {arithmetics.mode()}')
print(f'Std deviation: {arithmetics.standard_deviation()}')
print()

# Question 2
vote_eligibility_checker = VotingEligibilityChecker()
vote_eligibility_checker.check_eligibility(17)
vote_eligibility_checker.check_eligibility(18)
print()

# Question 3
eligible_person = Person('Ani', 41200)
not_eligible_person = Person('Mesh', 9000)
eligibility_checker = LoanEligibilityChecker()
eligibility_checker.check_eligibility(eligible_person)
eligibility_checker.check_eligibility(not_eligible_person)

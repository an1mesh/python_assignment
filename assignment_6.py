import random
import string
from datetime import datetime


def remove_digit(arr):
    for i in range(len(arr)):
        arr[i] = ''.join((x for x in arr[i] if not x.isdigit()))
    return arr


def generate_random_data(no_of_data_entry):
    data = []
    for _ in range(no_of_data_entry):
        entry = {
            'id': random.randint(1, 1000),
            'value': random.uniform(1.0, 1000.0),
            'name': ''.join(random.choices(string.ascii_lowercase, k=5))
        }
        data.append(entry)
    return data


def separate_digits_alphabets(arr):
    digits = filter(lambda x: type(x) == int, arr)
    alphabets = filter(lambda x: type(x) == str, arr)
    print(list(digits))
    print(list(alphabets))


def check_date_range(date, start_date, end_date, date_format="%Y-%m-%d"):
    try:
        date = datetime.strptime(date, date_format)
        start_date = datetime.strptime(start_date, date_format)
        end_date = datetime.strptime(end_date, date_format)
        return start_date <= date <= end_date
    except Exception as e:
        return False


def get_unique_numbers(arr):
    unique_list = []
    st = set()
    for i in arr:
        if i in st:
            continue
        st.add(i)
        unique_list.append(i)
    unique_list = sorted(unique_list)
    return unique_list


arr1 = ['name512', 'same1example', 'joy18full']
arr2 = [1, 'a', 2, 'b', 3, 'c']
arr3 = [1, 2, 3, 1, 3, 4, 6, 5, 3]
print(remove_digit(arr1))
print()
separate_digits_alphabets(arr2)
print()
print(get_unique_numbers(arr3))
print()
print(check_date_range("2023-07-22", "2023-01-01", "2023-12-31"))
print()
random_data = generate_random_data(3)
for data in random_data:
    print(data)

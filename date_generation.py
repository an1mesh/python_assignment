from datetime import datetime, timedelta


def generate_dates(start_date_str, end_date_str=''):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    current_date = start_date
    if end_date_str == '':
        end_date = start_date + timedelta(days=4 * 365)
    else:
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')

    while current_date <= end_date:
        yield current_date.strftime('%Y-%m-%d')
        current_date += timedelta(days=1)


start_date = '2024-08-02'
end_date = '2025-01-01'

# Date generation for given range
range_date_generator = generate_dates(start_date, end_date)
for i in range_date_generator:
    print(i)

# Date generation for 4 years
date_generator = generate_dates(start_date)
for i in date_generator:
    print(i)

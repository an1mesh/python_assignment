from datetime import datetime, timedelta


def generate_dates(start_date_str):
    start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
    current_date = start_date
    end_date = start_date + timedelta(days=4 * 365)

    while current_date <= end_date:
        yield current_date.strftime('%Y-%m-%d')
        current_date += timedelta(days=1)


start_date = '2024-08-02'
date_generator = generate_dates(start_date)
for i in date_generator:
    print(i)

import argparse
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


def main():
    parser = argparse.ArgumentParser(description="Generate a range of dates.")
    parser.add_argument('start_date', type=str, help="Start date in YYYY-MM-DD format")
    parser.add_argument('--end_date', type=str,
                        help="End date in YYYY-MM-DD format. If not provided, will generate dates for 4 years from start_date.")

    args = parser.parse_args()

    if args.end_date:
        # Date generation for a given range
        print(f"Generating dates from {args.start_date} to {args.end_date}:")
        range_date_generator = generate_dates(args.start_date, args.end_date)
        for date in range_date_generator:
            print(date)
    else:
        # Date generation for 4 years
        print(f"Generating dates from {args.start_date} for 4 years:")
        date_generator = generate_dates(args.start_date)
        for date in date_generator:
            print(date)


if __name__ == "__main__":
    main()

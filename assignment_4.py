import time
from functools import wraps


def counter(start=0, step=1):
    count = start
    while True:
        yield count
        count += step


def retry(retry_count=3, retry_interval=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retry_count:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= retry_count:
                        print(f'Failed after {retry_count} attempts')
                        raise
                    print(f'Attempt {attempts} failed: {e}. Retrying in {retry_interval} seconds')
                    time.sleep(retry_interval)

        return wrapper

    return decorator


@retry(retry_count=3, retry_interval=3)
def retry_func():
    print("Retry is the function's function")
    raise ValueError("An error occurred")


arr = [1, 2, 3, 4, 5]
new_arr = [i * 2 for i in arr]

# Counter generator
gen = counter(start=1, step=1)
for _ in range(10):
    print(next(gen))

# Retry decorator
try:
    retry_func()
except Exception as e:
    print(f'Error: {e}')

# List comprehension
print(new_arr)

import time
import psutil
import os


class PerformanceMonitor:
    def __init__(self):
        self.data = {}

    def track_time(self, function):
        def wrapped(*args, **kwargs):
            start = time.time()
            result = function(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            func_name = function.__name__
            if func_name not in self.data:
                self.data[func_name] = {'time': [], 'memory': []}
            self.data[func_name]['time'].append(elapsed)
            print(f"{func_name} execution time: {elapsed:.6f} seconds")
            return result

        return wrapped

    def track_memory(self, function):
        def wrapped(*args, **kwargs):
            process = psutil.Process(os.getpid())
            start_memory = process.memory_info().rss / (1024 * 1024)  # in MB
            result = function(*args, **kwargs)
            end_memory = process.memory_info().rss / (1024 * 1024)  # in MB
            memory_used = end_memory - start_memory
            func_name = function.__name__
            if func_name not in self.data:
                self.data[func_name] = {'time': [], 'memory': []}
            self.data[func_name]['memory'].append(memory_used)
            print(f"{func_name} memory usage: {memory_used:.6f} MB")
            return result

        return wrapped

    def retrieve_stats(self, function_name):
        return self.data.get(function_name, None)


# Instantiate PerformanceMonitor
monitor = PerformanceMonitor()


@monitor.track_time
@monitor.track_memory
def sample_function():
    time.sleep(1)
    lst = [i for i in range(1000000)]
    return sum(lst)


# Execute the function
sample_function()

# Fetch and display stats
statistics = monitor.retrieve_stats('sample_function')
print(f"Stats for sample_function: {statistics}")

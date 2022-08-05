import requests
from time import time


def time_function(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        func(*args, **kwargs)
        t2 = time()
        print(f'Request took {round(t2 - t1, 2)} seconds.')
    return wrapper


@time_function
def make_request(url='https://www.google.com'):
    print(f'Making request to {url} ...')
    requests.get(url)


if __name__ == '__main__':
    url = input('Enter a website address (e.g. https://www.google.com): ')
    if url == '':
        make_request()
    else:
        make_request(url)
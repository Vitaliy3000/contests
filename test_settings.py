import sys
import time


def test(function, data):
    results = []
    if isinstance(data, dict):
        data = tuple(data.items())
    for n, (arg, answer) in enumerate(data, 1):
        try:
            start = time.time()
            result = function(*arg)
            finish = time.time()
        except :
            print(f'Error: {sys.exc_info()[0]}')
        else:
            if result == answer:
                results.append(True)
                lead_time = round(finish-start, 2)
                print(f'Test {n} is good. Time: {lead_time}')
            else:
                results.append(False)
                print(f'Test {n} is bad')
                print(f'result = {result}')
                print(f'answer = {answer}')
        finally:
            print()
    verdict = {False: 'Bad', True: 'Good'}[all(results)]
    print(f'Function is {verdict}')
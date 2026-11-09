
def calculate_total(prices):
    total = sum(prices)
    return total


def greet_user(name):
    return f"Hello, {name}!"


def calculate_average(numbers):
    if len(numbers) == 0:
        return 0

    average = sum(numbers) / len(numbers)
    return average


def process_data(data):
    new_data = []

    for number in data:
        if isinstance(number, int):
            new_data.append(number * 2)

    return new_data

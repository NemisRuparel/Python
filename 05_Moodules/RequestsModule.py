# Requests Module

import requests


# 1. GET Request
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1",
        timeout=10
    )

    response.raise_for_status()

    print("GET Request")
    print("Status Code:", response.status_code)
    print("Response:", response.json())

except requests.exceptions.RequestException as error:
    print("GET request failed:", error)


# 2. Accessing JSON Data
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos/1",
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    print("\nJSON Data")
    print("Title:", data["title"])
    print("Completed:", data["completed"])

except requests.exceptions.RequestException as error:
    print("JSON request failed:", error)


# 3. Query Parameters
try:
    response = requests.get(
        "https://httpbin.org/get",
        params={"name": "Nemis", "language": "Python"},
        timeout=10
    )

    response.raise_for_status()

    print("\nQuery Parameters")
    print("URL:", response.url)
    print("Parameters:", response.json()["args"])

except requests.exceptions.RequestException as error:
    print("Query request failed:", error)


# 4. POST Request
try:
    response = requests.post(
        "https://httpbin.org/post",
        json={"name": "Nemis", "course": "Python"},
        timeout=10
    )

    response.raise_for_status()

    print("\nPOST Request")
    print("Status Code:", response.status_code)
    print("Sent Data:", response.json()["json"])

except requests.exceptions.RequestException as error:
    print("POST request failed:", error)
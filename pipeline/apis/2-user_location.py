#!/usr/bin/env python3
"""
Script to get GitHub user location
"""
import requests
import sys
import time


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data.get("location"))

    elif response.status_code == 404:
        print("Not found")

    elif response.status_code == 403:
        reset_time = int(response.headers.get("X-RateLimit-Reset", 0))
        current_time = int(time.time())
        minutes = (reset_time - current_time) // 60
        print(f"Reset in {minutes} min")

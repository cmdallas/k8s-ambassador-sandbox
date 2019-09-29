import multiprocessing
from os import environ as env


workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()

bind = env.get("HOST", "0.0.0.0") + ":" + env.get("PORT", 5000)

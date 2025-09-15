from os import environ as env
import multiprocessing

PORT = int(env.get("PORT" , 8080))
debug_mod = int(env.get("DEBUG_MOD" , 1))

bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()


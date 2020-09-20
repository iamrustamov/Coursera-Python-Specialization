# Синхронизация потоков, блокировки

import threading

a = threading.RLock()  # Объект блокировки
b = threading.RLock()


def foo():
    try:
        a.acquire()  # Получить(захватить) блокировку
        b.acquire()
    finally:
        a.release()  # Отпустить блокировку
        b.release()

import os

MARK_AGRO_READY = "agro-ready"
MARK_AGRO_LOCK = "agro-lock"
MARK_AGRO_PROCESS = "agro-process"

def is_ready(folder):
    return os.path.exists(os.path.join(folder, MARK_AGRO_READY))


def is_lock(folder):
    return os.path.exists(os.path.join(folder, MARK_AGRO_LOCK))


def is_process(folder):
    return os.path.exists(os.path.join(folder, MARK_AGRO_PROCESS))


def lock(folder):
    if not is_lock(folder):
        with open(os.path.join(folder, MARK_AGRO_READY), 'w') as lock_file:
            os.utime(os.path.exists(folder, MARK_AGRO_READY), None)


def unlock(folder):
    if is_lock(folder):
        os.remove(os.path.join(folder, MARK_AGRO_READY))


def make_process(folder):
    if not is_lock(folder):
        with open(os.path.join(folder, MARK_AGRO_PROCESS), 'a') as process_file:
            os.utime(os.path.join(folder, MARK_AGRO_PROCESS), None)


def make_ready(folder):
    if not is_lock(folder):
        if is_process(folder):
            os.remove(os.path.join(folder, MARK_AGRO_PROCESS))
        with open(os.path.join(folder, MARK_AGRO_READY), 'a') as ready_file:
            os.utime(os.path.join(folder, MARK_AGRO_READY), None)
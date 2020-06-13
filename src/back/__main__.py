from sqlite3 import connect
from time import sleep

from src.lib.config import DB_PATH
from src.back.lib import clean_text


def process_runs():
    with connect(DB_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute((
            'SELECT r.id, r.state, r.input, r.output FROM runs AS r '
            'WHERE r.state = "SUBMITTED"'
        ))
        runs = cursor.fetchall()
        print(f'Found {len(runs)} to process')
        if not runs:
            return
        for run in runs:
            assert len(run) == 4
            print(f'Processing run {run[0]}')
            cursor.execute((
                'UPDATE runs '
                f'SET output = "{clean_text(run[2])}", state = "DONE" '
                f'WHERE id = "{run[0]}"'
            ))
            sleep(2)  # simulate a long run
            print(f'Processed run {run[0]}')


if __name__ == "__main__":
    while(True):
        process_runs()
        sleep(2)

from sqlite3 import connect, Error


class SQLiteStorage:

    _database = None

    def __init__(self, database_name):
        try:
           self._database = connect(database_name, check_same_thread=False)
        except Error as e:
            print("Database error: %s" %e)

    def execute(self, command: str):
        try:
            cur = self._database.cursor()
            cur.execute(command)
            cur.close()
            self._database.commit()
        except Exception as e:
            if self._database:
                self._database.rollback()
            raise e

    def fetch(self, command: str):
        cur = self._database.cursor()
        cur.execute(command)
        result = cur.fetchall()
        cur.close()
        return result
        
    def _up(self, script):
        with open(script, 'r') as f:
            sql_script = f.read()
        cur = self._database.cursor()
        cur.executescript(sql_script)
        cur.close()
    
    def _down(self, script):
        with open(script, 'r') as f:
            sql_script = f.read()
        cur = self._database.cursor()
        cur.executescript(sql_script)
        cur.close()
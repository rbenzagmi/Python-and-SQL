from Logistic import Logistic


class _Logistics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, logistic):
        self._conn.execute("""
            INSERT INTO logistics (id, name, count_sent, count_received) VALUES (?, ?, ?, ?)
        """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])

    def updateSent(self, id, newCountSent):
        self._conn.execute(""" 
            UPDATE logistics SET count_sent = ? WHERE id = ? 
        """, [newCountSent, id])

    def updateRec(self, id, newCountRec):
        self._conn.execute(""" 
            UPDATE logistics SET count_received = ? WHERE id = ? 
        """, [newCountRec, id])

    def find(self, id):
        c = self._conn.cursor()
        c.execute("""
              SELECT id, name, count_sent, count_received FROM logistics WHERE id = ?
          """, [id])
        return Logistic(*c.fetchone())
from Vaccine import Vaccine


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, vaccine):
        self._conn.execute("""
            INSERT INTO vaccines (id, date, supplier, quantity) VALUES (?, ?, ?, ?)
        """, [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])

    def delete(self, id):
        c = self._conn.cursor()
        c.execute("""
            DELETE FROM vaccines WHERE id = ?
        """, [id])

    def findID(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, date, supplier, quantity FROM vaccines WHERE id = ?
        """, [id])
        return Vaccine(*c.fetchone())

    def findIDREF(self, id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, date, supplier, quantity FROM vaccines WHERE supplier = ?
        """, [id])
        return Vaccine(*c.fetchone())

    def find(self):
        c = self._conn.cursor()
        c.execute("""
            SELECT * FROM vaccines ORDER BY date ASC 
        """)
        return Vaccine(*c.fetchone())

    def update(self, id, newQuantity):
        self._conn.execute(""" 
            UPDATE vaccines SET quantity = ? WHERE id = ? 
        """, [newQuantity, id])

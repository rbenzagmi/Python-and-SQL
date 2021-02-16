from Supplier import Supplier


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
            INSERT INTO suppliers (id, name, logistic) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.logistic])

    def find(self, name):
        c = self._conn.cursor()
        c.execute("""
             SELECT id, name, logistic FROM suppliers WHERE name = ?
         """, [name])
        return Supplier(*c.fetchone())

    def findREF(self, id):
        c = self._conn.cursor()
        c.execute("""
             SELECT id, name, logistic FROM suppliers WHERE id = ?
         """, [id])
        return Supplier(*c.fetchone())

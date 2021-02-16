from Clinic import Clinic


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
            INSERT INTO clinics (id, location, demand, logistic) VALUES (?, ?, ?, ?)
        """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])

    def find(self, location):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, location, demand, logistic FROM clinics WHERE location = ?
        """, [location])
        return Clinic(*c.fetchone())

    def update(self, id, newDemand):
        self._conn.execute(""" 
            UPDATE clinics SET demand = ? WHERE id = ? 
        """, [newDemand, id])

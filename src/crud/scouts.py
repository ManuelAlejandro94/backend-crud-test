import datetime

from mysql import connector


class Scouts(object):
    def __init__(
            self,
            database
    ):
        self.database = database

    def find_clients(self):
        cnx = connector.connect(**self.database)
        cursor = cnx.cursor()
        query = ("SELECT * FROM crud_test_db.clients")
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return results

    def find_client_by_names(self, firstName, lastName):
        cnx = connector.connect(**self.database)
        cursor = cnx.cursor()
        query = (
            "SELECT * FROM crud_test_db.clients WHERE FirstName = %s AND LastName = %s"
        )
        cursor.execute(query, (firstName, lastName))
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return results

    def insert_client(self, params):
        created = datetime.datetime.now()
        cnx = connector.connect(**self.database)
        cursor = cnx.cursor()
        query = (
            "INSERT INTO crud_test_db.clients (FirstName, LastName, Phone, Email, Age, ClientStatus, Created, Updated)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        )
        values = (
            params["firstName"], params["lastName"], params["phone"], params["email"], params["age"], \
            params["status"], created, created)
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()
        cnx.close()

    def update_client(self, params):
        cnx = connector.connect(**self.database)
        cursor = cnx.cursor()
        updated = datetime.datetime.now()
        query = (
            "UPDATE crud_test_db.clients SET FirstName=%s, LastName=%s, Phone=%s, Email=%s, Age=%s, ClientStatus=%s, Updated=%s"
            "WHERE ID=%s"
        )
        values = (
            params["firstName"], params["lastName"], params["phone"], params["email"], params["age"], \
            params["status"], updated, params["id"])
        cursor.execute(query, values)
        cnx.commit()
        row_affected = int(cursor.rowcount)
        cursor.close()
        cnx.close()
        return row_affected

    def find_client_by_id(self, id):
        cnx = connector.connect(**self.database)
        cursor = cnx.cursor()
        query = (
            "SELECT * FROM crud_test_db.clients WHERE ID = %s"
        )
        cursor.execute(query, id)
        cnx.commit()
        results = cursor.fetchall()
        cursor.close()
        cnx.close()
        return results

    def delete_client_by_id(self, id):
        cnx = connector.connect(**self.database)
        cursor = cnx.cursor()
        query = (
            f"DELETE FROM crud_test_db.clients WHERE ID = {int(id)}"
        )
        cursor.execute(query)
        cnx.commit()
        results = int(cursor.rowcount)
        cursor.close()
        cnx.close()
        return results
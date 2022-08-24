from flask import request

def register_routes(app, scouts):

    @app.route('/clients/<id>', methods=['PUT'])
    def put_clients(id):
        busqueda_params = request.get_json()

        params = {
            "id": int(id),
            "firstName": busqueda_params["firstName"],
            "lastName": busqueda_params["lastName"],
            "phone": busqueda_params["phone"],
            "email": busqueda_params["email"],
            "age": busqueda_params["age"],
            "status": busqueda_params["status"]
        }

        error = None
        try:
            rows_affected = scouts.update_client(params)
            if rows_affected > 0:
                return {
                           "code": 0,
                           "message": "Client updated successfully"
                       }, 200
            else:
                return {
                    "error_code": -1,
                    "message": "Client not found"
                }, 422
        except Exception as e:
            error = e
            raise e


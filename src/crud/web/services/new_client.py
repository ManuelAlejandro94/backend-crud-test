from flask import request

def register_routes(app, scouts):

    @app.route('/clients', methods=['POST'])
    def post_client():
        busqueda_params = request.get_json()

        response = []
        error = None
        try:
            results = scouts.find_client_by_names(busqueda_params["firstName"], busqueda_params["lastName"])
            if len(list(results)) > 0:
                return {
                    "error_code": -1,
                    "message": "Already exists this client"
                }, 422
            scouts.insert_client(busqueda_params)
            return {
                "code": 0,
                "message": "Client added successfully"
            }, 201
        except Exception as e:
            error = e
            raise e


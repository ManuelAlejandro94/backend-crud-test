from flask import request

def register_routes(app, scouts):

    @app.route('/clients/delete/<id>', methods=['PUT'])
    def delete_clients(id):
        multimap = request.args if request.method == 'PUT' else request.form
        busqueda_params = multimap.to_dict(flat=True)

        error = None
        try:
            rows_affected = scouts.delete_client_by_id(id)
            if rows_affected is not None and rows_affected > 0:
                return {
                           "code": 0,
                           "message": "Client deleted successfully"
                       }, 200
            else:
                return {
                    "error_code": -1,
                    "message": "Client not found"
                }, 422
        except Exception as e:
            error = e
            raise e


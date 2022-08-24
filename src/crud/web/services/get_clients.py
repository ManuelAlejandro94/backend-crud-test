import json
from flask import request

def register_routes(app, scouts):

    @app.route('/clients', methods=['GET'])
    def search_all_clients():
        multimap = request.args if request.method == 'GET' else request.form
        busqueda_params = multimap.to_dict(flat=True)

        response = []
        error = None
        try:
            results = scouts.find_clients()
            if results:
                for (ID, FirstName, LastName, Phone, Email, Age, ClientStatus, Created, Updated) in results:
                    obj = {
                        "id": ID,
                        "firstName": FirstName,
                        "lastName": LastName,
                        "phone": Phone,
                        "email": Email,
                        "age": Age,
                        "status": ClientStatus,
                        "created": Created,
                        "updated": Updated
                    }
                    response.append(obj)
            return response
        # except Exception as e:
        #     error = {
        #         "codigo": str(e.error.value[0].value[0]) + "." + str(e.error.value[1]),
        #         "detalle": str(e.detalle),
        #         "mensaje": str(e.args[0])
        #     }
        #     raise e
        except Exception as e:
            error = e
            raise e


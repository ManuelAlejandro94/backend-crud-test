from flask import Flask
import logging.config
from src.crud.scouts import Scouts
from src.crud.web.services import get_clients, new_client, update_client, delete_client


def logging_config(config):
    if config:
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=logging.DEBUG)


def create_application(config):
    logging.debug("Creando aplicación")

    logging_config(config.get('logging'))

    app = Flask(__name__)

    mysql_config = config.get('mysql')

    scouts = Scouts(
        database=mysql_config
    )

    get_clients.register_routes(app, scouts)
    new_client.register_routes(app, scouts)
    update_client.register_routes(app, scouts)
    delete_client.register_routes(app, scouts)

    return app

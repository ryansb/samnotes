"""Main entry point
"""
from pyramid.config import Configurator
from sqlalchemy import create_engine
from corniceapp.models import initialize_db
import os

db_url = "sqlite://"

if os.environ.get("OPENSHIFT_MYSQL_DB_URL"):
    db_url = os.environ.get("OPENSHIFT_MYSQL_DB_URL") + 'someapp'


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("cornice")
    config.scan("corniceapp.views")

    engine = create_engine(db_url)
    initialize_db(engine)

    return config.make_wsgi_app()

import click
import logging

from fastapi_tut.db.session import SessionLocal
from fastapi_tut.db.init_db import init_db, drop_db

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
	db = SessionLocal()
	init_db(db)

@click.command()
def initial_data() -> None:
	logger.info("Dropping tables")
	drop_db()
	
	logger.info("Creating initial data")
	init()
	logger.info("Initial data created")

@click.command()
def test():
	click.echo('hello world!')


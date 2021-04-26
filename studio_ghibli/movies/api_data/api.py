import requests
import logging

from constants import GHIBLI_URL

logger = logging.getLogger(__file__)

def get_films():
    """Get films from studio ghibli api"""
    try:
        return requests.get(f"{GHIBLI_URL}films")
    except ConnectionError as e: 
        logger.exception('Could not connect to ghibli because of %s', e)
        raise SystemExit(e)

def get_people():
    """Get people from studio ghibli api"""
    try:
        return requests.get(f"{GHIBLI_URL}people")
    except ConnectionError as e:
        logger.exception('Could not connect to ghibli because of %s', e)
        raise SystemExit(e)
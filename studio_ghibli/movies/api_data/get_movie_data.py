import json
import time
import logging

from constants import GHIBLI_URL

logger = logging.getLogger(__file__)

def get_movie_data(films, people):
    """Request handler for movie api"""
    success = False
    movies = {}
    if films.status_code == 200 and people.status_code == 200:
        movies = map_cast(films.content, people.content)
        if len(movies) > 0:
            success = True
        message = "Request to ghibli was a success"
    else:
        message = f"""
        The api call to ghibli failed because the response code from ghibli for 
        film api was {films.status_code} and for people api, it was
        {people.status_code}. Please call ghibli support"""
        logger.error('Could not get data from ghibli because of %s', message)

    return {
        "is_success": success,
        "message": message,
        "movies": movies
    }

def map_cast(films, people):
    """Mapping of person with relevent movie"""
    mapped_people_films = []
    if len(films) > 0:
        updated_people_obj = []
        for person in json.loads(people):
            for film_by_person in person["films"]:
                film_id = film_by_person.split("/")[-1]
                person[film_id] = film_by_person
            person.pop("films", None)
            updated_people_obj.append(person)

        for single_film in json.loads(films):  
            cast_each_film = []
            for person in updated_people_obj:
                if person.get(single_film["id"]):
                    cast_each_film.append(person)
            single_film["people"] = cast_each_film
            mapped_people_films.append(single_film)
    return mapped_people_films



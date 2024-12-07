import logging
from flask import Response

from controllers import CountryController
from .countries_blueprint import country_bp
from utils import create_response
from config import session_scope


@country_bp.route("/<int:id>", methods=['GET'])
def get_country_by_id_handler(id: int) -> Response:
    """
    Handle GET request to retrieve a country by its ID.

    Args:
        id (int): ID of the country to retrieve.

    Returns:
        Response: JSON response containing the country data or
                  an error message.

    Raises:
        Logs unexpected exceptions and returns a 500 error response.
    """
    try:
        # Using session_scope context manager for database session
        with session_scope() as session:
            # Retrieve the country from the database
            country = CountryController.get_one_by_id(id, session)

            # Return the country data if found
            if country:
                return create_response(
                    data=[("countries", country)],
                    code=200
                )

            # Handle the case where the country is not found
            return create_response(
                data=[("message", "Countries not found")],
                code=404
            )

    except Exception as e:
        # Log unexpected errors with traceback
        logging.error(
            f"Error occurred while retrieving country with ID {id}: {str(e)}",
            exc_info=True
        )
        return create_response(
            data=[(
                "error",
                "An unexpected error occurred while retrieving country data."
            )],
            code=500
        )

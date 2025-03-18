from passwork.passwork_api import PassworkAPI


def delete_password(api: PassworkAPI, password_id: str) -> None:
    """
    Delete a password from the Passwork API.

    This function awaits for API to be logged in,
    after function call you also should logout API in your upper-level code

    Args:
        api (PassworkAPI): An instance of PassworkAPI class initialized with appropriate credentials.
        password_id (str): The unique identifier of the password to delete.

    This function doesn't provide the API login and logout, API should be logged in at the call of function,
    after that you can call logout of API in your upper-level code 

    Example usage:
        api = PassworkAPI(credentials)\n
        delete_password(api, 'password123')

    Raises:
        ValueError: If password_id is empty or None.
    """

    # Delete the specified password
    api.delete_password(password_id=password_id)

"""
Loads configuration values from the .env file.
"""

import dotenv


def load_config():
    """
    Loads the .env file and validates entries.
    :return: A tuple with the configuration values.
    """
    config = dotenv.dotenv_values(".env")

    mastodon_host_url = config["MASTODON_HOST_URL"]
    mastodon_client_key = config["API_CLIENT_KEY"]
    mastodon_client_secret = config["API_CLIENT_SECRET"]
    mastodon_client_access_token = config["API_ACCESS_TOKEN"]

    if (
        not mastodon_host_url
        or not mastodon_client_key
        or not mastodon_client_secret
        or not mastodon_client_access_token
    ):
        raise EnvironmentError("Required environment variables are not set.")

    return (
        mastodon_host_url,
        mastodon_client_key,
        mastodon_client_secret,
        mastodon_client_access_token,
    )

"""
Script for welcoming new users.
"""

from mastodon import Mastodon  # pylint: disable=E0401

import config


def extract_usernames_from_directory_dict(directory_dict_list):
    """
    Takes a list of dictionary items and extracts a string value from each item.
    :param directory_dict_list: A dictionary list of user directory entries.
    :return: A sorted list of usernames.
    """
    account_list = []

    for directory_dict in directory_dict_list:
        if directory_dict is not None:
            if directory_dict["username"] is not None:
                print(str(directory_dict))
                # commented out until I get this script running regularly.
                # account_list.append('@' + directory_dict['username'])
                account_list.append(
                    directory_dict["username"]
                )  # No "@" in the username this way.

    sorted_list = sorted(account_list, key=str.casefold)

    return sorted_list


if __name__ == "__main__":
    (
        host_url,
        client_key,
        client_secret,
        client_token,
    ) = config.load_config_from_env_variables()

    mastodon = Mastodon(client_key, client_secret, client_token, host_url)

    directory_list = mastodon.directory(limit=10, order="new", local=True)
    print(str(directory_list))

    sorted_accounts_list = extract_usernames_from_directory_dict(directory_list)

    ACCOUNTS = "\n".join(sorted_accounts_list)

    accounts_str = (
        f"Welcome to the latest users! 👋\n\n{ACCOUNTS}\n\nThe profiles directory "
        + f"is also available at {host_url}/directory"
    )

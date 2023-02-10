import config

from mastodon import Mastodon


def extract_usernames_from_directory_dict(directory_dict_list):
    account_list = []

    for directory_dict in directory_dict_list:
        if directory_dict is not None:
            if directory_dict['username'] is not None:
                # account_list.append('@' + directory_dict['username']) # commented out until I get this script running regularly.
                account_list.append(directory_dict['username'])  # No "@" in the username this way.

    sorted_list = sorted(account_list, key=str.casefold)

    return sorted_list


if __name__ == "__main__":
    host_url, client_key, client_secret, client_token = config.load_config_from_env_variables()

    mastodon = Mastodon(client_key, client_secret, client_token, host_url)

    directory_list = mastodon.directory(limit=10, order="new", local=True)

    sorted_accounts_list = extract_usernames_from_directory_dict(directory_list)

    accounts = '\n'.join(sorted_accounts_list)

    accounts_str = 'Welcome to the latest users! 👋\n\n{}\n\nThe profiles directory is also available at {}/directory'\
        .format(accounts, host_url)

    response = mastodon.status_post(
        accounts_str,
        visibility='unlisted'
    )

    print(str(response))

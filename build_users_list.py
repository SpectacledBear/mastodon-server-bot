import config

from mastodon import Mastodon

def extract_user_ids_from_directory(directory_dict_list):
    pass


def wrote_user_ids_to_file(user_ids):
    pass


if __name__ == "__main__":
    host_url, client_key, client_secret, client_token = config.load_config_from_env_variables()

    mastodon = Mastodon(client_key, client_secret, client_token, host_url)

    offset = 0
    directory_list = []
    while True:
        new_directory_list = mastodon.directory(limit=25, order="new", offset=offset, local=True)

        if len(new_directory_list) == 0:
            break

        offset += len(new_directory_list)

        for directory in new_directory_list:
            directory_list.append(directory)

    print(str(directory_list))
    print(str(offset))

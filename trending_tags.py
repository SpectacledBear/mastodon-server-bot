"""
Script for publishing trending tags.
"""

from mastodon import Mastodon  # pylint: disable=E0401

import config


def extract_tags_from_tags_dict(tag_dicts):
    """
    Extract tag names from a dictionary of tag items.
    :param tag_dicts: A list of dictionary items representing tags.
    :return: A sorted list of tag names.
    """
    tag_names_list = []

    for tag_dict in tag_dicts:
        if tag_dict is not None:
            if tag_dict["name"] is not None:
                tag_names_list.append("#" + tag_dict["name"])

    sorted_list = sorted(tag_names_list, key=str.casefold)

    return sorted_list


if __name__ == "__main__":
    (
        host_url,
        client_key,
        client_secret,
        client_token,
    ) = config.load_config_from_env_variables()

    mastodon = Mastodon(client_key, client_secret, client_token, host_url)

    tag_dict_list = mastodon.trending_tags()

    tags_array = extract_tags_from_tags_dict(tag_dict_list)
    TAGS = "\n".join(tags_array)

    tag_str = (
        f"Trending federated hashtags:\n\n{TAGS}\n\nTrending hashtags are also "
        + f"available at {host_url}/explore/tags"
    )

    response = mastodon.status_post(tag_str, visibility="unlisted")

    print(str(response))

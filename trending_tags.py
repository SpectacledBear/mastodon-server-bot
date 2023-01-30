from mastodon import Mastodon

import config


def extract_tags_from_tags_dict(tag_dict_array):
    tag_names_list = []

    for tag_dict in tag_dict_array:
        if tag_dict is not None:
            if tag_dict['name'] is not None:
                tag_names_list.append('#' + tag_dict['name'])

    sorted_list = sorted(tag_names_list, key=str.casefold)

    return sorted_list


if __name__ == '__main__':
    host_url, client_key, client_secret, client_token = config.load_config_from_env_variables()

    mastodon = Mastodon(client_key, client_secret, client_token, host_url)

    tag_dict_array = mastodon.trending_tags()

    tags_array = extract_tags_from_tags_dict(tag_dict_array)
    tags = '\n'.join(tags_array)

    tag_str = 'Trending federated hashtags:\n\n{}\n\nTrending hashtags are also available at {}/explore/tags'.format(
        tags,
        host_url
    )

    response = mastodon.status_post(
        tag_str,
        visibility='unlisted'
    )

    print(str(response))

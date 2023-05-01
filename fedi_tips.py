"""
A script for taking a random Fediverse/Mastodon usage tip and tooting it.
"""
import os
import random
import sys

from mastodon import Mastodon  # pylint: disable=E0401

import config

TIPS_DIR = os.path.join(os.path.curdir, "tips")


def make_array_of_files(dir_path):
    """
    Make an array of file paths from a provided directory.
    :param dir_path: The directory path.
    :return: A list of file paths.
    """
    files = []

    for root_dir, _, filenames in os.walk(dir_path):
        for filename in filenames:
            files.append(os.path.join(root_dir, filename))

    return files


if __name__ == "__main__":
    (
        host_url,
        client_key,
        client_secret,
        client_token,
    ) = config.load_config_from_env_variables()

    mastodon = Mastodon(client_key, client_secret, client_token, host_url)

    tips_files = make_array_of_files(TIPS_DIR)

    # Randomly select a tip
    try:
        tip_filename = random.choice(tips_files)
    except IndexError:
        sys.exit(-1)

    with open(tip_filename, "r", encoding="utf8") as tip_file:
        tip = tip_file.read()

        response = mastodon.status_post(tip, visibility="unlisted")

        print(str(response))

# Mastodon Server Bot



# Table of Contents

- [Purpose](#purpose)
- [Development Environment Setup](#development-environment-setup)
- [Troubleshooting](#troubleshooting)
<!-- - [Deployment Pipeline](#deployment-pipeline) -->



# Purpose

What problem does this project solve?



# Development Environment Setup

## Prerequisites
- Python 3.X

## Configuration

Copy the `.env.teplate` file to `.env` and add your Mastodon server URL and development API credentials.
Details on where to get these values are described in the [Mastodon API](#mastodon-api) section.

## Quick Install

1. `python -m venv venv` - create a Python virtual environment
2. `venv\scripts\activate` - start the virtual environment
3. `python -m pip install -r requirements.txt` - install required module dependencies

## Mastodon API

The bot scripts rely on the Mastodon web API, accessed using the `Mastodon.py` module.

Specifically these Mastodon APIs are used:

- [`/api/v1/statuses`](https://docs.joinmastodon.org/methods/statuses/#create)
- [`/api/v1/trends/tags`](https://docs.joinmastodon.org/methods/trends/#tags)

To interact with a Mastodon server, the **Mastodon server URL** and **application credentials** are required.
Application credentials are created by adding an application within the Development section of your Preferences on the Mastodon server.
When you have the application credentials, add them to your `.env` file.

## Scripts

| Script           | Description                                            |
|------------------|--------------------------------------------------------|
| fedi_tips.py     | Toots a random tip from the `tips/` directory.         |
| trending_tags.py | Toots the latest trending tags of the Mastodon server. |



<!--
# Deployment Pipeline

## First Pipeline (for example, Continuous Integration)

- Jenkins job: <https://jenkinsurl/job/somejob-ci/>

What are the steps that happen in this pipeline?

## Second Pipeline

- <https://appurl>
- Jenkins job: <https://jenkinsurl/job/somejob-env/>
- [Logs](http://someurl/)


# Troubleshooting

Add any scripts or tools you need to troubleshoot your application.

### Restart the application (EXAMPLE)

To restart this specific service you can run the following commands against its AKS cluster:

    `az aks...`
-->



# Attribution

This README template is located at <https://github.com/SpectacledBear/mastodon-server-bot/blob/main/README.md>



#!/usr/bin/env python3
import logging
import os
import re


import requests


def get_star_and_fork(user, repo):
    global logger
    url = 'https://api.github.com/repos/{}/{}?client_id={}&client_secret={}'
    res = requests.get(url.format(user, repo, CLIENT_ID, CLIENT_SECRET))
    try:
        stars = res.json()['stargazers_count']
        forks = res.json()['forks_count']
        return (stars, forks)
    except Exception as e:
        logger.error(user, repo, res.json())
        raise e


def parse_link(md_links):
    global logger
    parsed_md_links = []
    count = 0
    for md_link in md_links:
        if 'https://github.com' in md_link:
            try:
                pattern = (r'\[(.+)\]\((https://github.com/'
                           '([^/]+)/([^/^#]+)/*.*)\)')
                title, link, user, repo = re.match(pattern, md_link).groups()
                stars, forks = get_star_and_fork(user, repo)
                txt = '[:octocat: {}]({}) - :star: {} :fork_and_knife: {}'
                txt = txt.format(title, link, stars, forks)
                parsed_md_links.append(txt)
                count += 1
                logger.debug('{}. Done {}/{}. Parsed: {}'.format(count,
                                                                 user,
                                                                 repo,
                                                                 txt))
            except Exception as e:
                parsed_md_links.append(md_link)
                logger.error('{} {}'.format(md_link, e))
        else:
            title, link = re.match(r'\[(.+)\]\((.+)\)', md_link).groups()
            title = ':earth_americas: {}'.format(title)
            parsed = '[{}]({})'.format(title, link)
            parsed_md_links.append(parsed)
            count += 1
            logger.debug('{}. Done {}. Parsed: {}'.format(count, link, parsed))
    return zip(md_links, parsed_md_links)


def main():

    # get source readme.md to parse
    res = requests.get('https://raw.githubusercontent.com/vinta/'
                       'awesome-python/master/README.md')

    # get all links
    md_links = re.findall('.+(\[.+\]\(http[^\)]+\))+.+', res.text)
    replace_list = parse_link(md_links)
    final_txt = '''# Fucking Awesome Python

A curated list with Github stars and forks stats based on awesome
 [awesome-python](https://github.com/vinta/awesome-python),
 inspired by
 [fucking-awesome-go](https://github.com/hvnsweeting/fucking-awesome-go)
 and
 [fucking-awesome-python](https://github.com/trananhkma/fucking-awesome-python)

'''
    final_txt += res.text
    for i in replace_list:
        final_txt = final_txt.replace(i[0], i[1])
    with open('README.md', 'w') as f:
        f.write(final_txt)


# logging config
log_formatter = logging.Formatter('%(asctime)s [%(threadName)-12.12s]'
                                  ' [%(levelname)-5.5s]  %(message)s')
logger = logging.getLogger('FAP')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("{}.log".format(__name__))
file_handler.setFormatter(log_formatter)
logger.addHandler(file_handler)

console_handler = logging.StreamHandler()
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)

# get github client id and client secret
CLIENT_ID = os.getenv('fap_client_id')
CLIENT_SECRET = os.getenv('fav_client_secret')


if __name__ == '__main__':
    main()

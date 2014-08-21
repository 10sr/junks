#!/usr/bin/env python3

TOKEN_FILE = "~/.jtwitter.token"
CONSUMER_KEY = "QnuQ9aJRkWsZywky93QF4Dr4a"
CONSUMER_SECRET = "Ri960YKmMGGM1ga667lVUL4aELPLOcVd0ORvxUVXQkyVyqaeWL"

import sys
import os

import twitter as tw

TOKEN_FILE = os.path.expanduser(TOKEN_FILE)


def ensure_auth():
    if not os.path.exists(TOKEN_FILE):
        tw.oauth_dance("j/python/twitter", CONSUMER_KEY, CONSUMER_SECRET,
                       TOKEN_FILE)
    return


def update_status(text):
    text = text.strip()
    if not text:
        raise RuntimeError("No text to update")

    oauth_token, oauth_secret = tw.read_token_file(TOKEN_FILE)

    t = tw.Twitter(auth=tw.OAuth(oauth_token, oauth_secret,
                                 CONSUMER_KEY, CONSUMER_SECRET))

    t.statuses.update(status=text)

    return


def main(argv):

    ensure_auth()

    if sys.stdin.isatty():
        update_status(input("Status: "))
    else:
        update_status(sys.stdin.read())

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

#!/usr/bin/env python3

import sys, os

import twitter as tw

def main(argv):
    TOKEN_FILE = os.path.expanduser("~/.jtwitter.token")
    CONSUMER_KEY = "QnuQ9aJRkWsZywky93QF4Dr4a"
    CONSUMER_SECRET = "Ri960YKmMGGM1ga667lVUL4aELPLOcVd0ORvxUVXQkyVyqaeWL"

    if not os.path.exists(TOKEN_FILE):
        tw.oauth_dance("j/python/twitter", CONSUMER_KEY, CONSUMER_SECRET,
                       TOKEN_FILE)

    oauth_token, oauth_secret = tw.read_token_file(TOKEN_FILE)

    t = tw.Twitter(auth=tw.OAuth(oauth_token, oauth_secret,
                                 CONSUMER_KEY, CONSUMER_SECRET))
    t.statuses.update(status="@tos j/p/t test")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))

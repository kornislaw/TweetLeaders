import os
import json
import tweepy
from pprint import pprint as pp
from tweepy import OAuthHandler


# getting keys from OS ENV variables (stored there to avoid commiting secrets to the repo)
consumer_key = os.environ['TWITTER_TWEETLEAD_CONSUMER_KEY']
consumer_secret = os.environ['TWITTER_TWEETLEAD_CONSUMER_SECRET']
access_token = os.environ['TWITTER_TWEETLEAD_ACCESS_TOKEN']
access_secret = os.environ['TWITTER_TWEETLEAD_ACCESS_SECRET']

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# api.search_users('@AndrzejDuda')
u_name = 'kornislaw'

def print_followers():
    u = api.get_user(u_name)

    nodes = 'nodes = [\n'
    nodes += f"\t\t{{id: {u.id}, shape: 'circularImage', image: '{u.profile_image_url}', label:'{u.screen_name}'}},\n"
    for flr in api.followers(u_name):
        nodes += f"\t\t{{id: {flr.id}, shape: 'circularImage', image: '{flr.profile_image_url}', label:'{flr.screen_name}'}},\n"
    nodes += '];\n'

    edges = 'edges = [\n'
    for flr in api.followers(u_name):
        edges += f'\t\t{{from: {flr.id}, to: {u.id}}},\n'
    edges += '];\n'

    print(nodes)
    print(edges)

def get_followers(u_name):
    u = api.get_user(u_name)
    flrs = api.followers(u_name)
    nodes = [{'id': flr.id, 'shape': 'circularImage', 'image': flr.profile_image_url, 'label': flr.screen_name} for flr in flrs]
    nodes.append({'id': u.id, 'shape': 'circularImage', 'image': u.profile_image_url, 'label': u.screen_name, 'size': 70 })
    edges = [{'from': flr.id, 'to': u.id} for flr in flrs]

    return json.dumps({'nodes': nodes, 'edges': edges})
    # return {'nodes': nodes, 'edges': edges}

print(get_followers('kornislaw'))
# def print_followed():
    # API.friends_ids(id/screen_name/user_id[, cursor]

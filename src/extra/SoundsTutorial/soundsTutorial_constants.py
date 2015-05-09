#-*- coding: utf-8 -*-
import reverse_sort
import application
actions = reverse_sort.reverse_sort([  ("audio", _(u"Audio tweet.")),
  ("create_timeline", _(u"User timeline buffer created.")),
    ("delete_timeline", _(u"Buffer destroied.")),
    ("dm_received", _(u"Direct message received.")),
    ("dm_sent", _(u"Direct message sent.")),
    ("error", _(u"Error.")),
  ("favourite", _(u"Tweet favorited.")),
  ("favourites_timeline_updated", _(u"Favourites buffer updated.")),
  ("geo",   _(u"Geotweet.")),
("limit", _(u"Boundary reached.")),
    ("list_tweet", _(u"List updated.")),
    ("max_length", _(u"Too many characters.")),
    ("mention_received", _(u"Mention received.")),
  ("new_event", _(u"New event.")),
  ("ready", _(unicode(application.name+" is ready."))),
    ("reply_send", _(u"Mention sent.")),
    ("retweet_send", _(u"Tweet retweeted.")),
    ("search_updated", _(u"Search buffer updated.")),
    ("tweet_received", _(u"Tweet received.")),
    ("tweet_send", _(u"Tweet sent.")),
    ("trends_updated", _(u"Trending topics buffer updated.")),
    ("tweet_timeline", _(u"New tweet in user timeline buffer.")),
    ("update_followers", _(u"New follower.")),
    ("volume_changed", _(u"Volume changed."))])
What's New
----------
We've added three methods for interacting with Collections on Twitter:

* :py:func:`twitter.api.Api.GetCollectionEntries` (https://dev.twitter.com/rest/reference/get/collections/entries) will return a Collection populated with Status objects found in that Collection. This Collection object will have a not-None `statuses` attribute. This Collection will also have a `timeline` attribute for organizing tweets.

* :py:func:`twitter.api.Api.GetCollection` (https://dev.twitter.com/rest/reference/get/collections/show) will return a Collection with some information about that collection such as name, id, user, etc.

* :py:func:`twitter.api.Api.GetCollectionList` (https://dev.twitter.com/rest/reference/get/collections/list) will return a list of Collections (along with previous and next cursors) either for a given: user_id, screen_name, or containing a particular status.

Additionally, a :py:class:`twitter.models.Collection` model has been added. Because the endpoints above return a couple different flavors of Collections (with and without statuses/timelines/etc.), users should be aware that attributes may or may not exist (they should return ``None``, but file a bug report if this isn't the case for things like ``statuses`` or ``min_position``, etc. As with all models, there is a ``_json`` attribute if it is required.


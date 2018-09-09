![News.io App](https://support.apple.com/library/content/dam/edam/applecare/images/en_US/mac_apps/itunes/iphone7-ipad-use-news-hero.jpg)

Unofficial News App through News API for [News API](https://newsapi.org/).
The app is live here [News.io](https://news-io.herokuapp.com/).


Features
========

- Built with Python 3 (3.7+) and Flask
- Shows 'pitches','categories' and sorted by post date
- Styled using Bootstrap
- Handles external get posts and requests from database
- Get news articles from several sources (`choose from landing page`)


Installation
========

    $ git clone <repository_url>


Usage
========

**NOTE:** You need to have fully cloned it to run it locally.


    $ ./start.sh 

    # it will launch the web page from local server and fetch 
    news using api provided


API Object Reference
========

## Classes: `user, Pitch`


**Arguments:**

| Name | Type | Required | Description | Default |
| ---- | ---- | -------- | ----------- | ------- |
| `pitch` | string | No | pitches from this category only and sorted by relevancy. | `(empty string)`  |
| `user` | integer | No | Returns the user from this database source only. | `(user's choice)` |



## Class: `Pitches`

Each `Pitch` has the following properties

- **title** - pitch name
- **id** - news source unique id
- **content** - the pitch content
- **pot date** - official website link to news source

## Class: `User`

Each `User` has the following properties

- **id** - unique id of the article
- **username** - name stored on database
- **email** - user email
- **image url** - profile picture for user

Tests
========

To run the tests locally just do:

    $ cd app
    $ python3.7 test_users.py


The tests are run on a local test server.

Contribute
========

If you want to add any new features, or improve existing ones, feel free to send a pull request!
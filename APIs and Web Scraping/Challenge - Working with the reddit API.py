## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
params= {'t':'day'}

response = requests.get('https://oauth.reddit.com/r/python/top', headers = headers, params = params)

python_top = response.json()


## 3. Getting the Most Upvoted Post ##

python_top_articles = python_top['data']['children']

ups = 0
id_ = 0
for article in python_top_articles:
    if article['data']['ups'] > ups:
        ups = article['data']['ups'] 
        id_ = article['data']['id'] 

most_upvoted = id_

## 4. Getting Post Comments ##

response = requests.get('https://oauth.reddit.com/r/python/comments/4b7w9u', headers = headers)

comments = response.json()

## 5. Getting the Most Upvoted Comment ##

comments_list = comments[1]['data']['children']

ups = 0
id_ = 0
for comment in comments_list:
    if comment['data']['ups'] > ups:
        ups = comment['data']['ups'] 
        id_ = comment['data']['id'] 

most_upvoted_comment = id_


## 6. Upvoting a Comment ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
payload= {'dir': 1, 'id':'d16y4ry'}

response = requests.post('https://oauth.reddit.com/api/vote', headers = headers, json = payload)

status = response.status_code
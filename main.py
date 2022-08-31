import time
from utils.format_comment import filter_comments_to_tweet
from utils.get_users_comments import get_comments_from_all_users

users = [
    "HS_Celestalon",
    "ChakkiHS",
    "HS_Valerie_C",
    "IksarHS",
    "Cgsongbird",
    "HS_Liv",
    "MyntCondytion",
    "cmdylux",
    "Kaeyoh",
]

i = 0

while True:
    print('Waking up......................... ')
    comments = get_comments_from_all_users(users)
    time.sleep(5)
    filter_comments_to_tweet(comments)
    print('Done......................Sleep mode activated ')

    time.sleep(60)

    

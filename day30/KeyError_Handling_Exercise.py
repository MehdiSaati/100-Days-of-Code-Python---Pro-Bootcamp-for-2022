# Key Error Handling Exercise
facebook_posts = [
    {'likes':21, 'comments': 2},
    {'likes':13, 'comments': 2, 'shares': 1},
    {'likes':33, 'comments': 8, 'shares': 3},
    {'likes':4, 'comments': 2},
    {'likes':1, 'comments': 1},
    {'likes':19, 'comments': 3},
]

total_likes = 0

for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
       
    except KeyError as key:
        total_likes += 0

print(total_likes)

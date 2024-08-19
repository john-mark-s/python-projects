# %%
# Analysing Hacker News Posts - A Guided Project by Data Quest*
# We will be analyzing a csv export from Hacker News posts to determine which type of posts receive more attention and comments.

import csv
import os
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

# Steps 1 of 8
FOLDER_PATH = os.getenv('FOLDER_PATH')
data = open(f'{FOLDER_PATH}hacker_news.csv')

# Reading it as a list
hn = list(csv.reader(data))

# Checking the first five rows of the list / csv
hn[:5]

## Steps 2 of 8
# extract the first row into 'headers'
headers = hn[0]

# Keep the rest of the table
hn = hn[1:]

# Print to test whether it worked
# print(headers)
# print(hn[:5])

# 3 of 8
# Return True or False if the string starts with the string passed
# print('dataquest'.startswith('Data'))
# print('dataquest'.startswith('data'))

# Converts a string into lowercase
# print('DataQuest'.lower())

# Instructions
ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)

lenght_of_all_questions = len(hn)
length_ask = len(ask_posts)
length_show = len(show_posts)
length_other = len(other_posts)
# print(len(ask_posts) + len(show_posts) + len(other_posts))

# 4 of 8
# print(ask_posts[:5])

# Calculating number of comments in ask questions (num_comments is in column 5 = index 4)
total_ask_comments = 0
for question in ask_posts:
    num_comments = int(question[4])
    total_ask_comments += num_comments

# Average comments per ask question
avg_ask_comments = total_ask_comments / length_ask
# print(avg_ask_comments)

# Calcuating number of comments in show questions
total_show_comments = 0
for question in show_posts:
    num = int(question[4])
    total_show_comments += num

avg_show_comments = total_show_comments / length_show
# print(avg_show_comments)

'''
On average, 'Ask HN' receive 4 more comments than 'Show HN' posts.
Ask HN posts receive 14 comments on average, versus 10 comments which 'Show HN' posts receive.
'''

# 5 of 8 - Focus on Ask HN questions
result_list = []

# Filtering for DateTime and Number of Comments
for post in ask_posts:
    date = post[6]
    num_comments = int(post[4])
    result_list.append([date, num_comments])


# print(result_list)

counts_by_hour = {}
comments_by_hour = {}
date_format = "%m/%d/%Y %H:%M"

for each_row in result_list:
    date = each_row[0]
    comment = each_row[1]
    time = dt.datetime.strptime(date, date_format).strftime("%H")
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

# Step 6 of 8 - Calculating the Average Number of Comments for Ask HN Posts by Hour

avg_by_hour = []

for hour in comments_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour] / counts_by_hour[hour]])

# print(avg_by_hour)

# Step 7 of 8 - Sorting and Printing Values from a List of Lists
swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

# print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)
sorted_swap = sorted_swap[:5]

print("Top 5 Hours for Ask Posts Comments")
for avg in sorted_swap:
    hour = avg[1]
    avg_comments = avg[0]
    avg_comm_new = "{:.2f}".format(avg_comments)
    time = dt.datetime.strptime(hour, "%H").strftime("%H:%M")
    print("{0}: {1} average comments per post".format(time, avg_comm_new))

'''Here are our findings:
Top 5 Hours for Ask Posts Comments
15:00: 38.59 average comments per post
02:00: 23.81 average comments per post
20:00: 21.52 average comments per post
16:00: 16.80 average comments per post
21:00: 16.01 average comments per post

Couldn't find the 'time zone' for the times in the documentation
'''

# Step 8 of 8 - Conclusion. All done.


# %%
import random
import csv
import pandas as pd

# Alphabet files with random numbers and summary

for i in range(65, 91, 1):
    with open(f'13.1/{chr(i)}.txt', mode='w') as file:
        number = random.randint(1, 100)
        file.write(f'{number}')
    with open('13.1/summary.txt', mode='a') as file:
        file.write(f'{chr(i)}.txt: {number}\n')

# Create file and dublicate with upper case content

with open('13.2/file.txt', mode='w') as file:
    file.write('“Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed\
 do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad\
 minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea\
 commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit\
 esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat\
 cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est\
 laborum”.')

with open('13.2/copy.txt', mode='w') as copy:
    with open('13.2/file.txt', mode='r') as file:
        text = file.read()
    copy.write(text.upper())

# Simulate game scores and save to CSV

header = ['Player name', 'Score']
names = ['Josh', 'Luke', 'Kate', 'Mark', 'Mary']
user_scores = []

for i in range(100):
    for j in names:
        user_scores.append([j, random.randint(0, 1000)])

with open('13.3/scores.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    for v in user_scores:
        writer.writerow(v)

# Create a file with the highest scores of players

data = pd.read_csv('13.3/scores.csv')

max_scores = data.groupby('Player name').max()
max_scores = max_scores.sort_values(by='Score', ascending=False).reset_index()

max_scores.columns = ['Player name', 'Highest score']
max_scores.to_csv('13.4/high_scores.csv', index=False)

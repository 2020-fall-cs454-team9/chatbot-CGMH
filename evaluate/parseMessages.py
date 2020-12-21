import json, sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("message", type=str, help="path to the JSON message file")
parser.add_argument("parsed", type=str, help="path to the parsed .txt file")
args = parser.parse_args()

with open(args.message) as f:
    messages = json.load(f)

#print(messages['messages'])
messages = messages['messages']

# for msg in messages:
#     print(msg)

# print()

botMessages = list(map(lambda x: x['content'], filter(lambda x: x['sender_name'] == 'Pandorabots', sorted(messages, key=lambda x: x['timestamp_ms']))))
# for msg in botsMessages:
#     print(msg)

# print()
'''
indices = [i for i, x in enumerate(botMessages) if x == "Is that a smiley face?"]

'''
indices = [15, 30, 45, 60, 75]
indices.insert(0, 0)
indices.append(len(botMessages))

print(indices)

cutMessages = []
for i in range(len(indices)-1):
    cutMessages.append(botMessages[indices[i]:indices[i+1]])

print(len(botMessages))


with open(args.parsed, 'w') as outfile:
    json.dump(cutMessages, outfile)
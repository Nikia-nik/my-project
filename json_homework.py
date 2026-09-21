import json

with open("chat.json", "r", encoding="utf-8") as file:
    messages = json.load(file)

counts = {}
for message in messages:
    name = message["from"]
    if name not in counts:
        counts[name] = 0
    counts[name] += 1
print("number of messages :")
for name in counts:
    percent = counts[name] / len(messages) * 100
    print(name, counts[name], "مایپ", round(percent, 2), "%")

 
hours = {}
for message in messages:
    hour = message["time"][:2]
    if hour not in hours:
        hours[hour] = 0
    hours[hour] += 1
busy_hour = max(hours, key=hours.get)
print("busiest hour", busy_hour, "اب", hours[busy_hour], "مایپ")

lengths = {}
for message in messages:
    name = message["from"]
    length = len(message["text"])
    if name not in lengths:
        lengths[name] = []
    lengths[name].append(length)
print("average:")
for name in lengths:
    average = sum(lengths[name]) / len(lengths[name])
    print(name, round(average, 2), "character")
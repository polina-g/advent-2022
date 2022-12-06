
file = open("data.py", "r")

data = file.readlines()
list = []

for item in data:
    item = item.replace("\n", "")
    list.append(item)

curr_max = 0
result_max = 0
for number in list:
  if number != "":
    curr_max = curr_max + int(number)

  else:
    if curr_max > result_max:
        result_max = curr_max
    curr_max = 0

print("Answer 1: {}").format(result_max)


all_sums = []

count_track = 0
for number in list:
    if number != "":
        count_track = count_track + int(number)

    else:
        all_sums.append(count_track)
        count_track = 0

all_sums.sort(reverse=True)
print("Answer 2: {}").format(sum(all_sums[:3]))

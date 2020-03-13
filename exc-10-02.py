# Open the file
f_name = input("Enter file name: ")
if len(f_name) > 0: f_name = "mbox-short.txt"

# Handle exceptional case when open the file
try:
    f_handle = open(f_name)
except:
    print('Something wrong with the file')
d_counts = dict()       # Histogram // number of emails sent by hour
d_count_sort = list()    # Use to sort the d_counts
l_timestamp = list()    # List of all sending email time by timestamp
l_hour = list()         # List of all sending email time by hour
x_busy_hour = 0         # Name of the highest number of email hour
x_count_send = 0        # Count of emails has been send by the most email sender

for line in f_handle:
    if not line.startswith("From "):
        continue
    tl_word = line.split()
    l_timestamp.append(tl_word[-2].strip("(){}<>;"))

for time in l_timestamp:
    tl_word = time.split(":")
    l_hour.append(tl_word[0])

for hour in l_hour:
    d_counts[hour] = d_counts.get(hour, 0) + 1

for hour, count in d_counts.items():
    d_count_sort.append((hour, count))

for hour, count in sorted(d_count_sort):
    print(hour, count)
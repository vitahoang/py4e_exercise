# Open the file
f_name = input("Enter file name: ")
if len(f_name) > 0: f_name = "mbox-short.txt"

# Handle exceptional case when open the file
try:
    f_handle = open(f_name)
except:
    print('Something wrong with the file')
d_counts = dict()   # Histogram of number of emails have been sent by senders
l_senders = list()  # List of all senders' email address
x_most_sender = 0   # Email address of the most email sender
x_count_send = 0    # Count of emails has been send by the most email sender

for line in f_handle:
    if not line.startswith("From "): continue
    l_word = line.split()
    l_senders.append(l_word[1].strip("(){}<>;"))

for sender in l_senders:
    d_counts[sender] = d_counts.get(sender, 0) + 1

for sender, count in d_counts.items():
    if x_most_sender is None or count > x_count_send:
        x_most_sender = sender
        x_count_send = count
print(x_most_sender, x_count_send)

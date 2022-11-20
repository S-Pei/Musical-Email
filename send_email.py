import yagmail

import pandas as pd

# Read csv with columns needed: 
# 'First Name', 'Email', 'seats'
df = pd.read_csv('musicaldata.csv')

# there must be a column name "seats", in the format of ([A-Z][number])
# ei. the first letter of the seat is an alphabet, followed by a number
# eg. G1, H12, but not AB12
df['seat_num'] = df['seats'].str[1:].astype(int)
df['seat_row'] = df['seats'].str[:1]
df = df.sort_values(by=['seat_row','seat_num'])
# print(df.to_string())

# dict = {}
# # create dict to store mapping of email to file (for testing)
# for i in df.index :
#     email = df['Email'][i]
#     seat = df['seats'][i]
#     dict[email] = f'{seat}.pdf'

# print(dict)

# Add the content of the email in a .txt file and replace with your file name in the line below
with open("youremailcontent.txt") as f:
    email_template = f.read()

yag = yagmail.SMTP(user="youremail@gmail.com", password="applicationpw")

for i in df.index :
    email = df['Email'][i]
    seat = df['seats'][i]
    first_name = df['First Name'][i]
    file = f'{seat}.pdf'
    receiver = email
    body = email_template.format(name=first_name)
    # print(body)
    yag.send(
        to=receiver,
        subject="Your Subject",
        contents=body,
        attachments=file,
    )
    print(f'Email sent to:{email}')



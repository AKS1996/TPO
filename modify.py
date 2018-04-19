import csv
import re

males = []
females = []
surnames = []
tokens = []
missed = []

# TODO Make sure names and surnames > 3 letters. Else they'll create problems


def sort_common_names():
    # reading csv file
    with open('./male_names.csv') as f:
        sorted_file = sorted(f)

    # save to a file
    with open('./male_names.csv','w') as f:
        f.writelines(sorted_file)

    with open('./female_names.csv') as f:
        sorted_file = sorted(f)

    # save to a file
    with open('./female_names.csv','w') as f:
        f.writelines(sorted_file)

    with open('./surnames.csv') as f:
        sorted_file = sorted(f)

    # save to a file
    with open('./surnames.csv','w') as f:
        f.writelines(sorted_file)


def read_common_names():
    # reading csv file
    with open('./male_names.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            males.append(row[0])

    with open('./female_names.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            females.append(row[0])

    with open('./surnames.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            surnames.append(row[0])


def read_from_csv():
    # reading csv file
    with open('./contacts.csv', 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)

        # Ignoring the headers
        next(csvreader)

        # extracting each data row one by one
        for row in csvreader:
            txt = row[2]

            txt = txt.replace('\"','')
            txt = txt.replace('\'','')
            txt = txt.replace('.com','')
            txt = txt.replace('.co','')
            txt = txt.replace('.net','')
            txt = txt.replace('.edu','')
            txt = txt.replace('gmail','')
            txt = txt.replace('.in','')
            txt = txt.replace('@',' ')
            txt = txt.replace('<','')
            txt = txt.replace('>','')
            txt = txt.replace('_',' ')
            txt = txt.replace('.',' ')

            # Replace numbers
            re.sub('\d', '', txt)

            # Lowercase
            txt = txt.lower()

            # No need of removing surname
            # for s in surnames:
            #     txt = re.sub(s,'',txt)

            # TODO Check multiple name match issue
            added = False

            for m in males:
                if m in txt:
                    tokens.append(txt)
                    added = True
                    break

            for f in females:
                if f in txt:
                    tokens.append(txt)
                    added = True
                    break

            # Print those which aint found
            if not added:
                missed.append(txt)


sort_common_names()
read_common_names()
read_from_csv()

for m in missed:
    if len(m) > 1:
        print(m)

print("Matches:",len(tokens))
print("Missed:",len(missed))
print("Male Names:",len(males),", Female Names:", len(females))

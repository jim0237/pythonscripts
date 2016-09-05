__author__ = 'jbeasley'
import csv
# the purpose of the program is to read an input file generated from skyward that is named users.csv
# Modifications are made to the file as outlined below
# The modified information is then written to an output file called skywardusers.csv
# The intention is for skyward users file to be merged with the PEIMS user file to create the main users.csv file
# that is required my MY Big Campus to create user accounts

# read in values from the users.csv input file
# rename columns in first row
    # State ID = 'unique_sis_user_id'
    # Building Code = 'unique_sis_school_id'
    # Emp Type code = 'user_type'
# insert column between State ID and First Name called "username"
# go through each row and make modifications as needed
    # if building code = '1' then change to '001'
    # if building code = '41' then change to '041'
    # username =  users email address without the @llanoisd.org
    # if Emp Type Code is TCH or COU12 or COU11 change to '2'
    # if EMP Type Code is LIB11,LIB12 change to '3'
    # if Emp Type Code is DIR12,PRI12,CFO,ADM,12-Apr,SUP12,ASU change to '4'
# all modifications are written to a file called "skywardusers.csv"
#'./DigitalEscrow/static/img/logo.jpg'


def TynkerCSV():
    with open('users.csv', 'rb') as f:
        reader = csv.reader(f)
        outfile = open('skywardusers.csv', "wb")
        writer = csv.writer(outfile)
        writer.writerow(['unique_sis_user_id', 'username', 'first_name', 'last_name',
                         'unique_sis_school_id', 'grade', 'email', 'user_type', 'password', 'authentication'])
        row_number = 0
        for row in reader:
            if row_number > 0:
                if row[3] == '1':
                    row[3] = '001'
                if row[3] == '41':
                    row[3] = '041'
                if row[3] == 'ABC  ':
                    row[3] = '001'
# strip off the white space and change the difference skyward employee codes to numeric values
                row[5] = row[5].rstrip()
                if row[5] == 'TCH':
                    row[5] = '2'
                if row[5] == 'TCH11':
                    row[5] = '2'
                if row[5] == 'TCH12':
                    row[5] = '2'
                if row[5] == 'COU12':
                    row[5] = '2'
                if row[5] == 'COU11':
                    row[5] = '2'
                if row[5] == 'LIB11':
                    row[5] = '3'
                if row[5] == 'LIB12':
                    row[5] = '3'
                if row[5] == 'DIR12':
                    row[5] = '4'
                if row[5] == 'PRI12':
                    row[5] = '4'
                if row[5] == 'CFO':
                    row[5] = '4'
                if row[5] == 'CFO12':
                    row[5] = '4'
                if row[5] == 'ADM':
                    row[5] = '4'
                if row[5] == 'ADM12':
                    row[5] = '4'
                if row[5] == '12-Apr':
                    row[5] = '4'
                if row[5] == 'SUP12':
                    row[5] = '4'
                if row[5] == 'ASU':
                    row[5] = '4'
                if row[5] == 'ASU12':
                    row[5] = '4'
                row[1] = row[1].lower() # make the first name lower case
                row[1] = row[1].rstrip(' ') # strip out the trailing spaces

                row[2] = row[2].lower() # make the last name lower case
                row[2] = row[2].rstrip(' ') # strip out the trailing spaces

                row[4] = row[4].lower() # make the email addresses lower case
                row[4] = row[4].rstrip(' ') # strip out the trailing spaces
# The next step is to create the proper user name by getting rid of the @llanoisd.org part of the email address
                username = row[4].split('@')
                username = username[0].lower()
                row.insert(1,  username) #insert a column for the username
                row.insert(5, ' ') # insert a new column and put blank in grade column
                row.insert(8, ' ') # insert a new column and put blank in password column
                row.append('0')
                writer.writerow(row)
            #print row
            row_number += 1

        outfile.close()
        f.close()

SkywardCSV()







def date_format(date):
    new_format = date[6] + date[7] + date[8] + date[9]+ '-' + date[0]+date[1]+ '-' + date[3]+date[4]
    return new_format
print(date_format('12/32/2921'))
def is_leap_year(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    return True if year%4 == 0 else False

if __name__ == '__main__':
    print(is_leap_year(300))
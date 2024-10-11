def sort_dates(dates):
    year = lambda x: (x[6:], x[0:1], x[3:4])
    
    # month = lambda x: x[0:1]
    # day = lambda x: x[3:4]
    new_dates = sorted(dates,key=year,reverse=False)
    # new_dates = sorted(dates,key=month,reverse=False)
    # new_dates = list(map(sorted(dates,key=year,reverse=False),dates))
    return new_dates
    
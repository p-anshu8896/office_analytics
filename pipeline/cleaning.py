def clean_data(att, tasks, sales):
    # fill missing values with mean
    tasks.fillna(tasks.mean(), inplace=True)
    sales.fillna(sales.mean(), inplace=True)

    att['status'] = att['status'].str.lower()

    # fix time and date formats
    att['check_in_time'] = att['check_in'].fillna('10:00')
    att['check_out'] = att['check_out'].fillna('18:00')

    return att, tasks, sales
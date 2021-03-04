def str_bt_quotations(s):
    import re
    try:
        return re.findall('"([^"]*)"', str(s))[0]
    except IndexError:
        return print('No match')


def comand_parser(comand):
    result = {
        'comand': '',
        'data': []
    }
    if comand.lower() == 'show all' or comand.lower() == 'good bye':
        result['comand'] = comand.lower()
        return result['comand'], result['data']
    data_list = comand.split(' ')
    result['comand'] = data_list[0].lower()
    result['data'] = data_list[1:]
    return result['comand'], result['data']


dict_contacts = dict()

def input_error(func):
    def inner(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except KeyError:
            return 'Wrong name'
        except IndexError:
            return 'Wrong amount values'
        except ValueError:
            return "Give me name and phone please"
    return inner

@input_error
def hello() -> str:
    return "How can I help you?"

@input_error
def add(data: list) -> None:
    if data[0] in dict_contacts:
        raise ValueError('This contact alredy exist')
    if not (data[1]).isnumeric():
        raise ValueError
    dict_contacts.update({data[0]: data[1]})

@input_error
def change(data: list) -> None:
    if not (data[1]).isnumeric():
        raise ValueError
    dict_contacts[data[0]] = data[1]

@input_error
def phone(data: list) -> str:
    return dict_contacts[data[0]]

@input_error
def show_all() -> dict:
    if not dict_contacts:
        return 'The contact list is empty'
    return dict_contacts

@input_error
def end_program():
    return 'Good bye!'

def wrong_comand():
    return 'Wrong comand!'

OPERATIONS = {
    'hello': hello,
    'add': add,
    'change': change,
    'phone': phone,
    'show all': show_all,
    'good bye': end_program,
    'close': end_program,
    'exit': end_program,
    'wrong comand': wrong_comand
}


def get_hendler(processed_comand):
    if processed_comand not in OPERATIONS:
        return OPERATIONS['wrong comand']
    return OPERATIONS[processed_comand]

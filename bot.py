import bot_handler, bot_parser


def main() -> None:
    while True:
        comand = input('Waiting comand: ')
        processed_comand, data = bot_parser.comand_parser(comand)
        if data:
            result = bot_handler.get_hendler(processed_comand)(data)
        if not data:
            result = bot_handler.get_hendler(processed_comand)()
        if type(result) is dict:
            for key, value in result.items():
                print('{:<15} {:>15}'.format(key, value))
                continue
        elif result:
            print(result)
            if result == 'Good bye!':
                break



if __name__ == '__bot__':
    print('Program start')
    main()

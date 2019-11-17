from random import randint
message_to_send = 2
def push_data(user_name):
    # check_rent_data()
    number = 1
    global message_to_send
    if message_to_send:
        message_to_send -= 1
        print('I push data to the server: {0}'.format(number))
        yield 'data: %s\n\n' % 'I am data that has been pushed to the server: {0}'.format(number)
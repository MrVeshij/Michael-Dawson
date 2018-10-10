# 1)Доработайте функцию ask_numЬer() так, чтобы ее можно было вызывать еще с одним параметром -
# кратностью (величиной шага). Сделайте шаг по умолчанию равным 1.

question = 'some text'

def  ask_number(question, low, high, step = 1):
    """Просит  ввести  число  из  диапазона."""
    response = None
    while  response  not  in  range(low, high, step):
        response = int(input(question))
    return  response

ask_number(question, 1, 10, 2)
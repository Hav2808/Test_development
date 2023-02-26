list_all = {'user1': [213, 213, 213, 15, 213],
               'user2': [54, 54, 119, 119, 119],
               'user3': [213, 98, 98, 35]}

def number_choice(dir_all: dict) -> list:
    dir_1 = dir_all
    global num_set
    checklist = []
    for key, value in dir_1.items():
        checklist = checklist + value
        res = value
        num_set = list(set(checklist))
    # print(num_set)
    num_set.sort()
    return num_set

namber_new = number_choice(list_all)
print(namber_new)


print()
print("=" * 50)

queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
def request_choice(quer: list) -> dict:
    res_dict = {}
    total_requests = len(quer)
    lens = []
    for lenght in quer:
        splitting = lenght.split(sep=' ')
        string_length = len(splitting)
        lens.append(string_length)

    lens_d = {}.fromkeys(lens, 0)
    for a in lens:
        lens_d[a] += 1
    print()
    print("Распределение количества слов в запросах:")
    print()
    for number, requests in lens_d.items():
        x = float(requests)
        percent = float(x / total_requests * 100)
        res_dict[number] = round(percent)
        print(f"Слов в запросе {number}: всего поисковых запросов {round(percent)} % ")
    print()
    print("=" * 50)
    return res_dict


request_word = request_choice(queries)
print(request_word)

stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

def channel_selection(choice: dict) -> str:
    collection = choice
    channel_selection = list(collection.items())
    channel = max(channel_selection, key=lambda i: i[1])
    return (channel[0])

#Эталоны и переменные для тестов

etalon = ['yandex']

list_test = ([
    ('facebook', 55),
    ('vk', 115),
    ('google', 99),
    ('yandex', 120)])


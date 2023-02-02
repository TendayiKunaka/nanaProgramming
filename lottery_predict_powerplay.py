# code that made me win the lottery in Harare, Zimbabwe

# Ready to win, don't forget to give me some
import pandas as pd
from collections import Counter

# Create 2 empty lists to use later
numbers_to_play = []
mega_number_to_play = []


def read_xlsx_and_convert_winning_numbs_to_list():
    filedata = pd.read_excel('C:\\Users\\TendayiKunaka\\Downloads\\africa_lotto_powerball.xlsx', 'Sheet1')

    list_of_rows = filedata.values.tolist()

    list_of_numbers = []

    for row in list_of_rows:
        for num in row:
            list_of_numbers.append(num)
    return list_of_numbers


def read_xlsx_adn_convert_megaball_nums_to_list():
    filedata = pd.read_excel('C:\\Users\\TendayiKunaka\\Downloads\\africa_lotto_bonus.xlsx', 'Sheet2')

    list_of_rows = filedata.values.tolist()

    list_of_mega_numbers = []

    for row in list_of_rows:
        for num in row:
            list_of_mega_numbers.append(num)
    return list_of_mega_numbers


def predict_future_winners(past_winners):
    counter = Counter(past_winners)
    most_common = counter.most_common(12)

    for number, count in most_common:
        number = int(number)
        numbers_to_play.append(number)
    numbers_to_play.sort()

    print('Numbers to Play: ', numbers_to_play)


def predict_future_mega_number(past_mega_numbs):
    counter = Counter(past_mega_numbs)
    most_common = counter.most_common(1)

    for number, count in most_common:
        number = int(number)
        mega_number_to_play.append(number)

    print('Mega Ball To Play: ', mega_number_to_play)


past_winners = read_xlsx_and_convert_winning_numbs_to_list()
predict_future_winners(past_winners)

past_mega_numbs = read_xlsx_adn_convert_megaball_nums_to_list()
predict_future_mega_number(past_mega_numbs)

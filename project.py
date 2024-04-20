
import pandas as pd
import random

def main():
    print('Marcin')


def excel_read(time):
    results = pd.read_excel('results.xlsx')
    time_set = time
    try:
        time_filter = results[results['time'] == time_set]
        my_columns = [column for column in time_filter.columns]
        max_index = [time_filter[column].idxmax(skipna=True) for column in my_columns]
        max = [time_filter.loc[index] for index in max_index]
    except ValueError:
        time_set = 0
        time_filter = results[results['time'] == time_set]
        my_columns = [column for column in time_filter.columns]
        max_index = [time_filter[column].idxmax(skipna=True) for column in my_columns]
        max = [time_filter.loc[index] for index in max_index]

    words_max = max[1]
    chars_max = max[2]
    keystrokes_max = max[3]
    accuracy_max = max[4]
    return words_max,chars_max,keystrokes_max,accuracy_max

def excel_write(*args):
    results = pd.read_excel('results.xlsx', sheet_name='Arkusz1', header=0)
    new_row = pd.DataFrame({'time': [args[0]],
                            'word': [args[1]],
                            'chars': [args[2]],
                            'keystrokes':[args[3]],
                            'accuracy':[args[4]],
                            'data':[args[5]],
                            'user': [args[6]]})
    with pd.ExcelWriter('results.xlsx', mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
        new_row.to_excel(writer, index=False, header=False, sheet_name='Arkusz1',
                        startrow=results.shape[0]+1)

def make_text(sec):
    with open ('word_long.txt') as long:
        list_long = random.choices(long.read().split('\n'),k=2*sec+1)
    with open ('word_medium.txt') as medium:
        list_medium = random.choices(medium.read().split('\n'),k=2*sec)
    with open ('word_short.txt') as short:
        list_short = random.choices(short.read().split('\n'),k=2*sec)
    list_of_words = list_long+list_short+list_medium
    random.shuffle(list_of_words)
    return list_of_words, len(list_of_words)



def validation(time):
    try:
        seconds = int(time)
        if seconds < 0:
            raise ValueError
    except ValueError:
        return ValueError
    else:

        return seconds
def timer_control(liczba):
    minute, secondss = divmod(liczba, 60)
    if minute < 10:
        minute_text = '0' + f'{minute}'
    else:
        minute_text = str(minute)
    if secondss < 10:
        second_text = '0' + f'{secondss}'
    else:
        second_text = str(secondss)
    return minute_text, second_text




if __name__ == '__main__':
    main()



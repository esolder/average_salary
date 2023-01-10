from hh_stat import get_hh_stat
from sj_stat import get_sj_stat
from terminaltables import SingleTable
import time
import requests
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    headers = {'X-Api-App-Id': os.environ['SUPERJOB_SECRET_KEY']}
    print(get_table(safe_connect(get_sj_stat, headers), 'SuperJob Moscow'))
    print(get_table(safe_connect(get_hh_stat), 'HeadHunter Moscow'))


def safe_connect(get_stat_func, headers=None):
    while True:
        try:
            return get_stat_func(headers)
        except requests.ConnectionError:
            print('Connection error. Retrying in 5 seconds')
            time.sleep(5)
            continue


def get_table(langs_stat, title):
    table = [('Язык программирования',
                  'Вакансий найдено',
                  'Вакансий обработано',
                  'Средняя зарплата')]

    for language, stat in langs_stat.items():
        table.append([language,
                           stat['vacancies_found'],
                           stat['vacancies_processed'],
                           stat['average_salary']])


    return SingleTable(table, title=title).table

if __name__ == '__main__':
    main()

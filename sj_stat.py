from dotenv import load_dotenv
import os
from support_funcs import predict_salary, get_langs_stat, get_langs

BASE_URL = 'https://api.superjob.ru/'
PATH = '2.0/vacancies'
PAGES = 5
MOSCOW_ID = 4
SEARCH_PERIOD = 30
MAX_COUNT_PER_PAGE = 100


def get_sj_stat(headers):
    params = {'town': MOSCOW_ID,
              'period': SEARCH_PERIOD,
              'count': MAX_COUNT_PER_PAGE}

    return get_langs_stat(BASE_URL,
                                 PATH,
                                 params,
                                 PAGES,
                                 'keyword',
                                 'objects',
                                 predict_rub_salary_sj,
                                 'total',
                                 get_langs(),
                                 headers)


def predict_rub_salary_sj(vacancy):
    if not (vacancy['payment_from'] and vacancy['payment_to']):
        return
    return predict_salary(vacancy['payment_from'], vacancy['payment_to'])


if __name__ == '__main__':
    load_dotenv()
    headers = {'X-Api-App-Id': os.environ['SUPERJOB_SECRET_KEY']}
    print(get_sj_stat(headers))

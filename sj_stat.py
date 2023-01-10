from dotenv import load_dotenv
import os
from support_funcs import predict_salary, get_vacancies_by_lang

BASE_URL = 'https://api.superjob.ru/'
PATH = '2.0/vacancies'
PAGES = 5

def get_sj_stat():
    headers = {'X-Api-App-Id': os.environ['SUPERJOB_SECRET_KEY']}

    params = {'town': 4,
              'period': 30,
              'count': 100}

    return get_vacancies_by_lang(BASE_URL,
                                 PATH,
                                 params,
                                 PAGES,
                                 'keyword',
                                 'objects',
                                 predict_rub_salary_sj,
                                 'total',
                                 headers)



def predict_rub_salary_sj(vacancy):
    if not (vacancy['payment_from'] and vacancy['payment_to']):
        return
    return predict_salary(vacancy['payment_from'], vacancy['payment_to'])


if __name__ == '__main__':
    load_dotenv()
    print(get_sj_stat())

from support_funcs import predict_salary, get_langs_stat, get_langs

BASE_URL = 'https://api.hh.ru/'
PATH = 'vacancies'
PAGES = 39
PROGRAMMER_PROF_ID = 96
MOSCOW_ID = 1
SEARCH_PERIOD = 30
MAX_COUNT_PER_PAGE = 50


def get_hh_stat(headers=None):
    params = {'professional_role': PROGRAMMER_PROF_ID,
              'area': MOSCOW_ID,
              'period': SEARCH_PERIOD,
              'per_page': MAX_COUNT_PER_PAGE}

    return get_langs_stat(BASE_URL,
                          PATH,
                          params,
                          PAGES,
                          'text',
                          'items',
                          predict_rub_salary_hh,
                          'found',
                          get_langs())


def predict_rub_salary_hh(vacancy):
    salary = vacancy['salary']
    if not salary:
        return
    if salary['currency'] != 'RUR':
        return
    return predict_salary(salary['from'], salary['to'])


if __name__ == '__main__':
    print(get_hh_stat())

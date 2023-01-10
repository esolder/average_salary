from support_funcs import predict_salary, get_vacancies_by_lang

BASE_URL = 'https://api.hh.ru/'
PATH = 'vacancies'
PAGES = 39

def get_hh_stat(headers=None):
    params = {'professional_role': 96,
              'area': 1,
              'period': 30,
              'per_page': 50}

    return get_vacancies_by_lang(BASE_URL,
                                 PATH,
                                 params,
                                 PAGES,
                                 'text',
                                 'items',
                                 predict_rub_salary_hh,
                                 'found')


def predict_rub_salary_hh(vacancy):
    salary = vacancy['salary']
    if not salary:
        return
    if salary['currency'] != 'RUR':
        return
    return predict_salary(salary['from'], salary['to'])


if __name__ == '__main__':
    print(get_hh_stat())

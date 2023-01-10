from urllib.parse import urljoin
import requests


def get_langs():
    with open('langs_list.txt', 'r', encoding='utf8') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]


def get_response(base_url, path, params=None, headers=None):
    url = urljoin(base_url, path)
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) / 2
    if salary_from:
        return salary_from * 1.2
    if salary_to:
        return salary_to * 0.8


def get_vacancies_by_lang(base_url,
                          path,
                          params,
                          pages,
                          keyword_name,
                          items_name,
                          predict_salary_func,
                          count_name,
                          headers=None):
    langs_stat = {}

    for lang in get_langs():
        params[keyword_name] = f'Программист {lang}'
        salaries = []
        langs_stat[lang] = {}

        for page in range(pages):
            params['page'] = page + 1
            
            response = get_response(base_url, path, params, headers)
            response_json = response.json()

            for vacancy in response_json[items_name]:
                vacancy_salary = predict_salary_func(vacancy)
                if vacancy_salary:
                    salaries.append(vacancy_salary)

        langs_stat[lang]['vacancies_found'] = response_json[count_name]
        salaries_count = len(salaries)
        langs_stat[lang]['vacancies_processed'] = salaries_count
        if salaries_count:
            langs_stat[lang]['average_salary'] = int(
                sum(salaries) / salaries_count)
        else:
            langs_stat[lang]['average_salary'] = 0
    
    return langs_stat

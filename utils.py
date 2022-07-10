import json


def load_candidates(file):
    """загрузит данные из файла"""
    with open(file, "r") as f:
        data = json.load(f)
        return data


def get_all(data):
    """покажет всех кандидатов"""
    main_page = []
    for people in data:
        candidates_dict = {"name": people["name"], "position": people["position"],
                           "skills": people["skills"]}
        candidates_data = f'Имя: {candidates_dict["name"]},\n' \
                          f'Позиция кандидата: {candidates_dict["position"]},\n' \
                          f'Навыки кандидата: {candidates_dict["skills"]}\n '
        main_page.append(candidates_data)
    main_page = "\n".join(main_page)
    return f'<pre>{main_page}</pre>'


def get_by_pk(pk, data):
    """вернет кандидата по pk"""
    for candidates in data:
        if candidates['pk'] == int(pk):
            return f'<img src="{candidates["picture"]}">' \
                   f'<pre>Имя: {candidates["name"]},\n' \
                   f'Позиция кандидата: {candidates["position"]},\n' \
                   f'Навыки кандидата: {candidates["skills"]}\n</pre>'


def get_by_skill(skill_name, data):
    """вернет кандидатов по навыку"""

    candidates_with_skills = []
    for candidates in data:
        skills_list = candidates['skills'].split(", ")
        lower_skills = []
        for skill in skills_list:
            lower_skills.append(skill.lower())
        if skill_name.lower() in lower_skills:
            candidates_with_skills.append(f"Имя: {candidates['name']},\nПозиция кандидата: {candidates['position']},\n"
                                          f"Навыки кандидата: {candidates['skills']}\n")
    candidates_with_skills = "\n".join(candidates_with_skills)
    return f'<pre>{candidates_with_skills}</pre>'

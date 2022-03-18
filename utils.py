import json
from settings import path


def load_candidates_from_json(path):
    """Загрузка данных из JSON файла"""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_candidates():
    """Возвращает всех кандидатов в читабельном формате"""
    candidates = load_candidates_from_json(path)
    all_candidates = ""
    for candidate in candidates:
        all_candidates += f"<strong>Имя:</strong> {candidate['name']}<br><img src={candidate['picture']}><br><strong>Вакансия:</strong> {candidate['position']}<br><strong>Пол:</strong> {candidate['gender']}<br><strong>Возраст:</strong> {candidate['age']}<br><strong>Навыки:</strong> {candidate['skills']}<br><hr><br>"
    return all_candidates


def get_candidate(candidate_id):
    """Возвращает кандидата по ID"""
    data = load_candidates_from_json(path)
    str_candidate = ""
    for d in data:
        if d["id"] == candidate_id:
            str_candidate += f"Имя: {d['name']}<br><img src={d['picture']}><br>Вакансия: {d['position']}<br>Пол:{d['gender']}<br>Возраст:{d['age']}<br>Навыки: {d['skills']}"
    return str_candidate


def get_candidates_by_name(candidate_name):
    """Возвращает кандидата(ов) по имени"""
    candidates = load_candidates_from_json(path)
    str_candidate = ""
    for candidate in candidates:
        name = candidate["name"].split()
        if candidate_name.title() == name[0]:
            str_candidate += f"Имя: {candidate['name']}<br><img src={candidate['picture']}><br>Вакансия: {candidate['position']}<br>Пол:{candidate['gender']}<br>Возраст:{candidate['age']}<br>Навыки: {candidate['skills']}<br>"
    return str_candidate


def get_candidates_by_skills(skill_name):
    """Возвращает кандидата(ов) по скилу"""
    candidates = load_candidates_from_json(path)
    str_candidate = ""
    for candidate in candidates:
        skills_str = candidate["skills"]
        skills_list = skills_str.split()
        for skill in skills_list:
            if skill_name.lower() in skill.lower():
                str_candidate += f"{candidate['name']}<br>{candidate['skills']}<br>"
    return str_candidate




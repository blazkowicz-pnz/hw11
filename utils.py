import json
from settings import path


def load_candidates_from_json(path):
    """Загрузка данных из JSON файла"""
    with open(path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

__data = load_candidates_from_json(path)
def get_candidate(candidate_id):
    """Возвращает кандидата по ID"""
    for d in __data:
        if d["id"] == candidate_id:
            return {
                "name": d["name"],
                "picture": d["picture"],
                "position": d["position"],
                "skills": d["skills"]
            }
    return {"error": "Кандидат не найден"}


def get_candidates_by_name(candidate_name):
    """Возвращает кандидата(ов) по имени"""
    return [candidate for candidate in __data if candidate_name.lower() in candidate["name"].lower()]



def get_candidates_by_skills(skill_name):
    """Возвращает кандидата(ов) по скилу"""

    candidates = []
    for candidate in __data:
        candidate["skills"]
        skills_list = candidate["skills"].lower().split(", ")
        if skill_name in skills_list:
            candidates.append(candidate)
    return candidates




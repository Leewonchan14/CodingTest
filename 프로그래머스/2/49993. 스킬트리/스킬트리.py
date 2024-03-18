import re
def solution(skill, skill_trees):
    def remove(tree):
        return re.sub(f"[^{skill}]", "", tree)
    
    return len([i for i in map(remove, skill_trees) if skill.startswith(i)])
        
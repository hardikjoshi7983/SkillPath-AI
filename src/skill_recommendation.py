def get_skill_gaps(ratings, career_requirements):
    """Return skills where the student's 0-5 rating is below the target."""
    gaps = []
    for skill, required_level in career_requirements.items():
        try:
            current = max(0, min(5, int(ratings.get(skill, 0))))
        except (TypeError, ValueError):
            current = 0
        target = max(0, min(5, int(required_level)))
        gap = max(target - current, 0)
        if gap:
            priority = "High" if gap >= 3 else "Medium" if gap == 2 else "Low"
            gaps.append({
                "skill": skill,
                "current": current,
                "required": target,
                "gap": gap,
                "priority": priority,
            })
    order = {"High": 0, "Medium": 1, "Low": 2}
    gaps.sort(key=lambda x: (order[x["priority"]], -x["gap"], x["skill"]))
    return gaps


def create_learning_roadmap(gaps):
    roadmap = []
    for index, gap in enumerate(gaps, start=1):
        roadmap.append({
            "step": index,
            "skill": gap["skill"],
            "priority": gap["priority"],
            "reason": f"Improve {gap['skill']} from {gap['current']}/5 toward the {gap['required']}/5 career target.",
        })
    return roadmap

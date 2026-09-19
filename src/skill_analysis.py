import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHART_DIR = os.path.join(BASE_DIR, "static", "charts")
os.makedirs(CHART_DIR, exist_ok=True)


def calculate_readiness(ratings, skill_requirements):
    """Calculate readiness from student ratings on a 0-5 scale."""
    skills = list(skill_requirements.keys())
    if not skills:
        return 0
    total = sum(max(0, min(5, int(ratings.get(skill, 0)))) for skill in skills)
    return round((total / (len(skills) * 5)) * 100, 1)


def create_skill_chart(ratings):
    """Create a rating-distribution pie chart for a dictionary of skill -> 0-5 rating."""
    counts = {score: 0 for score in range(6)}
    for value in ratings.values():
        try:
            score = max(0, min(5, int(value)))
        except (TypeError, ValueError):
            score = 0
        counts[score] += 1

    labels = [str(score) for score in range(6) if counts[score] > 0]
    values = [counts[score] for score in range(6) if counts[score] > 0]

    plt.figure(figsize=(7, 7))
    if values:
        plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    else:
        plt.pie([1], labels=["No ratings"], startangle=90)
    plt.title("Self-Rating Distribution (0-5)")
    plt.tight_layout()

    chart_path = os.path.join(CHART_DIR, "skill_distribution.png")
    plt.savefig(chart_path, dpi=150, bbox_inches="tight")
    plt.close()
    return "/static/charts/skill_distribution.png"

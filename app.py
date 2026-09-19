from flask import Flask, render_template, request, redirect, url_for, session
from datetime import datetime

from src.resource_recommendation import get_resources

app = Flask(__name__)
app.secret_key = "skillpath-ai-secret-key"


@app.context_processor
def inject_template_defaults():
    return {
        "profile": session.get("profile", {}),
        "now": datetime.now(),
    }


# ============================================================
# CAREERS (24 across 8 domains)
# ============================================================
CAREER_SKILLS = {
    "Machine Learning Engineer": [
        "Python", "SQL", "Statistics", "Machine Learning", "Pandas & NumPy",
        "Data Visualization", "Scikit-learn", "Git & GitHub", "Deep Learning",
        "Model Deployment"
    ],
    "Data Scientist": [
        "Python", "SQL", "Statistics", "Machine Learning", "Pandas & NumPy",
        "Data Visualization", "Scikit-learn", "Feature Engineering", "Data Cleaning",
        "Git & GitHub"
    ],
    "AI Engineer": [
        "Python", "NumPy", "Pandas", "Machine Learning", "Deep Learning",
        "PyTorch", "Computer Vision", "NLP", "Git", "Docker"
    ],
    "NLP Engineer": [
        "Python", "Machine Learning", "Deep Learning", "NLP", "Transformers",
        "PyTorch", "Statistics", "Git & GitHub", "Model Deployment", "Data Cleaning"
    ],
    "Computer Vision Engineer": [
        "Python", "NumPy", "OpenCV", "Machine Learning", "Deep Learning",
        "PyTorch", "Computer Vision", "Git & GitHub", "Model Deployment", "Data Cleaning"
    ],
    "MLOps Engineer": [
        "Python", "Machine Learning", "Docker", "Kubernetes", "Git & GitHub",
        "CI/CD", "AWS", "FastAPI", "Model Deployment", "Linux"
    ],
    "Data Analyst": [
        "Excel", "SQL", "Python", "Statistics", "Power BI", "Data Visualization",
        "Pandas", "Data Cleaning", "Business Analysis", "Communication"
    ],
    "Data Engineer": [
        "Python", "SQL", "Pandas & NumPy", "ETL", "Data Warehousing",
        "Apache Spark", "Docker", "Git & GitHub", "Linux", "Data Cleaning"
    ],
    "Business Analyst": [
        "Excel", "SQL", "Statistics", "Data Visualization", "Power BI",
        "Business Analysis", "Communication", "Data Cleaning", "Pandas", "Tableau"
    ],
    "BI Developer": [
        "SQL", "Power BI", "Tableau", "Excel", "Data Warehousing",
        "ETL", "Data Visualization", "Python", "Business Analysis", "Communication"
    ],
    "Frontend Developer": [
        "HTML", "CSS", "JavaScript", "React", "Git & GitHub", "Responsive Design",
        "UI/UX", "APIs", "Debugging", "Web Performance"
    ],
    "Backend Developer": [
        "Python", "SQL", "Flask", "REST APIs", "Git & GitHub", "Databases",
        "Authentication", "Debugging", "Data Structures", "Deployment"
    ],
    "Full Stack Developer": [
        "HTML", "CSS", "JavaScript", "React", "Python", "SQL",
        "REST APIs", "Git & GitHub", "Databases", "Deployment"
    ],
    "Software Engineer": [
        "Python", "Data Structures", "Algorithms", "OOP", "SQL",
        "Git & GitHub", "Testing", "System Design", "Debugging", "Communication"
    ],
    "Python Developer": [
        "Python", "SQL", "Git & GitHub", "Flask", "REST APIs",
        "OOP", "Testing", "Docker", "Data Structures", "Debugging"
    ],
    "Cloud Engineer": [
        "Linux", "Networking", "AWS", "Docker", "Kubernetes",
        "Python", "Git & GitHub", "Terraform", "CI/CD", "Deployment"
    ],
    "DevOps Engineer": [
        "Linux", "Git & GitHub", "Docker", "Kubernetes", "CI/CD",
        "AWS", "Python", "Terraform", "Networking", "Deployment"
    ],
    "Cybersecurity Analyst": [
        "Networking", "Linux", "Cybersecurity", "Python", "Cryptography",
        "Web Security", "SIEM", "Incident Response", "Git & GitHub", "Communication"
    ],
    "UI/UX Designer": [
        "UI Design", "UX Research", "Figma", "Wireframing", "Prototyping",
        "User Research", "Typography", "Color Theory", "Design Systems",
        "Usability Testing"
    ],
    "Product Designer": [
        "UI Design", "UX Research", "Figma", "Prototyping", "Design Systems",
        "User Research", "Wireframing", "Usability Testing", "Typography", "Communication"
    ],
    "Product Analyst": [
        "SQL", "Python", "Statistics", "Excel", "Data Visualization",
        "Product Analytics", "A/B Testing", "Communication", "Business Analysis", "Power BI"
    ],
    "Product Manager": [
        "Product Analytics", "Business Analysis", "Communication", "SQL",
        "Data Visualization", "A/B Testing", "Excel", "Statistics", "UX Research", "Git & GitHub"
    ],
    "Database Administrator": [
        "SQL", "PostgreSQL", "MySQL", "Linux", "Database Administration",
        "Backup and Recovery", "Database Security", "Networking", "Python", "Git & GitHub"
    ],
}

REQUIRED_LEVELS = {
    "Machine Learning Engineer": {"Python": 4, "SQL": 3, "Statistics": 4, "Machine Learning": 5, "Pandas & NumPy": 4, "Data Visualization": 3, "Scikit-learn": 4, "Git & GitHub": 3, "Deep Learning": 3, "Model Deployment": 3},
    "Data Scientist": {"Python": 4, "SQL": 4, "Statistics": 5, "Machine Learning": 4, "Pandas & NumPy": 4, "Data Visualization": 4, "Scikit-learn": 4, "Feature Engineering": 4, "Data Cleaning": 4, "Git & GitHub": 3},
    "AI Engineer": {"Python": 5, "NumPy": 4, "Pandas": 4, "Machine Learning": 5, "Deep Learning": 5, "PyTorch": 5, "Computer Vision": 4, "NLP": 4, "Git": 4, "Docker": 4},
    "NLP Engineer": {"Python": 5, "Machine Learning": 5, "Deep Learning": 5, "NLP": 5, "Transformers": 5, "PyTorch": 4, "Statistics": 4, "Git & GitHub": 4, "Model Deployment": 4, "Data Cleaning": 4},
    "Computer Vision Engineer": {"Python": 5, "NumPy": 4, "OpenCV": 5, "Machine Learning": 5, "Deep Learning": 5, "PyTorch": 5, "Computer Vision": 5, "Git & GitHub": 4, "Model Deployment": 4, "Data Cleaning": 4},
    "MLOps Engineer": {"Python": 5, "Machine Learning": 5, "Docker": 5, "Kubernetes": 5, "Git & GitHub": 5, "CI/CD": 5, "AWS": 4, "FastAPI": 4, "Model Deployment": 5, "Linux": 4},
    "Data Analyst": {"Excel": 4, "SQL": 4, "Python": 3, "Statistics": 4, "Power BI": 4, "Data Visualization": 4, "Pandas": 3, "Data Cleaning": 4, "Business Analysis": 4, "Communication": 4},
    "Data Engineer": {"Python": 5, "SQL": 5, "Pandas & NumPy": 4, "ETL": 5, "Data Warehousing": 5, "Apache Spark": 4, "Docker": 4, "Git & GitHub": 4, "Linux": 4, "Data Cleaning": 4},
    "Business Analyst": {"Excel": 5, "SQL": 4, "Statistics": 4, "Data Visualization": 4, "Power BI": 4, "Business Analysis": 5, "Communication": 5, "Data Cleaning": 4, "Pandas": 3, "Tableau": 4},
    "BI Developer": {"SQL": 5, "Power BI": 5, "Tableau": 5, "Excel": 4, "Data Warehousing": 4, "ETL": 4, "Data Visualization": 5, "Python": 3, "Business Analysis": 4, "Communication": 4},
    "Frontend Developer": {"HTML": 5, "CSS": 5, "JavaScript": 5, "React": 4, "Git & GitHub": 3, "Responsive Design": 4, "UI/UX": 4, "APIs": 3, "Debugging": 4, "Web Performance": 3},
    "Backend Developer": {"Python": 4, "SQL": 4, "Flask": 4, "REST APIs": 5, "Git & GitHub": 3, "Databases": 4, "Authentication": 4, "Debugging": 4, "Data Structures": 4, "Deployment": 3},
    "Full Stack Developer": {"HTML": 4, "CSS": 4, "JavaScript": 5, "React": 4, "Python": 4, "SQL": 4, "REST APIs": 5, "Git & GitHub": 4, "Databases": 4, "Deployment": 3},
    "Software Engineer": {"Python": 4, "Data Structures": 5, "Algorithms": 5, "OOP": 5, "SQL": 4, "Git & GitHub": 4, "Testing": 4, "System Design": 4, "Debugging": 4, "Communication": 4},
    "Python Developer": {"Python": 5, "SQL": 4, "Git & GitHub": 4, "Flask": 4, "REST APIs": 4, "OOP": 5, "Testing": 4, "Docker": 3, "Data Structures": 4, "Debugging": 4},
    "Cloud Engineer": {"Linux": 5, "Networking": 5, "AWS": 5, "Docker": 5, "Kubernetes": 4, "Python": 3, "Git & GitHub": 4, "Terraform": 4, "CI/CD": 4, "Deployment": 4},
    "DevOps Engineer": {"Linux": 5, "Git & GitHub": 5, "Docker": 5, "Kubernetes": 5, "CI/CD": 5, "AWS": 4, "Python": 4, "Terraform": 4, "Networking": 4, "Deployment": 5},
    "Cybersecurity Analyst": {"Networking": 5, "Linux": 5, "Cybersecurity": 5, "Python": 3, "Cryptography": 4, "Web Security": 4, "SIEM": 4, "Incident Response": 5, "Git & GitHub": 3, "Communication": 4},
    "UI/UX Designer": {"UI Design": 5, "UX Research": 4, "Figma": 5, "Wireframing": 5, "Prototyping": 4, "User Research": 4, "Typography": 4, "Color Theory": 4, "Design Systems": 4, "Usability Testing": 4},
    "Product Designer": {"UI Design": 5, "UX Research": 5, "Figma": 5, "Prototyping": 5, "Design Systems": 5, "User Research": 4, "Wireframing": 4, "Usability Testing": 4, "Typography": 4, "Communication": 4},
    "Product Analyst": {"SQL": 5, "Python": 4, "Statistics": 5, "Excel": 4, "Data Visualization": 5, "Product Analytics": 5, "A/B Testing": 4, "Communication": 4, "Business Analysis": 4, "Power BI": 4},
    "Product Manager": {"Product Analytics": 5, "Business Analysis": 5, "Communication": 5, "SQL": 4, "Data Visualization": 4, "A/B Testing": 4, "Excel": 4, "Statistics": 4, "UX Research": 4, "Git & GitHub": 3},
    "Database Administrator": {"SQL": 5, "PostgreSQL": 5, "MySQL": 5, "Linux": 4, "Database Administration": 5, "Backup and Recovery": 5, "Database Security": 4, "Networking": 4, "Python": 3, "Git & GitHub": 3},
}

CAREER_CATEGORIES = {
    "AI & Machine Learning": ["Machine Learning Engineer", "Data Scientist", "AI Engineer", "NLP Engineer", "Computer Vision Engineer", "MLOps Engineer"],
    "Data & Analytics": ["Data Analyst", "Data Engineer", "Business Analyst", "BI Developer"],
    "Web & Software": ["Frontend Developer", "Backend Developer", "Full Stack Developer", "Software Engineer", "Python Developer"],
    "Cloud & DevOps": ["Cloud Engineer", "DevOps Engineer"],
    "Cybersecurity": ["Cybersecurity Analyst"],
    "Design": ["UI/UX Designer", "Product Designer"],
    "Product & Management": ["Product Analyst", "Product Manager"],
    "Database": ["Database Administrator"],
}

DEGREES = [
    "Diploma", "B.Tech", "B.E", "BCA", "B.Sc", "B.Com", "BBA",
    "M.Tech", "MCA", "M.Sc", "MBA", "M.Com", "Other"
]

# Flat, HTML-only specialization choices grouped with <optgroup>
SPECIALIZATION_GROUPS = {
    "Engineering (B.Tech / B.E)": [
        "Computer Science & Engineering", "Information Technology",
        "AI & Machine Learning", "Data Science", "Electronics & Communication",
        "Electrical & Electronics", "Mechanical Engineering", "Civil Engineering",
        "Chemical Engineering", "Aerospace Engineering",
    ],
    "Computer Applications (BCA / MCA)": [
        "Computer Applications", "Data Science", "Cloud Computing",
        "Cyber Security", "AI & ML",
    ],
    "Science (B.Sc / M.Sc)": [
        "Computer Science", "Information Technology", "Data Science",
        "Mathematics", "Statistics", "Physics", "Chemistry", "Biotechnology",
    ],
    "Commerce (B.Com / M.Com)": [
        "General", "Computer Applications", "Finance", "Accounting",
    ],
    "Business (BBA / MBA)": [
        "General", "Business Analytics", "Digital Marketing", "Finance",
        "Marketing", "HR", "Operations",
    ],
    "Postgraduate Engineering (M.Tech)": [
        "Computer Science & Engineering", "AI & Machine Learning",
        "Data Science", "Cyber Security", "VLSI Design", "Structural Engineering",
    ],
    "Diploma": [
        "Computer Engineering", "Mechanical", "Electrical", "Civil", "Electronics",
    ],
    "Other": ["Other"],
}


# ============================================================
# HELPERS
# ============================================================
def clamp_score(value):
    try:
        return max(0, min(5, int(value)))
    except (TypeError, ValueError):
        return 0


def readiness_message(score):
    if score >= 85:
        return "Excellent readiness. Keep strengthening your skills with real-world projects."
    if score >= 70:
        return "Good progress. Focus on the remaining gaps to become career-ready."
    if score >= 50:
        return "You have a solid starting point. Prioritize the highlighted skill gaps next."
    if score >= 30:
        return "You are building your foundation. Work through the high-priority gaps first."
    return "Start with the fundamentals and follow the roadmap one skill at a time."


def readiness_level(score):
    if score >= 85: return "Excellent"
    if score >= 70: return "Career Ready"
    if score >= 50: return "Developing"
    if score >= 30: return "Early Stage"
    return "Beginner"


def readiness_tier(score):
    if score >= 85: return "tier-excellent"
    if score >= 70: return "tier-ready"
    if score >= 50: return "tier-developing"
    if score >= 30: return "tier-early"
    return "tier-beginner"


def build_pie_style(ratings):
    counts = {score: 0 for score in range(6)}
    for value in ratings.values():
        counts[clamp_score(value)] += 1

    total = sum(counts.values())
    if total == 0:
        return "conic-gradient(#e7edf5 0 100%)"

    colors = ["#cbd5e1", "#ef4444", "#f59e0b", "#facc15", "#14b8a6", "#2563eb"]
    stops = []
    current = 0.0

    for score in range(6):
        if counts[score] == 0:
            continue
        start = current
        current += (counts[score] / total) * 100
        stops.append(f"{colors[score]} {start:.2f}% {current:.2f}%")

    return "conic-gradient(" + ", ".join(stops) + ")"


def estimate_hours(gap):
    return {0: 0, 1: 10, 2: 25, 3: 45, 4: 70}.get(gap, gap * 20)


# ============================================================
# ROUTES
# ============================================================
@app.route("/")
def index():
    return render_template(
        "index.html",
        career_count=len(CAREER_SKILLS),
        skill_count=len({s for skills in CAREER_SKILLS.values() for s in skills}),
        category_count=len(CAREER_CATEGORIES),
        career_categories=CAREER_CATEGORIES,   # <-- add this line
    )


@app.route("/profile", methods=["GET", "POST"])
def profile():
    saved_profile = session.get("profile", {})
    error = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        degree = request.form.get("degree", "").strip()
        course = request.form.get("course", "").strip()
        year = request.form.get("year", "").strip()
        career = request.form.get("career", "").strip()

        if not name or not email or not degree or not course or not career or not year:
            error = "Please complete all required fields."
            saved_profile = {
                "name": name, "email": email, "degree": degree,
                "course": course, "career": career, "year": year,
            }
        elif career not in CAREER_SKILLS:
            error = "Please select a valid target career."
        else:
            old_career = session.get("profile", {}).get("career")
            session["profile"] = {
                "name": name, "email": email, "degree": degree,
                "course": course, "career": career, "year": year,
            }
            if old_career != career:
                session["ratings"] = {}
            elif "ratings" not in session:
                session["ratings"] = {}
            session.modified = True
            return redirect(url_for("skills"))

    return render_template(
        "profile.html",
        profile=saved_profile,
        degrees=DEGREES,
        specialization_groups=SPECIALIZATION_GROUPS,
        career_categories=CAREER_CATEGORIES,
        error=error,
    )


@app.route("/skills", methods=["GET", "POST"])
def skills():
    profile_data = session.get("profile")
    if not profile_data:
        return redirect(url_for("profile"))

    career = profile_data.get("career", "")
    skills_list = CAREER_SKILLS.get(career, [])
    ratings = {skill: clamp_score(score) for skill, score in session.get("ratings", {}).items()}
    error = None

    if request.method == "POST":
        new_ratings = {}
        missing = []
        for skill in skills_list:
            raw = request.form.get(skill)
            if raw is None or raw == "":
                missing.append(skill)
                new_ratings[skill] = 0
            else:
                new_ratings[skill] = clamp_score(raw)

        if missing:
            error = "Please rate every skill before continuing."
            ratings = new_ratings
        else:
            session["ratings"] = new_ratings
            session.modified = True
            return redirect(url_for("analysis"))

    return render_template(
        "skills.html",
        profile=profile_data,
        career=career,
        skills=skills_list,
        ratings=ratings,
        required=REQUIRED_LEVELS.get(career, {}),
        error=error,
    )


@app.route("/analysis")
def analysis():
    profile_data = session.get("profile")
    if not profile_data:
        return redirect(url_for("profile"))

    career = profile_data.get("career", "")
    skills_list = CAREER_SKILLS.get(career, [])
    ratings = session.get("ratings", {})

    if not skills_list or any(skill not in ratings for skill in skills_list):
        return redirect(url_for("skills"))

    required = REQUIRED_LEVELS.get(career, {})
    results, strong_skills, gap_skills, high_priority = [], [], [], []
    total_score = 0

    for skill in skills_list:
        current = clamp_score(ratings.get(skill, 0))
        target = clamp_score(required.get(skill, 3))
        gap = max(target - current, 0)
        percentage = current * 20

        if current >= 4:
            level = "Strong"
        elif current >= 2:
            level = "Developing"
        else:
            level = "Needs Improvement"

        if gap == 0:
            status = "On Track"
        elif gap == 1:
            status = "Small Gap"
        elif gap == 2:
            status = "Medium Gap"
        else:
            status = "High Priority"

        item = {
            "skill": skill, "current": current, "required": target,
            "gap": gap, "percentage": percentage, "level": level,
            "status": status, "hours": estimate_hours(gap),
        }
        results.append(item)
        total_score += current
        if current >= 4: strong_skills.append(item)
        if gap > 0: gap_skills.append(item)
        if gap >= 2: high_priority.append(item)

    maximum_score = len(skills_list) * 5
    overall_score = round((total_score / maximum_score) * 100) if maximum_score else 0
    level = readiness_level(overall_score)
    tier = readiness_tier(overall_score)
    message = readiness_message(overall_score)
    ml_confidence = min(98, max(60, 60 + round(overall_score * 0.38)))
    rating_distribution = {score: list(ratings.values()).count(score) for score in range(6)}
    gap_skills.sort(key=lambda x: (x["gap"], x["required"]), reverse=True)
    high_priority.sort(key=lambda x: (x["gap"], x["required"]), reverse=True)
    total_hours = sum(item["hours"] for item in gap_skills)
    estimated_weeks = max(1, round(total_hours / 10)) if total_hours else 0

    return render_template(
        "analysis.html",
        profile=profile_data, career=career, ratings=ratings, results=results,
        overall_score=overall_score, maximum_score=maximum_score, total_score=total_score,
        level=level, tier=tier, message=message, ml_confidence=ml_confidence,
        strong_skills=strong_skills, gap_skills=gap_skills, high_priority=high_priority,
        pie_style=build_pie_style(ratings), rating_distribution=rating_distribution,
        total_hours=total_hours, estimated_weeks=estimated_weeks,
    )


@app.route("/roadmap")
def roadmap():
    profile_data = session.get("profile")
    if not profile_data:
        return redirect(url_for("profile"))

    career = profile_data.get("career", "")
    ratings = session.get("ratings", {})
    required = REQUIRED_LEVELS.get(career, {})

    if not all(skill in ratings for skill in CAREER_SKILLS.get(career, [])):
        return redirect(url_for("skills"))

    roadmap_items = []
    for skill in CAREER_SKILLS.get(career, []):
        current = clamp_score(ratings.get(skill, 0))
        target = clamp_score(required.get(skill, 3))
        gap = max(target - current, 0)
        if gap == 0:
            continue

        if gap >= 3:
            priority = "High"
            recommendation = f"Build your {skill} foundation with structured courses and at least two hands-on projects before moving to advanced work."
        elif gap == 2:
            priority = "Medium"
            recommendation = f"Strengthen {skill} with guided practice, a focused mini-project, and code reviews."
        else:
            priority = "Low"
            recommendation = f"Polish your {skill} knowledge with targeted practice and one small real-world project."

        roadmap_items.append({
            "name": skill, "skill": skill, "current": current, "required": target,
            "gap": gap, "priority": priority, "recommendation": recommendation,
            "progress": current * 20, "hours": estimate_hours(gap),
            "resources": get_resources([skill]),
        })

    priority_order = {"High": 0, "Medium": 1, "Low": 2}
    roadmap_items.sort(key=lambda x: (priority_order[x["priority"]], -x["gap"], x["name"]))
    total_hours = sum(item["hours"] for item in roadmap_items)

    return render_template(
        "roadmap.html", profile=profile_data, career=career,
        roadmap=roadmap_items, total_hours=total_hours,
    )


@app.route("/reset")
def reset():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
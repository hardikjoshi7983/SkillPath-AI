import os
import random
import numpy as np
import pandas as pd


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_DIR = os.path.join(BASE_DIR, "data")

os.makedirs(DATA_DIR, exist_ok=True)


# ============================================================
# CAREERS AND REQUIRED SKILLS
# ============================================================

CAREER_SKILLS = {

    "Machine Learning Engineer": {
        "Python": 5,
        "NumPy": 4,
        "Pandas": 4,
        "Statistics": 5,
        "Machine Learning": 5,
        "Scikit-learn": 5,
        "SQL": 4,
        "Git": 3,
        "Docker": 3,
        "FastAPI": 3
    },

    "Data Scientist": {
        "Python": 5,
        "SQL": 4,
        "Statistics": 5,
        "Pandas": 5,
        "NumPy": 4,
        "Machine Learning": 5,
        "Data Visualization": 4,
        "Scikit-learn": 4,
        "Git": 3
    },

    "Data Analyst": {
        "SQL": 5,
        "Excel": 5,
        "Python": 4,
        "Pandas": 4,
        "Statistics": 4,
        "Data Visualization": 5,
        "Power BI": 5,
        "Tableau": 4,
        "Git": 2
    },

    "AI Engineer": {
        "Python": 5,
        "NumPy": 4,
        "Pandas": 4,
        "Machine Learning": 5,
        "Deep Learning": 5,
        "PyTorch": 5,
        "Computer Vision": 4,
        "NLP": 4,
        "Git": 4,
        "Docker": 4
    },

    "Backend Developer": {
        "Python": 5,
        "SQL": 5,
        "Git": 4,
        "FastAPI": 5,
        "REST API": 5,
        "Docker": 4,
        "Linux": 4,
        "PostgreSQL": 5
    },

    "Python Developer": {
        "Python": 5,
        "SQL": 4,
        "Git": 4,
        "FastAPI": 4,
        "REST API": 4,
        "OOP": 5,
        "Testing": 4,
        "Docker": 3
    },

    "Full Stack Developer": {
        "Python": 4,
        "HTML": 4,
        "CSS": 4,
        "JavaScript": 5,
        "SQL": 4,
        "REST API": 5,
        "Git": 4,
        "Docker": 3
    },

    "Software Engineer": {
        "Python": 4,
        "Data Structures": 5,
        "Algorithms": 5,
        "OOP": 5,
        "SQL": 4,
        "Git": 4,
        "Testing": 4,
        "System Design": 4
    },

    "Data Engineer": {
        "Python": 5,
        "SQL": 5,
        "Pandas": 4,
        "ETL": 5,
        "Data Warehousing": 5,
        "Apache Spark": 4,
        "Docker": 4,
        "Git": 4,
        "Linux": 4
    },

    "Cloud Engineer": {
        "Linux": 5,
        "Networking": 5,
        "AWS": 5,
        "Docker": 5,
        "Kubernetes": 4,
        "Python": 3,
        "Git": 4,
        "Terraform": 4
    },

    "DevOps Engineer": {
        "Linux": 5,
        "Git": 5,
        "Docker": 5,
        "Kubernetes": 5,
        "CI/CD": 5,
        "AWS": 4,
        "Python": 4,
        "Terraform": 4
    },

    "Cybersecurity Analyst": {
        "Networking": 5,
        "Linux": 5,
        "Cybersecurity": 5,
        "Python": 3,
        "Cryptography": 4,
        "Web Security": 4,
        "SIEM": 4,
        "Incident Response": 5
    },

    "Business Analyst": {
        "Excel": 5,
        "SQL": 4,
        "Statistics": 4,
        "Data Visualization": 4,
        "Power BI": 4,
        "Business Analysis": 5,
        "Communication": 5
    },

    "Product Analyst": {
        "SQL": 5,
        "Python": 4,
        "Statistics": 5,
        "Excel": 4,
        "Data Visualization": 5,
        "Product Analytics": 5,
        "A/B Testing": 4
    },

    "BI Developer": {
        "SQL": 5,
        "Power BI": 5,
        "Tableau": 5,
        "Excel": 4,
        "Data Warehousing": 4,
        "ETL": 4,
        "Data Visualization": 5
    },

    "Computer Vision Engineer": {
        "Python": 5,
        "NumPy": 4,
        "OpenCV": 5,
        "Machine Learning": 5,
        "Deep Learning": 5,
        "PyTorch": 5,
        "Computer Vision": 5,
        "Git": 4
    },

    "NLP Engineer": {
        "Python": 5,
        "Machine Learning": 4,
        "Deep Learning": 5,
        "NLP": 5,
        "Transformers": 5,
        "PyTorch": 4,
        "Statistics": 4,
        "Git": 4
    },

    "AI/ML Researcher": {
        "Python": 5,
        "Statistics": 5,
        "Linear Algebra": 5,
        "Calculus": 2,
        "Machine Learning": 3,
        "Deep Learning": 5,
        "PyTorch": 5,
        "Research": 5
    },

    "Database Administrator": {
        "SQL": 5,
        "PostgreSQL": 5,
        "MySQL": 5,
        "Linux": 4,
        "Database Administration": 5,
        "Backup and Recovery": 5,
        "Database Security": 4
    },

    "MLOps Engineer": {
        "Python": 5,
        "Machine Learning": 5,
        "Docker": 5,
        "Kubernetes": 5,
        "Git": 5,
        "CI/CD": 5,
        "AWS": 4,
        "FastAPI": 4
    }
}


# ============================================================
# ALL SKILLS
# ============================================================

SKILL_CATEGORIES = {

    "Python": "Programming",
    "NumPy": "Data Science",
    "Pandas": "Data Science",
    "Statistics": "Mathematics",
    "Machine Learning": "AI/ML",
    "Scikit-learn": "AI/ML",
    "SQL": "Database",
    "Git": "Tools",
    "Docker": "DevOps",
    "FastAPI": "Backend",

    "Data Visualization": "Data Science",
    "Excel": "Analytics",
    "Power BI": "Analytics",
    "Tableau": "Analytics",

    "Deep Learning": "AI/ML",
    "PyTorch": "AI/ML",
    "Computer Vision": "AI/ML",
    "OpenCV": "AI/ML",
    "NLP": "AI/ML",
    "Transformers": "AI/ML",

    "REST API": "Backend",
    "Linux": "Tools",
    "PostgreSQL": "Database",
    "MySQL": "Database",

    "OOP": "Programming",
    "Testing": "Software Development",
    "Data Structures": "Computer Science",
    "Algorithms": "Computer Science",
    "System Design": "Software Development",

    "ETL": "Data Engineering",
    "Data Warehousing": "Data Engineering",
    "Apache Spark": "Data Engineering",

    "Networking": "Cybersecurity",
    "Cybersecurity": "Cybersecurity",
    "Cryptography": "Cybersecurity",
    "Web Security": "Cybersecurity",
    "SIEM": "Cybersecurity",
    "Incident Response": "Cybersecurity",

    "AWS": "Cloud",
    "Kubernetes": "DevOps",
    "Terraform": "DevOps",
    "CI/CD": "DevOps",

    "Business Analysis": "Business",
    "Communication": "Soft Skills",
    "Product Analytics": "Analytics",
    "A/B Testing": "Analytics",

    "Database Administration": "Database",
    "Backup and Recovery": "Database",
    "Database Security": "Database",

    "Research": "Research",
    "Linear Algebra": "Mathematics",
    "Calculus": "Mathematics"
}


# ============================================================
# CREATE CAREER DATASET
# ============================================================

def create_career_skills():

    rows = []

    for career, skills in CAREER_SKILLS.items():

        for skill, required_level in skills.items():

            rows.append({
                "career": career,
                "skill": skill,
                "required_level": required_level
            })

    df = pd.DataFrame(rows)

    df.to_csv(
        os.path.join(
            DATA_DIR,
            "career_skills.csv"
        ),
        index=False
    )

    return df


# ============================================================
# CREATE SKILLS DATASET
# ============================================================

def create_skills():

    rows = []

    for skill, category in SKILL_CATEGORIES.items():

        rows.append({
            "skill": skill,
            "category": category
        })

    df = pd.DataFrame(rows)

    df.to_csv(
        os.path.join(
            DATA_DIR,
            "skills.csv"
        ),
        index=False
    )

    return df


# ============================================================
# CREATE SYNTHETIC ML DATA
#
# IMPORTANT:
# No study hours.
# No assessment score.
#
# Features:
# course
# year
# skill
# self_rating
# projects_completed
# ============================================================

def create_training_data(n_samples=5000):

    courses = [

        "B.Tech CSE",
        "B.Tech IT",
        "B.Tech AI & ML",
        "B.Tech Data Science",
        "B.Tech ECE",
        "B.Tech EEE",
        "B.Tech Mechanical",
        "B.Tech Civil",

        "BCA",
        "B.Sc Computer Science",
        "B.Sc Information Technology",
        "B.Sc Data Science",
        "B.Sc Mathematics",
        "B.Sc Statistics",

        "MCA",
        "M.Tech",
        "M.Sc Computer Science",
        "M.Sc Data Science",
        "M.Sc Statistics",

        "MBA",
        "BBA",
        "B.Com"
    ]

    skills = list(SKILL_CATEGORIES.keys())

    rows = []

    for _ in range(n_samples):

        course = random.choice(courses)

        year = random.randint(1, 4)

        skill = random.choice(skills)

        self_rating = random.randint(1, 5)

        projects_completed = random.randint(
            0,
            6
        )

        # Synthetic target generation.
        # This creates a realistic relationship between
        # self-rating and project experience.

        score = (
            self_rating * 15
            + projects_completed * 5
            + np.random.normal(0, 7)
        )

        if score < 35:

            level = "Beginner"

        elif score < 65:

            level = "Intermediate"

        else:

            level = "Advanced"

        rows.append({

            "course": course,

            "year": year,

            "skill": skill,

            "self_rating": self_rating,

            "projects_completed": projects_completed,

            "level": level
        })

    df = pd.DataFrame(rows)

    df.to_csv(
        os.path.join(
            DATA_DIR,
            "training_data.csv"
        ),
        index=False
    )

    return df


# ============================================================
# LEARNING RESOURCES
# ============================================================

def create_learning_resources():

    resources = [

        {
            "skill": "Python",
            "channel": "freeCodeCamp.org",
            "title": "Python Programming",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "Machine Learning",
            "channel": "Krish Naik",
            "title": "Machine Learning Tutorials",
            "url": "https://www.youtube.com/@krishnaik06"
        },

        {
            "skill": "Machine Learning",
            "channel": "CampusX",
            "title": "Machine Learning Tutorials",
            "url": "https://www.youtube.com/@campusx-official"
        },

        {
            "skill": "Statistics",
            "channel": "StatQuest with Josh Starmer",
            "title": "Statistics Tutorials",
            "url": "https://www.youtube.com/@statquest"
        },

        {
            "skill": "SQL",
            "channel": "freeCodeCamp.org",
            "title": "SQL Tutorials",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "Pandas",
            "channel": "Corey Schafer",
            "title": "Pandas Tutorials",
            "url": "https://www.youtube.com/@coreyms"
        },

        {
            "skill": "Git",
            "channel": "freeCodeCamp.org",
            "title": "Git and GitHub",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "Docker",
            "channel": "TechWorld with Nana",
            "title": "Docker Tutorials",
            "url": "https://www.youtube.com/@TechWorldwithNana"
        },

        {
            "skill": "Power BI",
            "channel": "Guy in a Cube",
            "title": "Power BI Tutorials",
            "url": "https://www.youtube.com/@GuyInACube"
        },

        {
            "skill": "Deep Learning",
            "channel": "freeCodeCamp.org",
            "title": "Deep Learning Tutorials",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "PyTorch",
            "channel": "freeCodeCamp.org",
            "title": "PyTorch Tutorials",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "FastAPI",
            "channel": "freeCodeCamp.org",
            "title": "FastAPI Tutorials",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "Cybersecurity",
            "channel": "NetworkChuck",
            "title": "Cybersecurity Tutorials",
            "url": "https://www.youtube.com/@NetworkChuck"
        },

        {
            "skill": "Linux",
            "channel": "freeCodeCamp.org",
            "title": "Linux Tutorials",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "Networking",
            "channel": "Professor Messer",
            "title": "Networking Tutorials",
            "url": "https://www.youtube.com/@professormesser"
        },

        {
            "skill": "JavaScript",
            "channel": "freeCodeCamp.org",
            "title": "JavaScript Tutorials",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "HTML",
            "channel": "freeCodeCamp.org",
            "title": "HTML Tutorials",
            "url": "https://www.youtube.com/@freecodecamp"
        },

        {
            "skill": "CSS",
            "channel": "freeCodeCamp.org",
            "title": "CSS Tutorials",
            "url": "https://www.youtube.com/@freecodecamp"
        }
    ]

    df = pd.DataFrame(resources)

    df.to_csv(
        os.path.join(
            DATA_DIR,
            "learning_resources.csv"
        ),
        index=False
    )

    return df


# ============================================================
# MAIN
# ============================================================

if __name__ == "__main__":

    print("Creating SkillPath AI datasets...")

    create_career_skills()

    create_skills()

    create_training_data()

    create_learning_resources()

    print(
        "All datasets created successfully!"
    )
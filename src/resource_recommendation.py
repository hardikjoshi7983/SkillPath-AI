import os
import pandas as pd

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RESOURCE_PATH = os.path.join(BASE_DIR, "data", "learning_resources.csv")

# Extra mappings cover the exact skill names used by the current career profiles.
# These are preparation channels/resources, not endorsements of a particular course.
CHANNELS = {
    "Python": [
        {"channel": "freeCodeCamp.org", "title": "Python tutorials", "url": "https://www.youtube.com/@freecodecamp"},
        {"channel": "Corey Schafer", "title": "Python tutorials", "url": "https://www.youtube.com/@coreyms"},
    ],
    "SQL": [
        {"channel": "freeCodeCamp.org", "title": "SQL tutorials", "url": "https://www.youtube.com/@freecodecamp"},
        {"channel": "Alex The Analyst", "title": "SQL and data analytics", "url": "https://www.youtube.com/@AlexTheAnalyst"},
    ],
    "Statistics": [
        {"channel": "StatQuest with Josh Starmer", "title": "Statistics and machine learning", "url": "https://www.youtube.com/@statquest"},
    ],
    "Machine Learning": [
        {"channel": "Krish Naik", "title": "Machine learning tutorials", "url": "https://www.youtube.com/@krishnaik06"},
        {"channel": "CampusX", "title": "Machine learning tutorials", "url": "https://www.youtube.com/@campusx-official"},
        {"channel": "StatQuest with Josh Starmer", "title": "ML concepts explained", "url": "https://www.youtube.com/@statquest"},
    ],
    "Pandas & NumPy": [
        {"channel": "Corey Schafer", "title": "Pandas tutorials", "url": "https://www.youtube.com/@coreyms"},
        {"channel": "freeCodeCamp.org", "title": "NumPy and Pandas tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Pandas": [
        {"channel": "Corey Schafer", "title": "Pandas tutorials", "url": "https://www.youtube.com/@coreyms"},
        {"channel": "freeCodeCamp.org", "title": "Pandas tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Scikit-learn": [
        {"channel": "Krish Naik", "title": "Scikit-learn and ML projects", "url": "https://www.youtube.com/@krishnaik06"},
        {"channel": "freeCodeCamp.org", "title": "Machine learning with Python", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Deep Learning": [
        {"channel": "Krish Naik", "title": "Deep learning tutorials", "url": "https://www.youtube.com/@krishnaik06"},
        {"channel": "freeCodeCamp.org", "title": "Deep learning tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Model Deployment": [
        {"channel": "Krish Naik", "title": "ML deployment and MLOps", "url": "https://www.youtube.com/@krishnaik06"},
        {"channel": "TechWorld with Nana", "title": "Docker and deployment", "url": "https://www.youtube.com/@TechWorldwithNana"},
    ],
    "Git & GitHub": [
        {"channel": "freeCodeCamp.org", "title": "Git and GitHub tutorials", "url": "https://www.youtube.com/@freecodecamp"},
        {"channel": "CodeWithHarry", "title": "Git and GitHub tutorials", "url": "https://www.youtube.com/@CodeWithHarry"},
    ],
    "Feature Engineering": [
        {"channel": "Krish Naik", "title": "Feature engineering and ML", "url": "https://www.youtube.com/@krishnaik06"},
        {"channel": "StatQuest with Josh Starmer", "title": "ML concepts", "url": "https://www.youtube.com/@statquest"},
    ],
    "Data Cleaning": [
        {"channel": "Alex The Analyst", "title": "Data cleaning and analytics", "url": "https://www.youtube.com/@AlexTheAnalyst"},
        {"channel": "Corey Schafer", "title": "Pandas and data processing", "url": "https://www.youtube.com/@coreyms"},
    ],
    "Data Visualization": [
        {"channel": "Alex The Analyst", "title": "Data visualization and analytics", "url": "https://www.youtube.com/@AlexTheAnalyst"},
        {"channel": "freeCodeCamp.org", "title": "Python data visualization", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Excel": [
        {"channel": "Leila Gharani", "title": "Excel tutorials", "url": "https://www.youtube.com/@LeilaGharani"},
        {"channel": "Alex The Analyst", "title": "Excel for data analytics", "url": "https://www.youtube.com/@AlexTheAnalyst"},
    ],
    "Power BI": [
        {"channel": "Guy in a Cube", "title": "Power BI tutorials", "url": "https://www.youtube.com/@GuyInACube"},
        {"channel": "Alex The Analyst", "title": "Power BI for analysts", "url": "https://www.youtube.com/@AlexTheAnalyst"},
    ],
    "Business Analysis": [
        {"channel": "Alex The Analyst", "title": "Data and business analytics", "url": "https://www.youtube.com/@AlexTheAnalyst"},
        {"channel": "IIBA", "title": "Business analysis resources", "url": "https://www.youtube.com/@IIBA"},
    ],
    "Communication": [
        {"channel": "TED", "title": "Communication and presentation examples", "url": "https://www.youtube.com/@TED"},
    ],
    "HTML": [
        {"channel": "freeCodeCamp.org", "title": "HTML tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "CSS": [
        {"channel": "freeCodeCamp.org", "title": "CSS tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "JavaScript": [
        {"channel": "freeCodeCamp.org", "title": "JavaScript tutorials", "url": "https://www.youtube.com/@freecodecamp"},
        {"channel": "CodeWithHarry", "title": "JavaScript tutorials", "url": "https://www.youtube.com/@CodeWithHarry"},
    ],
    "React": [
        {"channel": "freeCodeCamp.org", "title": "React tutorials", "url": "https://www.youtube.com/@freecodecamp"},
        {"channel": "CodeWithHarry", "title": "React tutorials", "url": "https://www.youtube.com/@CodeWithHarry"},
    ],
    "Responsive Design": [
        {"channel": "freeCodeCamp.org", "title": "Responsive web design", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "UI/UX": [
        {"channel": "Figma", "title": "UI/UX and Figma resources", "url": "https://www.youtube.com/@Figma"},
        {"channel": "Flux Academy", "title": "Web and UI design", "url": "https://www.youtube.com/@FluxAcademy"},
    ],
    "APIs": [
        {"channel": "freeCodeCamp.org", "title": "API and web development tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Debugging": [
        {"channel": "freeCodeCamp.org", "title": "Debugging and development tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Web Performance": [
        {"channel": "Google Chrome Developers", "title": "Web performance resources", "url": "https://www.youtube.com/@ChromeDevelopers"},
    ],
    "Flask": [
        {"channel": "freeCodeCamp.org", "title": "Flask tutorials", "url": "https://www.youtube.com/@freecodecamp"},
        {"channel": "Corey Schafer", "title": "Flask tutorials", "url": "https://www.youtube.com/@coreyms"},
    ],
    "REST APIs": [
        {"channel": "freeCodeCamp.org", "title": "REST API tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Databases": [
        {"channel": "freeCodeCamp.org", "title": "Database tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Authentication": [
        {"channel": "freeCodeCamp.org", "title": "Authentication and web security", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "Data Structures": [
        {"channel": "freeCodeCamp.org", "title": "Data structures and algorithms", "url": "https://www.youtube.com/@freecodecamp"},
        {"channel": "CodeWithHarry", "title": "DSA tutorials", "url": "https://www.youtube.com/@CodeWithHarry"},
    ],
    "Deployment": [
        {"channel": "TechWorld with Nana", "title": "Docker, cloud and deployment", "url": "https://www.youtube.com/@TechWorldwithNana"},
        {"channel": "freeCodeCamp.org", "title": "Deployment tutorials", "url": "https://www.youtube.com/@freecodecamp"},
    ],
    "UI Design": [
        {"channel": "Figma", "title": "UI design and Figma", "url": "https://www.youtube.com/@Figma"},
        {"channel": "Flux Academy", "title": "UI and web design", "url": "https://www.youtube.com/@FluxAcademy"},
    ],
    "UX Research": [
        {"channel": "NNgroup", "title": "UX research and usability", "url": "https://www.youtube.com/@NNgroup"},
        {"channel": "Figma", "title": "Product design resources", "url": "https://www.youtube.com/@Figma"},
    ],
    "Figma": [
        {"channel": "Figma", "title": "Official Figma tutorials", "url": "https://www.youtube.com/@Figma"},
    ],
    "Wireframing": [
        {"channel": "Figma", "title": "Wireframing and product design", "url": "https://www.youtube.com/@Figma"},
    ],
    "Prototyping": [
        {"channel": "Figma", "title": "Prototyping tutorials", "url": "https://www.youtube.com/@Figma"},
    ],
    "User Research": [
        {"channel": "NNgroup", "title": "User research and usability", "url": "https://www.youtube.com/@NNgroup"},
    ],
    "Typography": [
        {"channel": "Flux Academy", "title": "Typography and web design", "url": "https://www.youtube.com/@FluxAcademy"},
    ],
    "Color Theory": [
        {"channel": "Flux Academy", "title": "Color and web design", "url": "https://www.youtube.com/@FluxAcademy"},
    ],
    "Design Systems": [
        {"channel": "Figma", "title": "Design systems resources", "url": "https://www.youtube.com/@Figma"},
    ],
    "Usability Testing": [
        {"channel": "NNgroup", "title": "Usability testing resources", "url": "https://www.youtube.com/@NNgroup"},
    ],
}


def get_resources(skills):
    """Return preparation channels for the supplied skill names."""
    recommendations = []
    seen = set()

    # First use the explicit mapping because it matches the application's skill names.
    for skill in skills:
        for resource in CHANNELS.get(skill, []):
            key = (skill.lower(), resource["channel"].lower())
            if key not in seen:
                recommendations.append({"skill": skill, **resource})
                seen.add(key)

    # Then use the CSV as a fallback/extension for any future skill added to the app.
    if os.path.exists(RESOURCE_PATH):
        try:
            df = pd.read_csv(RESOURCE_PATH)
            for skill in skills:
                matches = df[df["skill"].astype(str).str.lower() == skill.lower()]
                for _, row in matches.iterrows():
                    key = (skill.lower(), str(row["channel"]).lower())
                    if key not in seen:
                        recommendations.append({
                            "skill": skill,
                            "channel": str(row["channel"]),
                            "title": str(row["title"]),
                            "url": str(row["url"]),
                        })
                        seen.add(key)
        except Exception:
            pass

    return recommendations

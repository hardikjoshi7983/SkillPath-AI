# SkillPath AI

**An AI-powered career readiness and skill gap analysis platform for students and early-career professionals.**

SkillPath AI helps users figure out exactly which skills they already have, which ones they're missing, and how to close the gap for their target career — through a machine-learning-driven readiness score, a prioritized skill roadmap, and curated free learning resources.

---

## Features

- **24 Career Roles** spanning 8 domains: AI & ML, Data & Analytics, Web & Software, Cloud & DevOps, Cybersecurity, Design, Product & Management, and Database.
- **Machine Learning Proficiency Model** trained on a synthetic dataset with Logistic Regression and Random Forest, selecting the higher-accuracy model.
- **Readiness Scoring** with tiered feedback (Beginner, Early Stage, Developing, Career Ready, Excellent).
- **Skill Gap Analysis** with per-skill current level, target level, gap size, and estimated study hours.
- **Prioritized Learning Roadmap** ordered by gap severity.
- **Curated Learning Resources** mapped per skill (YouTube channels and tutorials).
- **Interactive Visualizations** including a rating distribution pie chart, progress bars, and tier badges.
- **Session-Based State Management** — no database required.
- **Responsive Dark-Theme UI** built with modular CSS.

---

## System Architecture

### High-Level Architecture

```
┌───────────────────────────────────────────────────────────────────────┐
│                          CLIENT (Web Browser)                         │
│                                                                       │
│   index.html   profile.html   skills.html   analysis.html   roadmap.html │
└───────────────────────────────┬───────────────────────────────────────┘
                                │  HTTP (GET / POST)
                                ▼
┌───────────────────────────────────────────────────────────────────────┐
│                       FLASK APPLICATION (app.py)                      │
│                                                                       │
│   Routes:   /  →  /profile  →  /skills  →  /analysis  →  /roadmap     │
│                                                                       │
│   ┌──────────────────┐   ┌───────────────────┐   ┌────────────────┐   │
│   │  Session State   │   │  Career / Skill   │   │  Helper Logic  │   │
│   │  - profile       │   │  Constants        │   │  - readiness   │   │
│   │  - ratings       │   │  - CAREER_SKILLS  │   │  - tier calc   │   │
│   │                  │   │  - REQUIRED_LEVELS│   │  - pie style   │   │
│   │                  │   │  - CAREER_CATEGS  │   │  - hour est.   │   │
│   └──────────────────┘   └───────────────────┘   └────────────────┘   │
└──────────────┬──────────────────────────────────────────┬─────────────┘
               │                                          │
               ▼                                          ▼
┌──────────────────────────────┐          ┌──────────────────────────────┐
│      ML / DATA LAYER         │          │      RESOURCE LAYER          │
│                              │          │                              │
│  data_preprocessing.py       │          │  resource_recommendation.py  │
│  model_training.py           │          │  learning_resources.csv      │
│  prediction.py               │          │                              │
│  proficiency_model.pkl       │          │                              │
│                              │          │                              │
│  Datasets:                   │          │                              │
│   - career_skills.csv        │          │                              │
│   - skills.csv               │          │                              │
│   - training_data.csv        │          │                              │
└──────────────────────────────┘          └──────────────────────────────┘
```

### Request Lifecycle

```
User                    Flask App                 ML / Data Layer
 │                          │                            │
 │  GET /                   │                            │
 │─────────────────────────▶│                            │
 │  Render index.html       │                            │
 │◀─────────────────────────│                            │
 │                          │                            │
 │  POST /profile           │                            │
 │─────────────────────────▶│                            │
 │                          │  Store profile in session  │
 │  302 Redirect → /skills  │                            │
 │◀─────────────────────────│                            │
 │                          │                            │
 │  POST /skills            │                            │
 │─────────────────────────▶│                            │
 │                          │  Store ratings in session  │
 │  302 Redirect → /analysis│                            │
 │◀─────────────────────────│                            │
 │                          │                            │
 │  GET /analysis           │                            │
 │─────────────────────────▶│  Compute gaps + readiness  │
 │                          │  Build pie chart style     │
 │  Render analysis.html    │                            │
 │◀─────────────────────────│                            │
 │                          │                            │
 │  GET /roadmap            │                            │
 │─────────────────────────▶│  get_resources(skills)     │
 │                          │───────────────────────────▶│
 │                          │◀───────────────────────────│
 │  Render roadmap.html     │                            │
 │◀─────────────────────────│                            │
```

### Data Flow

```
User Input (profile + ratings)
        │
        ▼
Flask Session Storage  ◀──────▶  CAREER_SKILLS / REQUIRED_LEVELS (app.py)
        │
        ▼
Gap Computation
  - gap        = target − current
  - readiness  = (sum of ratings) / (skills × 5) × 100
  - priority   = High / Medium / Low
        │
        ├──────▶  ML Model (proficiency_model.pkl)  →  Confidence estimate
        │
        ▼
Roadmap Generation
  - Sorted by priority, then gap size
  - Estimated hours per skill
        │
        ▼
Resource Recommendation
  - CHANNELS dictionary + learning_resources.csv
        │
        ▼
Jinja2 Templates  →  analysis.html, roadmap.html
```

---

## Project Structure

```
skillpath-ai/
│
├── app.py                            
├── requirements.txt                  
├── README.md                         
├── proficiency_model.pkl             
│
├── data/                             
│   ├── career_skills.csv
│   ├── skills.csv
│   ├── training_data.csv
│   └── learning_resources.csv
│
├── models/                           
│   └── proficiency_model.pkl
│
├── src/                              
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── model_training.py
│   ├── prediction.py
│   ├── resource_recommendation.py
│   ├── skill_analysis.py
│   └── skill_recommendation.py
│
├── templates/                        
│   ├── index.html                    
│   ├── profile.html                 
│   ├── skills.html                   
│   ├── analysis.html                 
│   └── roadmap.html                  
│
└── static/                           
    ├── css/
    │   ├── style.css                 
    │   ├── dashboard.css             
    │   ├── roadmap.css            
    │   └── skills.css              
    └── charts/                       
```

---

## Machine Learning Pipeline

### Pipeline Flow

```
┌───────────────────────┐
│  training_data.csv    │   Synthetic dataset (~5000 samples)
│                       │
│  Features:            │
│   - course (cat.)     │
│   - year (num.)       │
│   - skill (cat.)      │
│   - self_rating       │
│   - projects_completed│
│                       │
│  Target:              │
│   - level             │   Beginner / Intermediate / Advanced
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Preprocessing        │
│   - OneHotEncoder     │   Applied to course and skill
│   - Passthrough       │   Applied to year, self_rating, projects
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Model Training       │
│   - Logistic Regression
│   - Random Forest     │
│   Compare by accuracy │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│  Best Model Saved     │
│  proficiency_model.pkl│
└───────────────────────┘
```

---

### Training the Model

```bash
# Step 1: Generate the datasets
python src/data_preprocessing.py

# Step 2: Train and evaluate the models
python src/model_training.py
```

Expected output:

```
Logistic Regression: 0.XXXX
Random Forest: 0.XXXX

Best model: <model_name>
Accuracy: <accuracy>
Model saved: models/proficiency_model.pkl
```

---

## Tech Stack

| Layer | Technologies |
|-------|--------------|
| Backend | Python 3.10+, Flask 3.0 |
| Machine Learning | scikit-learn, pandas, NumPy, joblib |
| Data Visualization | Matplotlib, CSS conic-gradient |
| Frontend | HTML5, CSS3, Jinja2 |
| Typography | Inter (Google Fonts) |
| State Management | Flask signed-cookie sessions |

---

## Installation

### Prerequisites

- Python 3.10 or higher
- pip
- virtualenv (recommended)

### Setup Steps

```bash
# 1. Clone the repository
git clone https://github.com/your-username/skillpath-ai.git
cd skillpath-ai

# 2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Generate datasets
python src/data_preprocessing.py

# 5. Train the machine learning model
python src/model_training.py
```

---

## Running the Application

```bash
python app.py
```

The application will be available at:

```
http://127.0.0.1:5000
```

---

## Usage Workflow

```
┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Landing    │───▶│   Profile    │───▶│    Skills    │───▶│   Analysis   │
│      /       │    │   /profile   │    │   /skills    │    │  /analysis   │
└──────────────┘    └──────────────┘    └──────────────┘    └──────┬───────┘
                                                                    │
                                                                    ▼
                                                             ┌──────────────┐
                                                             │   Roadmap    │
                                                             │   /roadmap   │
                                                             └──────────────┘
```

1. **Landing Page** — Introduces the platform, features, domains, and career roles.
2. **Profile** — The user enters name, email, degree, specialization, year, and target career.
3. **Skills** — The user self-rates each required skill on a 0–5 scale.
4. **Analysis** — Displays readiness score, tier, rating distribution, strengths, gaps, and a full skill table.
5. **Roadmap** — Presents a prioritized learning plan with per-skill resources and estimated study hours.

--- 

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request.

Please ensure code is tested and documented before submitting a PR.




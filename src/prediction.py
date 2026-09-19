import os
import joblib
import pandas as pd


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "proficiency_model.pkl"
)


def load_model():

    if not os.path.exists(
        MODEL_PATH
    ):

        raise FileNotFoundError(
            "ML model not found. "
            "Run model_training.py first."
        )

    return joblib.load(
        MODEL_PATH
    )


def predict_skill_level(
    course,
    year,
    skill,
    self_rating,
    projects_completed
):

    model = load_model()


    input_data = pd.DataFrame([{

        "course": course,

        "year": year,

        "skill": skill,

        "self_rating": self_rating,

        "projects_completed":
            projects_completed

    }])


    prediction = model.predict(
        input_data
    )[0]


    probabilities = model.predict_proba(
        input_data
    )[0]


    classes = model.classes_


    probability_dict = {

        str(label):

            round(
                float(probability) * 100,
                2
            )

        for label, probability

        in zip(
            classes,
            probabilities
        )
    }


    return (
        prediction,
        probability_dict
    )
import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "training_data.csv"
)

MODEL_DIR = os.path.join(
    BASE_DIR,
    "models"
)

os.makedirs(
    MODEL_DIR,
    exist_ok=True
)


def train_model():

    df = pd.read_csv(DATA_PATH)

    X = df.drop(
        "level",
        axis=1
    )

    y = df["level"]


    categorical_features = [
        "course",
        "skill"
    ]

    numerical_features = [
        "year",
        "self_rating",
        "projects_completed"
    ]


    preprocessor = ColumnTransformer(

        transformers=[

            (
                "categorical",

                OneHotEncoder(
                    handle_unknown="ignore"
                ),

                categorical_features
            )
        ],

        remainder="passthrough"
    )


    models = {

        "Logistic Regression":
            LogisticRegression(
                max_iter=1000
            ),

        "Random Forest":
            RandomForestClassifier(
                n_estimators=800,
                random_state=42
            )
    }


    X_train, X_test, y_train, y_test = train_test_split(

        X,
        y,

        test_size=0.20,

        random_state=42,

        stratify=y
    )


    best_model = None

    best_accuracy = 0

    best_name = ""


    for name, model in models.items():

        pipeline = Pipeline(

            steps=[

                (
                    "preprocessor",
                    preprocessor
                ),

                (
                    "model",
                    model
                )
            ]
        )


        pipeline.fit(
            X_train,
            y_train
        )


        predictions = pipeline.predict(
            X_test
        )


        accuracy = accuracy_score(
            y_test,
            predictions
        )


        print(
            f"{name}: "
            f"{accuracy:.4f}"
        )


        if accuracy > best_accuracy:

            best_accuracy = accuracy

            best_model = pipeline

            best_name = name


    model_path = os.path.join(

        MODEL_DIR,

        "proficiency_model.pkl"
    )


    joblib.dump(
        best_model,
        model_path
    )


    print("\nBest model:", best_name)

    print(
        "Accuracy:",
        round(
            best_accuracy,
            4
        )
    )

    print(
        "\nModel saved:",
        model_path
    )


if __name__ == "__main__":

    train_model()
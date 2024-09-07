from joblib import load
import pandas as pd

PREDICTOR_FILE_PATH = "grades/ml_model/trained_model.joblib"


class GradeMLPredictor:
    def __init__(
        self,
        year,
        period,
        grade,
        age,
        gender,
        family_size,
        parent_status,
        medu,
        fedu,
        travel_time,
        study_time,
        schoolsup,
        activities,
        higher,
        internet,
        famrel,
        freetime,
        health,
        g1_conduct,
        course,
    ):
        self.raw_data = pd.DataFrame(
            [
                [
                    year,
                    period,
                    grade,
                    age,
                    gender,
                    family_size,
                    parent_status,
                    medu,
                    fedu,
                    travel_time,
                    study_time,
                    schoolsup,
                    activities,
                    higher,
                    internet,
                    famrel,
                    freetime,
                    health,
                    g1_conduct,
                    course,
                ]
            ],
            columns=[
                "year",
                "period",
                "grade",
                "age",
                "gender",
                "famsize",
                "Pstatus",
                "Medu",
                "Fedu",
                "traveltime",
                "studytime",
                "schoolsup",
                "activities",
                "higher",
                "internet",
                "famrel",
                "freetime",
                "health",
                "G1_conduct",
                "course",
            ],
        )
        print(self.raw_data.iloc[0])

        self.clf = load(PREDICTOR_FILE_PATH)

    def map_data(self):
        # Convert string columns to int
        string_columns = ["year", "period", "age", "grade", "G1_conduct"]

        for column in string_columns:
            self.raw_data[column] = self.raw_data[column].astype(int)

        print("Obtaining code for gender:", self.raw_data.loc[0, "gender"])
        self.raw_data.loc[0, "gender_code"] = (
            1 if self.raw_data.loc[0, "gender"] == "Masculino" else 0
        )

        print("Obtaining code for famsize:", self.raw_data.loc[0, "famsize"])

        if self.raw_data.loc[0, "famsize"] == "Mas de tres":
            self.raw_data.loc[0, "famsize_code"] = 0

        elif self.raw_data.loc[0, "famsize"] == "Tres o menos":
            self.raw_data.loc[0, "famsize_code"] = 1

        print("Obtaining code for Pstatus:", self.raw_data.loc[0, "Pstatus"])
        self.raw_data.loc[0, "Pstatus_code"] = (
            1 if self.raw_data.loc[0, "Pstatus"] == "Viven juntos" else 0
        )

        print("Obtaining code for Medu:", self.raw_data.loc[0, "Medu"])
        if self.raw_data.loc[0, "Medu"] == "Educacion Primaria":
            self.raw_data.loc[0, "Medu_code"] = 0

        elif self.raw_data.loc[0, "Medu"] == "Educacion Secundaria":
            self.raw_data.loc[0, "Medu_code"] = 1

        elif self.raw_data.loc[0, "Medu"] == "Educacion Superior":
            self.raw_data.loc[0, "Medu_code"] = 2

        elif self.raw_data.loc[0, "Medu"] == "Ninguna":
            self.raw_data.loc[0, "Medu_code"] = 3

        print("Obtaining code for Fedu:", self.raw_data.loc[0, "Fedu"])
        if self.raw_data.loc[0, "Fedu"] == "Educacion Primaria":
            self.raw_data.loc[0, "Fedu_code"] = 0

        elif self.raw_data.loc[0, "Fedu"] == "Educacion Secundaria":
            self.raw_data.loc[0, "Fedu_code"] = 1

        elif self.raw_data.loc[0, "Fedu"] == "Educacion Superior":
            self.raw_data.loc[0, "Fedu_code"] = 2

        elif self.raw_data.loc[0, "Fedu"] == "Ninguna":
            self.raw_data.loc[0, "Fedu_code"] = 3

        print("Obtaining code for traveltime:", self.raw_data.loc[0, "traveltime"])
        if self.raw_data.loc[0, "traveltime"] == "15 a 30 minutos":
            self.raw_data.loc[0, "traveltime_code"] = 0

        elif self.raw_data.loc[0, "traveltime"] == "30 minutos a 1 hora":
            self.raw_data.loc[0, "traveltime_code"] = 1

        elif self.raw_data.loc[0, "traveltime"] == "Más de 1 hora":
            self.raw_data.loc[0, "traveltime_code"] = 2

        elif self.raw_data.loc[0, "traveltime"] == "Menos de 15 minutos":
            self.raw_data.loc[0, "traveltime_code"] = 3

        print("Obtaining code for studytime:", self.raw_data.loc[0, "studytime"])
        if self.raw_data.loc[0, "studytime"] == "2 a 5 horas":
            self.raw_data.loc[0, "studytime_code"] = 0

        elif self.raw_data.loc[0, "studytime"] == "Menos de 2 a 5 horas horas":
            self.raw_data.loc[0, "studytime_code"] = 1

        self.raw_data.loc[0, "schoolsup_code"] = (
            1 if self.raw_data.loc[0, "schoolsup"] == "yes" else 0
        )

        self.raw_data.loc[0, "activities_code"] = (
            1 if self.raw_data.loc[0, "activities"] == "yes" else 0
        )

        print("Obtaining code for higher:", self.raw_data.loc[0, "higher"])
        self.raw_data.loc[0, "higher_code"] = (
            1 if self.raw_data.loc[0, "higher"] == "yes" else 0
        )

        print("Obtaining code for internet:", self.raw_data.loc[0, "internet"])
        self.raw_data.loc[0, "internet_code"] = (
            1 if self.raw_data.loc[0, "internet"] == "yes" else 0
        )

        print("Obtaining code for famrel:", self.raw_data.loc[0, "famrel"])
        if self.raw_data.loc[0, "famrel"] == "Bien":
            self.raw_data.loc[0, "famrel_code"] = 0

        elif self.raw_data.loc[0, "famrel"] == "Excelente":
            self.raw_data.loc[0, "famrel_code"] = 1

        elif self.raw_data.loc[0, "famrel"] == "Mal":
            self.raw_data.loc[0, "famrel_code"] = 2

        elif self.raw_data.loc[0, "famrel"] == "Muy mal":
            self.raw_data.loc[0, "famrel_code"] = 3

        elif self.raw_data.loc[0, "famrel"] == "Regular":
            self.raw_data.loc[0, "famrel_code"] = 4

        print("Obtaining code for freetime:", self.raw_data.loc[0, "freetime"])
        if self.raw_data.loc[0, "freetime"] == "2 a 5 horas":
            self.raw_data.loc[0, "freetime_code"] = 0

        elif self.raw_data.loc[0, "freetime"] == "Mas de 5 horas":
            self.raw_data.loc[0, "freetime_code"] = 1

        elif self.raw_data.loc[0, "freetime"] == "Menos de 2 a 5 horas horas":
            self.raw_data.loc[0, "freetime_code"] = 2

        print("Obtaining code for health:", self.raw_data.loc[0, "health"])

        if self.raw_data.loc[0, "health"] == "Bien":
            self.raw_data.loc[0, "health_code"] = 0

        elif self.raw_data.loc[0, "health"] == "Excelente":
            self.raw_data.loc[0, "health_code"] = 1

        elif self.raw_data.loc[0, "health"] == "Mal":
            self.raw_data.loc[0, "health_code"] = 2

        elif self.raw_data.loc[0, "health"] == "Muy mal":
            self.raw_data.loc[0, "health_code"] = 3

        elif self.raw_data.loc[0, "health"] == "Regular":
            self.raw_data.loc[0, "health_code"] = 4

        print("Obtaining code for course:", self.raw_data.loc[0, "course"])
        if self.raw_data.loc[0, "course"] == "Historia del Perú":
            self.raw_data.loc[0, "course_code"] = 0

        elif self.raw_data.loc[0, "course"] == "Inglés":
            self.raw_data.loc[0, "course_code"] = 1

        elif self.raw_data.loc[0, "course"] == "Razonamiento Matemático":
            self.raw_data.loc[0, "course_code"] = 2

        elif self.raw_data.loc[0, "course"] == "Razonamiento Verbal":
            self.raw_data.loc[0, "course_code"] = 3

        self.raw_data.loc[0, "approved_code"] = ""

        students_features = [
            "year",
            "period",
            "grade",
            "age",
            "gender_code",
            "famsize_code",
            "Pstatus_code",
            "Medu_code",
            "Fedu_code",
            "traveltime_code",
            "studytime_code",
            "schoolsup_code",
            "activities_code",
            "higher_code",
            "internet_code",
            "famrel_code",
            "freetime_code",
            "health_code",
            "G1_conduct",
            "course_code",
        ]

        self.model_data = self.raw_data[students_features]
        print(self.model_data.iloc[0])

    def predict(self):
        self.map_data()

        prediction = self.clf.predict(self.model_data)

        print(f"This if the xgboost prediction: {prediction}")

        return "Aprobado" if prediction[0] == 1 else "Desaprobado"

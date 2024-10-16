from django import forms


class RatePredictionForm(forms.Form):
    """Form representing a student grade
    at the end of his/her course."""

    student_code = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "text", "class": "form-control", "placeholder": "ID000234"}
        ),
        required=True,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Ingresa el nombre completo",
            }
        ),
        required=True,
    )

    year = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el año"),
                ("2021", "2021"),
                ("2022", "2022"),
                ("2023", "2023"),
                ("2024", "2024"),
            ],
        ),
        required=True,
    )

    period = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa un número",
                "min": 1,
                "max": 4,
            }
        ),
        required=True,
    )

    course = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el curso"),
                ("Historia del Perú", "Historia del Perú"),
                ("Inglés", "Inglés"),
                ("Razonamiento Matemático", "Razonamiento Matemático"),
                ("Razonamiento Verbal", "Razonamiento Verbal"),
            ],
        ),
        required=True,
    )

    gender = forms.CharField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-check-input",
            },
            choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")],
        ),
        required=True,
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa un número",
                "min": 1,
                "max": 30,
            }
        ),
        required=True,
    )
    grade = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa un número",
                "min": 1,
                "max": 6,
            }
        ),
        required=True,
    )

    family_size = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el tamaño"),
                ("Mas de tres", "Mas de tres"),
                ("Tres o menos", "Tres o menos"),
            ],
        ),
        required=True,
    )

    parent_status = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el estado"),
                ("Separados", "Separados"),
                ("Viven juntos", "Viven juntos"),
            ],
        ),
        required=True,
    )
    medu = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el nivel"),
                ("Educacion Primaria", "Educacion Primaria"),
                ("Educacion Secundaria", "Educacion Secundaria"),
                ("Educacion Superior", "Educacion Superior"),
                ("Ninguna", "Ninguna"),
            ],
        ),
        required=True,
    )
    fedu = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el nivel"),
                ("Educacion Primaria", "Educacion Primaria"),
                ("Educacion Secundaria", "Educacion Secundaria"),
                ("Educacion Superior", "Educacion Superior"),
                ("Ninguna", "Ninguna"),
            ],
        ),
        required=True,
    )

    travel_time = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el tiempo"),
                (
                    "15 a 30 minutos",
                    "15 a 30 minutos",
                ),
                ("30 minutos a 1 hora", "30 minutos a 1 hora"),
                ("Más de 1 hora", "Más de 1 hora"),
                ("Menos de 15 minutos", "Menos de 15 minutos"),
            ],
        ),
        required=True,
    )
    study_time = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el tiempo"),
                (
                    "2 a 5 horas",
                    "2 a 5 horas",
                ),
                ("Menos de 2 a 5 horas horas", "Menos de 2 a 5 horas horas"),
            ],
        ),
        required=True,
    )

    schoolsup = forms.CharField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input", "type": "checkbox"},
            choices=[("true", "¿Tiene apoyo escolar?")],
        ),
        required=False,
    )

    activities = forms.CharField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input", "type": "checkbox"},
            choices=[("true", "¿Realiza actividades extracurriculares?")],
        ),
        required=False,
    )
    higher = forms.CharField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input", "type": "checkbox"},
            choices=[("true", "¿Aspira a educación superior?")],
        ),
        required=False,
    )

    internet = forms.CharField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input", "type": "checkbox"},
            choices=[("true", "¿Tiene acceso a internet?")],
        ),
        required=False,
    )
    famrel = forms.IntegerField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona una opción"),
                ("Bien", "Bien"),
                ("Excelente", "Excelente"),
                ("Mal", "Mal"),
                ("Muy mal", "Muy mal"),
                ("Regular", "Regular"),
            ],
        ),
        required=True,
    )
    freetime = forms.IntegerField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona una opción"),
                ("2 a 5 horas", "2 a 5 horas"),
                ("Mas de 5 horas", "Mas de 5 horas"),
                ("Menos de 2 a 5 horas horas", "Menos de 2 a 5 horas horas"),
            ],
        ),
        required=True,
    )
    health = forms.IntegerField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona una opción"),
                ("Bien", "Bien"),
                ("Excelente", "Excelente"),
                ("Mal", "Mal"),
                ("Muy mal", "Muy mal"),
                ("Regular", "Regular"),
            ],
        ),
        required=True,
    )
    g1_conduct = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa un número",
                "min": 0,
                "max": 20,
                "value": 0,
            }
        ),
        required=True,
    )


class PredictionResultForm(forms.Form):
    """Form for presenting student evaluation
    prediction at the end of his/her course."""

    student_code = forms.CharField(
        widget=forms.TextInput(
            attrs={"type": "text", "class": "form-control", "placeholder": "ID000234"}
        ),
        required=True,
    )
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Ingresa el nombre completo",
            }
        ),
        required=True,
    )

    year = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el año"),
                ("2021", "2021"),
                ("2022", "2022"),
                ("2023", "2023"),
                ("2024", "2024"),
            ],
        ),
        required=True,
    )

    period = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa un número",
                "min": 1,
                "max": 4,
            }
        ),
        required=True,
    )

    course = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el curso"),
                ("Historia del Perú", "Historia del Perú"),
                ("Inglés", "Inglés"),
                ("Razonamiento Matemático", "Razonamiento Matemático"),
                ("Razonamiento Verbal", "Razonamiento Verbal"),
            ],
        ),
        required=True,
    )

    gender = forms.CharField(
        widget=forms.RadioSelect(
            attrs={
                "class": "form-check-input",
            },
            choices=[("Masculino", "Masculino"), ("Femenino", "Femenino")],
        ),
        required=True,
    )
    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa un número",
                "min": 1,
                "max": 30,
            }
        ),
        required=True,
    )
    grade = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa un número",
                "min": 1,
                "max": 6,
            }
        ),
        required=True,
    )

    family_size = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el tamaño"),
                ("Mas de tres", "Mas de tres"),
                ("Tres o menos", "Tres o menos"),
            ],
        ),
        required=True,
    )

    parent_status = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el estado"),
                ("Separados", "Separados"),
                ("Viven juntos", "Viven juntos"),
            ],
        ),
        required=True,
    )
    medu = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el nivel"),
                ("Educacion Primaria", "Educacion Primaria"),
                ("Educacion Secundaria", "Educacion Secundaria"),
                ("Educacion Superior", "Educacion Superior"),
                ("Ninguna", "Ninguna"),
            ],
        ),
        required=True,
    )
    fedu = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el nivel"),
                ("Educacion Primaria", "Educacion Primaria"),
                ("Educacion Secundaria", "Educacion Secundaria"),
                ("Educacion Superior", "Educacion Superior"),
                ("Ninguna", "Ninguna"),
            ],
        ),
        required=True,
    )

    travel_time = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el tiempo"),
                ("15 a 30 minutos","15 a 30 minutos"),
                ("30 minutos a 1 hora", "30 minutos a 1 hora"),
                ("Más de 1 hora", "Más de 1 hora"),
                ("Menos de 15 minutos", "Menos de 15 minutos"),
            ],
        ),
        required=True,
    )
    study_time = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Selecciona el tiempo",
                "min": 0,
                "max": 24,
                "value": 0,
            }
        ),
        required=True,
        
        # widget=forms.Select(
        #     attrs={
        #         "class": "form-select",
        #     },
        #     choices=[
        #         ("", "Selecciona el tiempo"),
        #         (
        #             "2 a 5 horas",
        #             "2 a 5 horas",
        #         ),
        #         ("Menos de 2 a 5 horas horas", "Menos de 2 a 5 horas horas"),
        #     ],
        # ),
        # required=True,
    )
    

    schoolsup = forms.CharField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input", "type": "checkbox"},
            choices=[("true", "¿Tiene apoyo escolar?")],
        ),
        required=False,
    )

    activities = forms.CharField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input", "type": "checkbox"},
            choices=[("true", "¿Realiza actividades extracurriculares?")],
        ),
        required=False,
    )
    higher = forms.CharField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input", "type": "checkbox"},
            choices=[("true", "¿Aspira a educación superior?")],
        ),
        required=False,
    )

    internet = forms.CharField(
        widget=forms.CheckboxSelectMultiple(
            attrs={"class": "form-check-input", "type": "checkbox"},
            choices=[("true", "¿Tiene acceso a internet?")],
        ),
        required=False,
    )
    famrel = forms.IntegerField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona una opción"),
                ("Bien", "Bien"),
                ("Excelente", "Excelente"),
                ("Mal", "Mal"),
                ("Muy mal", "Muy mal"),
                ("Regular", "Regular"),
            ],
        ),
        required=True,
    )
    freetime = forms.IntegerField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona una opción"),
                ("2 a 5 horas", "2 a 5 horas"),
                ("Mas de 5 horas", "Mas de 5 horas"),
                ("Menos de 2 a 5 horas horas", "Menos de 2 a 5 horas horas"),
            ],
        ),
        required=True,
    )
    health = forms.IntegerField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona una opción"),
                ("Bien", "Bien"),
                ("Excelente", "Excelente"),
                ("Mal", "Mal"),
                ("Muy mal", "Muy mal"),
                ("Regular", "Regular"),
            ],
        ),
        required=True,
    )
    g1_conduct = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa un número",
                "min": 0,
                "max": 20,
                "value": 0,
            }
        ),
        required=True,
    )

    gf = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ingresa la nota final",
                "min": 0,
                "max": 20,
                "value": 0,
            }
        ),
        required=True,
    )

    predicted_evaluation = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "text",
                "class": "form-control",
                "placeholder": "Prediccion de evaluación final",
                "readonly": True,
            }
        ),
        required=False,
    )

    final_evaluation = forms.CharField(
        widget=forms.Select(
            attrs={
                "class": "form-select",
            },
            choices=[
                ("", "Selecciona el resultado final"),
                ("Nothing", "Sin evaluación"),
                ("Aprobado", "Aprobado"),
                ("Desaprobado", "Desaprobado"),
            ],
        ),
        required=True,
    )

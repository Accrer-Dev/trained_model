from django.shortcuts import render, redirect
from .forms import RatePredictionForm, PredictionResultForm
from .predictor import GradeMLPredictor
from .models import StudentRate


def home(request):
    return render(request, "grades/home.html", {})


def index(request):
    student_rates = StudentRate.objects.all()
    print(f"Student rates: {student_rates}")
    context = {"grades": student_rates}
    return render(request, "grades/grades_index.html", context)


def add(request):
    if request.method == "POST":
        # form = PredictionResultForm(request.POST)
        data = {k: v[0] for k, v in dict(request.POST).items()}
        print(f"Result form: {data}")
        student_code = request.POST.get("student_code")
        name = request.POST.get("name")
        year = request.POST.get("year")
        period = request.POST.get("period")

        # school = request.POST.get("school")
        course = request.POST.get("course")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        family_size = request.POST.get("family_size")
        parent_status = request.POST.get("parent_status")
        medu = request.POST.get("medu")
        fedu = request.POST.get("fedu")
        # reason = request.POST.get("reason")
        travel_time = request.POST.get("travel_time")
        study_time = request.POST.get("study_time")
        schoolsup = request.POST.get("schoolsup", "false")
        activities = request.POST.get("activities", "false")
        higher = request.POST.get("higher", "false")
        internet = request.POST.get("internet", "false")
        famrel = request.POST.get("famrel")
        freetime = request.POST.get("freetime")
        health = request.POST.get("health")
        # absences = request.POST.get("absences")
        g1_conduct = request.POST.get("g1_conduct")
        predicted_evaluation = request.POST.get("predicted_evaluation")
        final_evaluation = request.POST.get("final_evaluation")

        # r1 = request.POST.get("r1")
        gf = request.POST.get("gf")

        print(f"Student absences: {student_code} and r1: {name} ")

        student_rate = StudentRate()
        student_rate.student_code = student_code
        student_rate.name = name
        student_rate.year = year
        student_rate.period = period
        # student_rate.school = school
        student_rate.course = course
        student_rate.gender = gender
        student_rate.age = age
        student_rate.grade = grade
        student_rate.family_size = family_size
        student_rate.parent_status = parent_status
        student_rate.medu = medu
        student_rate.fedu = fedu
        # student_rate.reason = reason
        student_rate.travel_time = travel_time
        student_rate.study_time = study_time
        student_rate.schoolsup = schoolsup
        student_rate.activities = activities
        student_rate.higher = higher
        student_rate.internet = internet
        student_rate.famrel = famrel
        student_rate.freetime = freetime
        student_rate.health = health
        # student_rate.absences = absences
        student_rate.g1_conduct = g1_conduct
        student_rate.predicted_evaluation = predicted_evaluation
        student_rate.final_evaluation = final_evaluation
        # student_rate.r1 = r1
        student_rate.gf = gf

        student_rate.save()

    return redirect("/grades")


def predict(request):
    if request.method == "POST":
        form = RatePredictionForm(request.POST)

        student_code = request.POST.get("student_code")
        name = request.POST.get("name")

        print(f"Student code: {student_code} and name: {name} ")
        year = request.POST.get("year")
        period = request.POST.get("period")
        # school = request.POST.get("school")
        course = request.POST.get("course")
        gender = request.POST.get("gender")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        family_size = request.POST.get("family_size")
        parent_status = request.POST.get("parent_status")
        medu = request.POST.get("medu")
        fedu = request.POST.get("fedu")
        # reason = request.POST.get("reason")
        travel_time = request.POST.get("travel_time")
        study_time = request.POST.get("study_time")
        schoolsup = request.POST.get("schoolsup", "false")
        activities = request.POST.get("activities", "false")
        higher = request.POST.get("higher", "false")
        internet = request.POST.get("internet", "false")
        famrel = request.POST.get("famrel")
        freetime = request.POST.get("freetime")
        health = request.POST.get("health")
        g1_conduct = request.POST.get("g1_conduct")
        # absences = request.POST.get("absences")

        predictor = GradeMLPredictor(
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
        )
        prediction = predictor.predict()
        string_prediction = "This is the current prediction: {prediction}"
        print(string_prediction.format(prediction=prediction))

        data = {k: v[0] for k, v in dict(request.POST).items()}
        data["predicted_evaluation"] = prediction
        data["final_evaluation"] = "Nothing"
        # data["r1"] = 0
        # data["r2"] = 0
        result_form = PredictionResultForm(data)
        # result_form.fields["predicted_evaluation"].initial = prediction

        print(f"Result form: {data}")
        return render(
            request, "grades/grades_predict_result.html", {"form": result_form}
        )
    else:
        form = RatePredictionForm()

    return render(request, "grades/grades_predict.html", {"form": form})

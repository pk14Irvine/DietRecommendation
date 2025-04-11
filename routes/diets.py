import json
from sqlmodel import SQLModel, Session, text
from model.session import engine
from model.diet_stats import DietStats, RecResponse
from flask import Blueprint, request
from ml.knn import KNN, load_class

diet = Blueprint('diet', __name__)

@diet.route('/diet')
def check_diet_health():
    return "hello this is diet"

@diet.route('/create_diet', methods=['POST'])
def create_diet():
    stats = compose_diet_object(request.get_json())
    insert_into_db(stats)
    return dict(stats)

@diet.route('/reccomend', methods = ['GET'])
def get_reccomendation():
    with Session(engine) as session:
        person_stats = request.get_json()
        query = '''
        select "Age", "Weight_kg", "Height_cm", "BMI", "Daily_Caloric_Intake",
        "Cholesterol_mg_dL", "Glucose_mg_dL", "Weekly_Exercise_Hours", "Diet_Recommendation"
        from dietstats d
        where d.gender = :gender;
        '''
        resp = session.execute(text(query),{
            'gender': person_stats['gender'],
        }).fetchall()
        response = [compose_rec_response(row) for row in resp]
        json_data = [dict(d) for d in response]
        knn = load_class(11, json.dumps(json_data))
        person_stats = dict(person_stats)
        del person_stats['gender']
        stats = []
        for label in ["Age", "Weight_kg", "Height_cm", "BMI", "Daily_Caloric_Intake","Cholesterol_mg_dL", "Glucose_mg_dL", "Weekly_Exercise_Hours"]:
            stats.append(person_stats[label])
        rec = knn.predict(stats)
        return rec

def compose_diet_object(data):
    return DietStats(
        id=data['Patient_ID'],
        Age=data['Age'],
        gender=data['Gender'],
        Weight_kg=data['Weight_kg'],
        Height_cm=data['Height_cm'],
        BMI=data['BMI'],
        Disease_Type=data['Disease_Type'],
        Severity=data['Severity'],
        Physical_Activity_Level=data['Physical_Activity_Level'],
        Daily_Caloric_Intake=data['Daily_Caloric_Intake'],
        Cholesterol_mg_dL=data['Cholesterol_mg/dL'],
        Blood_Pressure_mmHg=data['Blood_Pressure_mmHg'],
        Glucose_mg_dL=data['Glucose_mg/dL'],
        Dietary_Restrictions=data['Dietary_Restrictions'],
        Allergies=data['Allergies'],
        Preferred_Cuisine=data['Preferred_Cuisine'],
        Weekly_Exercise_Hours=data['Weekly_Exercise_Hours'],
        Adherence_to_Diet_Plan=data['Adherence_to_Diet_Plan'],
        Dietary_Nutrient_Imbalance_Score=data['Dietary_Nutrient_Imbalance_Score'],
        Diet_Recommendation=data['Diet_Recommendation']
    )

def compose_rec_response(data) -> RecResponse:
    return RecResponse(
        Age = data[0],
        Weight_kg = data[1],
        Height_cm = data[2],
        BMI = data[3],
        Daily_Caloric_Intake = data[4],
        Cholesterol_mg_dL = data[5],
        Glucose_mg_dL = data[6],
        Weekly_Exercise_Hours = data[7],
        Diet_Recommendation = data[8]
    )

def insert_into_db(stats: DietStats):
    with Session(engine) as session:
        session.add(stats)
        session.commit()
        session.refresh(stats)
        return stats

from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field


class DietStats(SQLModel, table=True):
    id: str = Field(primary_key=True)
    Age: Optional[int]
    gender: Optional[str] = Field(index = True)
    Weight_kg: Optional[float]
    Height_cm: Optional[float]
    BMI: Optional[float]
    Disease_Type: Optional[str]
    Severity: Optional[str]
    Physical_Activity_Level: Optional[str]
    Daily_Caloric_Intake: Optional[float]
    Cholesterol_mg_dL: Optional[float]
    Blood_Pressure_mmHg: Optional[str]  # e.g., "120/80"
    Glucose_mg_dL: Optional[float]
    Dietary_Restrictions: Optional[str]
    Allergies: Optional[str]
    Preferred_Cuisine: Optional[str]
    Weekly_Exercise_Hours: Optional[float]
    Adherence_to_Diet_Plan: Optional[str]
    Dietary_Nutrient_Imbalance_Score: Optional[float]
    Diet_Recommendation: Optional[str]

class RecResponse(BaseModel):
    Age: Optional[int]
    Weight_kg: Optional[float]
    Height_cm: Optional[float]
    BMI: Optional[float]
    Daily_Caloric_Intake: Optional[float]
    Cholesterol_mg_dL: Optional[float]
    Glucose_mg_dL: Optional[float]
    Weekly_Exercise_Hours: Optional[float]
    Diet_Recommendation: Optional[str]

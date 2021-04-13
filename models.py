# coding: utf-8
# flask-sqlacodegen --flask > models.py

#어떻게 Foreign Key가 하나도 없을 수 있죠????
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Concept(db.Model):
    __tablename__ = 'concept'

    concept_id = db.Column(db.Integer, primary_key=True)
    concept_name = db.Column(db.String(255))
    domain_id = db.Column(db.String(20))
    vocabulary_id = db.Column(db.String(20))
    concept_class_id = db.Column(db.String(20))
    standard_concept = db.Column(db.String(1))
    concept_code = db.Column(db.String(50))
    valid_start_date = db.Column(db.Date)
    valid_end_date = db.Column(db.Date)
    invalid_reason = db.Column(db.String(1))

    def __str__(self):
        return self.concept_name


class ConditionOccurrence(db.Model):
    __tablename__ = 'condition_occurrence'

    condition_occurrence_id = db.Column(db.BigInteger, primary_key=True)
    person_id = db.Column(db.BigInteger)
    condition_concept_id = db.Column(db.Integer)
    condition_start_date = db.Column(db.Date)
    condition_start_datetime = db.Column(db.DateTime)
    condition_end_date = db.Column(db.Date)
    condition_end_datetime = db.Column(db.DateTime)
    condition_type_concept_id = db.Column(db.Integer)
    condition_status_concept_id = db.Column(db.Integer)
    stop_reason = db.Column(db.String(20))
    provider_id = db.Column(db.BigInteger)
    visit_occurrence_id = db.Column(db.BigInteger)
    visit_detail_id = db.Column(db.BigInteger)
    condition_source_value = db.Column(db.String(50))
    condition_source_concept_id = db.Column(db.Integer)
    condition_status_source_value = db.Column(db.String(50))



class Death(db.Model):
    __tabelname__= 'death'

    person_id=db.Column(db.BigInteger, primary_key=True) #사람이 두 번 죽진 않으니까...
    death_date=db.Column(db.Date)
    death_datetime=db.Column(db.DateTime)
    death_type_concept_id=db.Column(db.Integer)
    cause_concept_id=db.Column(db.BigInteger)
    cause_source_value=db.Column(db.Integer)
    cause_source_concept_id=db.Column(db.BigInteger)

# death 테이블에는 pk가 없다...? 왜?
# t_death = db.Table(
#     'death',
#     db.Column('person_id', db.BigInteger),
#     db.Column('death_date', db.Date),
#     db.Column('death_datetime', db.DateTime),
#     db.Column('death_type_concept_id', db.Integer),
#     db.Column('cause_concept_id', db.BigInteger),
#     db.Column('cause_source_value', db.Integer),
#     db.Column('cause_source_concept_id', db.BigInteger)
# )


class DrugExposure(db.Model):
    __tablename__ = 'drug_exposure'

    drug_exposure_id = db.Column(db.BigInteger, primary_key=True)
    person_id = db.Column(db.BigInteger)
    drug_concept_id = db.Column(db.Integer)
    drug_exposure_start_date = db.Column(db.Date)
    drug_exposure_start_datetime = db.Column(db.DateTime)
    drug_exposure_end_date = db.Column(db.Date)
    drug_exposure_end_datetime = db.Column(db.DateTime)
    verbatim_end_date = db.Column(db.Date)
    drug_type_concept_id = db.Column(db.Integer)
    stop_reason = db.Column(db.String(20))
    refills = db.Column(db.Integer)
    quantity = db.Column(db.Numeric)
    days_supply = db.Column(db.Integer)
    sig = db.Column(db.Text)
    route_concept_id = db.Column(db.Integer)
    lot_number = db.Column(db.String(50))
    provider_id = db.Column(db.BigInteger)
    visit_occurrence_id = db.Column(db.BigInteger)
    visit_detail_id = db.Column(db.BigInteger)
    drug_source_value = db.Column(db.String(50))
    drug_source_concept_id = db.Column(db.Integer)
    route_source_value = db.Column(db.String(50))
    dose_unit_source_value = db.Column(db.String(50))



class Person(db.Model):
    __tablename__ = 'person'

    person_id = db.Column(db.BigInteger, primary_key=True)
    gender_concept_id = db.Column(db.Integer)
    year_of_birth = db.Column(db.Integer)
    month_of_birth = db.Column(db.Integer)
    day_of_birth = db.Column(db.Integer)
    birth_datetime = db.Column(db.DateTime)
    race_concept_id = db.Column(db.Integer)
    ethnicity_concept_id = db.Column(db.Integer)
    location_id = db.Column(db.BigInteger)
    provider_id = db.Column(db.BigInteger)
    care_site_id = db.Column(db.BigInteger)
    person_source_value = db.Column(db.String(50))
    gender_source_value = db.Column(db.String(50))
    gender_source_concept_id = db.Column(db.Integer)
    race_source_value = db.Column(db.String(50))
    race_source_concept_id = db.Column(db.Integer)
    ethnicity_source_value = db.Column(db.String(50))
    ethnicity_source_concept_id = db.Column(db.Integer)



class VisitOccurrence(db.Model):
    __tablename__ = 'visit_occurrence'

    visit_occurrence_id = db.Column(db.BigInteger, primary_key=True)
    person_id = db.Column(db.BigInteger)
    visit_concept_id = db.Column(db.Integer)
    visit_start_date = db.Column(db.Date)
    visit_start_datetime = db.Column(db.DateTime)
    visit_end_date = db.Column(db.Date)
    visit_end_datetime = db.Column(db.DateTime)
    visit_type_concept_id = db.Column(db.Integer)
    provider_id = db.Column(db.BigInteger)
    care_site_id = db.Column(db.BigInteger)
    visit_source_value = db.Column(db.String(50))
    visit_source_concept_id = db.Column(db.Integer)
    admitted_from_concept_id = db.Column(db.Integer)
    admitted_from_source_value = db.Column(db.String(50))
    discharge_to_source_value = db.Column(db.String(50))
    discharge_to_concept_id = db.Column(db.Integer)
    preceding_visit_occurrence_id = db.Column(db.BigInteger)

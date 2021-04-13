from flask_restx import Namespace
from flask_restx import Api, Resource
from sqlalchemy import func 
from models import Person, VisitOccurrence, ConditionOccurrence, DrugExposure, Concept, Death
from models import db


person = Namespace('Person', description="환자", path='/person')



@person.route('/total')
class TotalNum(Resource):
    def get(self):
        """전체 환자 수"""
        return {"전체 환자 수":Person.query.count()}



@person.route('/death')
class DeathNum(Resource):
    def get(self):
        '''사망 환자 수'''
        return {"사망 환자 수":Death.query.count()}



@person.route('/gender')
class GenderNum(Resource):
    def get(self):
        '''성별 환자 수'''
        Json = dict()
        q = db.session.query(
            Person.gender_concept_id,Concept.concept_name,func.count()
        ).select_from(
            Person
        ).join(
            Concept,Person.gender_concept_id == Concept.concept_id
        ).group_by(
            Person.gender_concept_id,Concept.concept_name
        ).all()
        for _, name, num in q:
            Json[name] = num
        return Json



@person.route('/race')
class RaceNum(Resource):
    def get(self):
        '''인종별 환자 수'''
        Json = dict()
        q = db.session.query(
            Person.race_concept_id,Concept.concept_name,func.count()
        ).select_from(
            Person
        ).join(
            Concept,Person.race_concept_id == Concept.concept_id
        ).group_by(
            Person.race_concept_id,Concept.concept_name
        ).all()
        for _, name, num in q:
            Json[name] = num
        return Json



@person.route('/ethnicity')
class EthnicityNum(Resource):
    def get(self):
        '''민족별 환자 수'''
        Json = dict()
        q = db.session.query(
            Person.ethnicity_concept_id,Concept.concept_name,func.count()
        ).select_from(
            Person
        ).join(
            Concept,Person.ethnicity_concept_id == Concept.concept_id
        ).group_by(
            Person.ethnicity_concept_id,Concept.concept_name
        ).all()
        for _, name, num in q:
            Json[name] = num
        return Json
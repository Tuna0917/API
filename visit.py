from flask_restx import Namespace
from flask_restx import Api, Resource
from sqlalchemy import func, extract
from models import Person as p, VisitOccurrence as v, ConditionOccurrence, DrugExposure, Concept as c, Death
from models import db

visit=Namespace('Visit',description='방문',path='/visit')

@visit.route('/type')
class TypeNum(Resource):
    def get(self):
        '''방문 유형(입원/외래/응급)별 방문 수'''
        Json = dict()
        q = db.session.query(
            v.visit_concept_id,c.concept_name,func.count()
        ).select_from(
            v
        ).join(
            c,v.visit_concept_id == c.concept_id
        ).group_by(
            v.visit_concept_id,c.concept_name
        ).all()
        for _, name, num in q:
            Json[name] = num
        return Json
@visit.route('/gender')
class GenderNum(Resource):
    def get(self):
        '''성별 방문 수'''
        Json = dict()
        q = db.session.query(
            c.concept_name, func.count()
        ).select_from(
            v
        ).join(
            p, p.person_id == v.person_id
        ).join(
            c, c.concept_id == p.gender_concept_id
        ).group_by(
            c.concept_name
        ).all()
        for name, num in q:
            Json[name] = num
        return Json  

@visit.route('/race')
class RaceNum(Resource):
    def get(self):
        '''인종별 방문 수'''
        Json = dict()
        q = db.session.query(
            c.concept_name, func.count()
        ).select_from(
            v
        ).join(
            p, p.person_id == v.person_id
        ).join(
            c, c.concept_id == p.race_concept_id
        ).group_by(
            c.concept_name
        ).all()
        for name, num in q:
            Json[name] = num
        return Json

@visit.route('/ethnicity')
class EthnicityNum(Resource):
    def get(self):
        '''민족별 방문 수'''
        Json = dict()
        q = db.session.query(
            c.concept_name, func.count()
        ).select_from(
            v
        ).join(
            p, p.person_id == v.person_id
        ).join(
            c, c.concept_id == p.ethnicity_concept_id
        ).group_by(
            c.concept_name
        ).all()
        for name, num in q:
            Json[name] = num
        return Json

@visit.route('/age')
class AgeNum(Resource):
    def get(self):
        '''방문시 연령대(10세 단위)별 방문 수'''
        Json = dict()
        q = db.session.query(
            func.floor(extract('year', func.age(v.visit_start_datetime,p.birth_datetime))/10)*10, func.count()
        ).join(
            p, p.person_id == v.person_id
        ).group_by(
            func.floor(extract('year', func.age(v.visit_start_datetime,p.birth_datetime))/10)*10
        ).order_by(
            func.floor(extract('year', func.age(v.visit_start_datetime,p.birth_datetime))/10)*10
        )
        for name, num in q:
            Json[str(int(name))+"대"] = num
        return Json

'''
select floor(EXTRACT(year from age(v.visit_start_datetime,p.birth_datetime))/10)*10, count(*) as cnt

from person as p
join visit_occurrence as v
on v.person_id = p.person_id
group by 1
order by 1;
'''
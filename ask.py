from flask import make_response, jsonify, request, abort
from flask_restx import Namespace
from flask_restx import Api, Resource
from sqlalchemy import func 
from sqlalchemy.orm import aliased
from models import Person as p , VisitOccurrence as v, ConditionOccurrence as co, DrugExposure as de, Concept as c, Death as d
from models import db

ask = Namespace('Ask', description="조회",path='/ask')

pagination_limit = 20

#https://stackoverflow.com/questions/55543011/flask-restful-pagination
def get_paginated_list(results, url, start, limit):
    start = int(start)
    limit = int(limit)
    count = len(results)
    if count < start or limit < 0:
        abort(404)
    # make response
    obj = {}
    obj['start'] = start
    obj['limit'] = limit
    obj['count'] = count
    # make URLs
    # make previous url
    if start == 1:
        obj['previous'] = ''
    else:
        start_copy = max(1, start - limit)
        limit_copy = start - 1
        obj['previous'] = url + '?start=%d&limit=%d' % (start_copy, limit_copy)
    # make next url
    if start + limit > count:
        obj['next'] = ''
    else:
        start_copy = start + limit
        obj['next'] = url + '?start=%d&limit=%d' % (start_copy, limit)
    # finally extract result according to bounds
    obj['results'] = results[(start - 1):(start - 1 + limit)]
    return obj




@ask.route('/condition')
class ConditionOccurrenceAsk(Resource):
    def get(self):
        '''condition_occurrence 조회'''
        data = []
        q = db.session.query(
            co.person_id,
            co.condition_concept_id,
            c.concept_name,
            co.condition_start_datetime,
            co.condition_end_datetime,
            co.visit_occurrence_id
        ).select_from(
            co
        ).join(
            c, c.concept_id == co.condition_concept_id
        )
        for _1,_2,_3,_4,_5,_6 in  q:
            data.append({
                'person_id' : _1,
                'condition_concept_id' : _2,
                'condition_concept_name' : _3,
                'condition_start_datetime' : _4,
                'condition_end_datetime' : _5,
                'visit_occurrence_id' : _6,
            })
        return jsonify(get_paginated_list(
        data, 
        '/ask/condition', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', pagination_limit)
        ))



@ask.route('/death')
class DeathAsk(Resource):
    def get(self):
        '''death 조회'''
        data = []
        q = d.query.all()
        for death in q:
            data.append({
            'person_id' : death.person_id,
            'death_date' : death.death_date,
            })
        return jsonify(get_paginated_list(
        data, 
        '/ask/death', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', pagination_limit)
        ))



@ask.route('/drug')
class DrugExposureAsk(Resource):
    def get(self):
        '''drug_exposure 조회'''
        data = []
        q = db.session.query(
            de.person_id, de.drug_concept_id, c.concept_name, de.drug_exposure_start_datetime, de.drug_exposure_end_datetime, de.visit_occurrence_id
        ).select_from(
            de
        ).join(
            c, c.concept_id == de.drug_concept_id
        )
        for _1,_2,_3,_4,_5,_6 in  q:
            data.append({
                'person_id' : _1,
                'drug_concept_id' : _2,
                'drug_concept_name' : _3,
                'drug_exposure_start_datetime' : _4,
                'drug_exposure_end_datetime' : _5,
                'visit_occurrence_id' : _6,
            })
        return jsonify(get_paginated_list(
        data, 
        '/ask/drug', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', pagination_limit)
        ))



@ask.route('/person')
class PersonAsk(Resource):
    def get(self):
        '''person조회'''
        data = []
        c2 = aliased(c)
        c3 = aliased(c)
        q = db.session.query( 
            p.person_id, p.gender_concept_id, c.concept_name,p.birth_datetime, p.race_concept_id, c2.concept_name,p.ethnicity_concept_id, c3.concept_name
        ).select_from(
            p
        ).join(
            c, c.concept_id == p.gender_concept_id
        ).join(
            c2, c2.concept_id == p.race_concept_id
        ).join(
            c3, c3.concept_id == p.ethnicity_concept_id
        ).all()
        for _1,_2,_3,_4,_5,_6,_7,_8 in q:
            data.append({
                'person_id' : _1,
                'gender_concept_id' : _2,
                'gender_concept_name' : _3,
                'birth_datetime' : _4,
                'race_concept_id' : _5,
                'race_concept_name' : _6,
                'ethnicity_concept_id' : _7,
                'ethnicity_concept_name' : _8,
            })
        return jsonify(get_paginated_list(
        data, 
        '/ask/person', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', pagination_limit)
        ))



@ask.route('/visit')
class VisitOccurrenceAsk(Resource):
    def get(self):
        '''visit_occurrence 조회'''
        data = []
        q = db.session.query(
            v.visit_occurrence_id, v.person_id, v.visit_concept_id, c.concept_name,v.visit_start_datetime,v.visit_end_datetime
        ).select_from(
            v
        ).join(
            c, c.concept_id == v.visit_concept_id
        )
        for _1,_2,_3,_4,_5,_6 in  q:
            data.append({
                'visit_occurrence_id' : _1,
                'person_id' : _2,
                'visit_concept_id' : _3,
                'visit_concept_name' : _4,
                'visit_start_datetime' : _5,
                'visit_end_datetime' : _6,
            })
        return jsonify(get_paginated_list(
        data, 
        '/ask/visit', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', pagination_limit)
        ))
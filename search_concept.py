from flask import make_response, jsonify, request, abort
from flask_restx import Namespace
from flask_restx import Api, Resource
from sqlalchemy import func 
from models import Concept as c
from models import db

search = Namespace('Search Concept', description="concept 검색.", path='/search')

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



@search.route('/id/<int:id>')
class SearchWithId(Resource):
    def get(self, id):
        '''이미 id를 알고 있을 경우'''
        q = c.query.filter(c.concept_id == id).first()
        if q:
            Json = {
                "id": q.concept_id,
                "name": q.concept_name,
                "domain": q.domain_id,
            }
            return Json
        else:
            return make_response(jsonify(f"{id} is not found."),404)



@search.route('/<search>')
class Search(Resource):
    def get(self, search):
        '''검색 기능'''
        data = []
        for k in c.query.filter(c.concept_name.like(f'{search}%')).all():
            data.append(
                {
                    "concept_id" : k.concept_id,
                    "concept_name" : k.concept_name,
                    "domain_id" : k.domain_id,
                }
            )

        return jsonify(get_paginated_list(
        data, 
        f'/search/{search}', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', pagination_limit)
        ))



@search.route('/keyword/<keyword>')
class SearchWithKeyword(Resource):
    def get(self, keyword):
        '''키워드 검색 기능'''
        kw = '% ' +' % '.join(keyword.split('%20'))+ ' %'
        #두 단어 이상이 입력되면 왜 안되는걸까요?
        data = []
        for k in c.query.filter(c.concept_name.like(f'{kw}')).all():
            data.append(
                {
                    "concept_id" : k.concept_id,
                    "concept_name" : k.concept_name,
                    "domain_id" : k.domain_id,
                }
            )

        return jsonify(get_paginated_list(
        data, 
        f'/search/keyword/{keyword}', 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', pagination_limit)
        ))


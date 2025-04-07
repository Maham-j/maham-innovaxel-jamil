from flask import Blueprint, request, jsonify
from models import db, URL
import shortuuid
from datetime import datetime

routes = Blueprint('routes', __name__)

def validate_url_input(data):
    if not data or 'url' not in data:
        return False, jsonify({"error": "Missing 'url' in request body"}), 400
    return True, None, None

@routes.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    valid, response, status = validate_url_input(data)
    if not valid:
        return response, status

    original_url = data['url']
    short_code = shortuuid.ShortUUID().random(length=6)

    new_url = URL(original_url=original_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()

    return jsonify({
        "id": new_url.id,
        "url": new_url.original_url,
        "shortCode": new_url.short_code,
        "createdAt": new_url.created_at.isoformat(),
        "updatedAt": new_url.updated_at.isoformat()
    }), 201

@routes.route('/shorten/<short_code>', methods=['GET'])
def get_original_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        url_entry.visit_count += 1
        db.session.commit()
        return jsonify({
            "id": url_entry.id,
            "url": url_entry.original_url,
            "shortCode": url_entry.short_code,
            "createdAt": url_entry.created_at.isoformat(),
            "updatedAt": url_entry.updated_at.isoformat()
        })
    return jsonify({"error": "Short URL not found"}), 404

@routes.route('/shorten/<short_code>', methods=['PUT'])
def update_url(short_code):
    data = request.get_json()
    valid, response, status = validate_url_input(data)
    if not valid:
        return response, status

    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        url_entry.original_url = data['url']
        url_entry.updated_at = datetime.utcnow()
        db.session.commit()
        return jsonify({
            "id": url_entry.id,
            "url": url_entry.original_url,
            "shortCode": url_entry.short_code,
            "createdAt": url_entry.created_at.isoformat(),
            "updatedAt": url_entry.updated_at.isoformat()
        })
    return jsonify({"error": "Short URL not found"}), 404

@routes.route('/shorten/<short_code>', methods=['DELETE'])
def delete_url(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        db.session.delete(url_entry)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Short URL not found"}), 404

@routes.route('/shorten/<short_code>/stats', methods=['GET'])
def get_url_stats(short_code):
    url_entry = URL.query.filter_by(short_code=short_code).first()
    if url_entry:
        return jsonify({
            "id": url_entry.id,
            "url": url_entry.original_url,
            "shortCode": url_entry.short_code,
            "createdAt": url_entry.created_at.isoformat(),
            "updatedAt": url_entry.updated_at.isoformat(),
            "accessCount": url_entry.visit_count
        })
    return jsonify({"error": "Short URL not found"}), 404

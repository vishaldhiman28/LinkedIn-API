from flask import Blueprint, jsonify, request, abort
from helper.linkedin import check_json_data, generate_unique_key
from lifeline.hawk.access_linkedin_hacker import AccessLinkedInHacker

linkedin = Blueprint('linkedin', __name__)


@linkedin.route('/linkedin/user_profile/', methods=['POST'])
def get_user_profile_details():
    json_data = request.json
    if not json_data:
        abort(400, description="JSON Error")

    if not check_json_data(json_data):
        abort(400, description="Specified Values are not provided.")
    try:
        unique_key = generate_unique_key(json_data)
        generated_data = AccessLinkedInHacker.access_the_hacker(unique_key, **json_data)
        return jsonify(generated_data), 200
    except:
        error_info = {"error_info": "Error Occurred at the Backend"}
        return jsonify(error_info), 500


@linkedin.route('/linkedin/company_details/')
def get_company_details():
    pass


@linkedin.route('/linkedin/school_details/')
def get_school_details():
    pass


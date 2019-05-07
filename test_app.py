
import dateutil.parser as date_parser

from flask import Flask, jsonify

from assignment_utils import AssignmentChecks

app = Flask(__name__)


@app.route('/business_seconds/<start_time>/<end_time>/', methods=['GET'])
def get_business_seconds(start_time, end_time):
    """Calculates business seconds between given time parameters.
    Returns an appropriate error message string for failed requests.
    """

    start_date = date_parser.parse(start_time)
    end_date = date_parser.parse(end_time)
    days = [start_date, end_date]

    # Initialise checks class to run validate checks.
    checks = AssignmentChecks(days)

    # Run required checks on parameters.
    checks.check_za_holidays()
    checks.check_weekdays()
    checks.check_work_hours()
        
    # If any checks failed, return errors string: else, calculate and return business seconds.
    if checks.has_errors():
        return checks.errors

    else:
        # Still running after checks. Calculate and return business seconds.
        business_seconds = int((end_date-start_date).total_seconds())
        return jsonify(business_seconds=business_seconds)

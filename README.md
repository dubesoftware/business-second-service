# business-secondr
A minimal Flask application with an GET endpoint that calculates and returns business seconds between two valid ISO 8601 dates (or returns appropriate error information on failed requests). The application tests that the dates provided do not fall on a South Africa holiday, are weekdays and (when hours are provided) are work hours in the format ```yyyy-mm-ddThh:mm:ss.ffffff```.

In order to test the application, use the following URL with the default Flask development server address and port:

```http://127.0.0.1:5000/business_seconds/<start_time>/<end_time>/```

Use the following command to run the Flask application: ```env FLASK_APP=test_app.py flask run```

The test tool used is unittest.

# business-secondr
A minimal Flask application with an GET endpoint that calculates and returns business seconds between two valid ISO 8601 dates (or returns appropriate error information on failed requests).

In order to test the application, use the following URL with the default Flask development server address and port:

http://127.0.0.1:5000/business_seconds/<start_time>/<end_time>/

The test tool used is unittest.
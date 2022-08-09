##Question 3
### Update `main.py` to make it an API for inference. Make the API invokable from a http request. The choice of web framework is up to you.

The API should have two endpoints:
- `POST /stream` : which takes a payload of one record and return the prediction for that record.
- `POST /batch` : which takes an array of multiple records and return an array of predictions

Think about what other features an enterprise machine learning system would have. 

## Solution

1. Go to `./question_3` directory to set as root directory.
2. Run `python app.py`

## Test
   - Head to `http://127.0.0.1:8080` to test the api in swagger and check request requirements.
   - Can also test in postman. Payload requirement:
     - Stream example: `{ "data": [ 0 ] }`
     - Stream requires 1 value.
     - Batch example: `{ "data": [ 1, 3] }`
     - Batch requires > 1 value.
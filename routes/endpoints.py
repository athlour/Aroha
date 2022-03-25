from fastapi import FastAPI, Request

app = FastAPI()


@app.api_route("/customer", methods=["GET", "POST"])
async def customer(request: Request, **customer_id):
    response_code, msg, result = None, None, False
    try:
        if request.method == "POST":
            # TODO Process the POST Request
            response_code, msg = 200, 'Success'
            result = True
        if request.method == "GET":
            # TODO Use the customer_id parameter/key and process the query request
            response_code, msg = 200, 'Success'
            result = True
    except Exception as e:
        response_code, msg = 500, e
    finally:
        if result is True:
            return {'Request Type': request.method, 'Response Code': response_code, 'message': msg, 'result': result}
        else:
            return {'Request Type': request.method, 'Response Code': response_code, 'message': msg}


@app.api_route("/bank/", methods=["GET", "POST"])
async def bank(request: Request, **bank_id):
    try:
        if request.method == "POST":
            # TODO Process the POST Request
            response_code, msg = 200, 'Success'
            result = True
        if request.method == "GET":
            # TODO Use the bank_id parameter/key and process the query request
            response_code, msg = 200, 'Success'
            result = True
    except Exception as e:
        response_code, msg = 500, e
    finally:
        if result is True:
            return {'Request Type': request.method, 'Response Code': response_code, 'message': msg, 'result': result}
        else:
            return {'Request Type': request.method, 'Response Code': response_code, 'message': msg}


@app.api_route("/source", methods=["GET", "POST"])
async def source(request: Request, **source_id: str):
    try:
        if request.method == "POST":
            # TODO Process the POST Request
            response_code, msg = 200, 'Success'
            result = True
        if request.method == "GET":
            # TODO Use the source_id parameter/key and process the query request
            response_code, msg = 200, 'Success'
            result = True
    except Exception as e:
        response_code, msg = 500, e
    finally:
        if result is True:
            return {'Request Type': request.method, 'Response Code': response_code, 'message': msg, 'result': result}
        else:
            return {'Request Type': request.method, 'Response Code': response_code, 'message': msg}
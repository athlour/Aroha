from fastapi import FastAPI, Request

app = FastAPI()


@app.api_route("/customer", methods=["GET", "POST"])
async def customer(request: Request, customer_id: str):
    if request.method == "POST":
        return {'Response Code': 200, 'Request Type': request.method}
    if request.method == "GET":
        # TODO Use the customer_id parameter/key and process the query request
        return {'Response Code': 200, 'Request Type': request.method, 'Query': customer_id}
    else:
        return {'Response Code': 501, 'Request Type': request.method}


@app.api_route("/bank", methods=["GET", "POST"])
async def bank(request: Request, bank_id: str):
    if request.method == "POST":
        return {'Response Code': 200, 'Request Type': request.method}
    if request.method == "GET":
        # TODO Use the bank_id parameter/key and process the query request
        return {'Response Code': 200, 'Request Type': request.method, 'Query': bank_id}
    else:
        return {'Response Code': 501, 'Request Type': request.method}


@app.api_route("/source", methods=["GET", "POST"])
async def source(request: Request, source_id: str):
    if request.method == "POST":
        return {'Response Code': 200, 'Request Type': request.method}
    if request.method == "GET":
        # TODO Use the bank_id parameter/key and process the query request
        return {'Response Code': 200, 'Request Type': request.method, 'id': source_id}
    else:
        return {'Response Code': 501, 'Request Type': request.method}
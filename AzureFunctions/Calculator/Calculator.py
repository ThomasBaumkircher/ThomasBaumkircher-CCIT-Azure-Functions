import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="Calculator")
def Calculator(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    calc = req.params.get('calc')
    if not calc:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            calc = req_body.get('calc')

    if calc:
        return func.HttpResponse(str(eval(calc)))
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
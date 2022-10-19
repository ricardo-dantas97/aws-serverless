import json


def lambda_handler(event, context):
    names = []
    for name in event.values():
        names.append(name.capitalize())
    
    name = ' '.join(names)
    print(f'Your name is {name}! Welcome to AWS Serverless!')

    response = {
        "status_code": 200,
        "body": {
            "data": f"{name}"
        }
    }

    return response

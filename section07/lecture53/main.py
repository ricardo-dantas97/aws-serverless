import json
import requests


def lambda_handler(event, context):
    r = requests.get(url='https://api.adviceslip.com/advice')
    r = r.json()
    advice = r['slip']['advice']

    names = []
    for name in event.values():
        names.append(name.capitalize())
    
    name = ' '.join(names)
    print(f'Hello {name}. I would like to give you a random advice:')
    print(advice)

    response = {
        "status_code": 200,
        "body": {
            "data": {
                "name": f"{name}",
                "advice": f"{advice}"
            }
        }
    }

    return response

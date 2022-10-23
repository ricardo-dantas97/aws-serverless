import json


def lambda_handler(event, context):
    print(f'Event received: \n {json.dumps(event)}')

    # Fetch method and querystring
    method = event['requestContext']['http']['method']
    query_string = event['queryStringParameters']
    body = json.loads(event['body'])
    

    response = {
        'status_code': 200,
        'body': {
            'data': {
                'method': f'{method}',
                'query_string': query_string,
                'body': body
            }
        }
    }

    return response
import json

def lambda_handler(event, context):
    print(f'Event received: \n{json.dumps(event)}')
    
    try:
        route = event['routeKey']

        if route == 'GET /product':
            body = 'Processing GET all products.'
        elif route == 'GET /product/{id}':
            id = event['pathParameters']['id']
            body = f'Processing GET product ID {id}'
        elif route == 'POST /product':
            if 'body' in event:
                post_body = json.loads(event['body'])
            else:
                post_body = {}
            body = f'Body received: {post_body}'                
        elif route == 'DELETE /product/{id}':
            id = event['pathParameters']['id']
            body = f'Processing DELETE product ID {id}'
        else:
            raise (f'Unsupported route: {route}')
        
        return {
            'status_code': 200,
            'body': {
                'message': f'Sucessfully finished operation: {route}',
                'body': body
            }
        }

    except Exception as error:
        print(error)
        return {
            'status_code': 400,
            'body': {
                'message': 'Failed to perform operation',
                'error_message': error
            }
        }
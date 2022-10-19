def lambda_handler(event, context):
    print(f'Remaining time: {context.get_remaining_time_in_millis()}')
    print(f'Function name: {context.function_name}')

    body = {
        "function_name": f"{context.function_name}",
        "logstream_name": f"{context.log_stream_name}"
    }

    return body
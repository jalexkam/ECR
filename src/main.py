def lambda_handler(event, context):
    """
    AWS Lambda handler function.
    
    Parameters:
    event (dict): The event data passed to the Lambda function (e.g., API Gateway payload).
    context (object): Provides runtime information about the Lambda function.

    Returns:
    dict: Response object.
    """
    # Log the incoming event for debugging
    print("Event Received:", event)

    # Example response
    response = {
        "statusCode": 200,
        "body": "Hello, this is a basic Lambda function!"
    }

    return response

import datetime
import boto3
import uuid


def lambda_handler(event, context):
    contract_id = str(uuid.uuid4())

    # circuit_status = event['CircuitStatus']

    dynamodb = boto3.resource('dynamodb')

    table_name = 'circuit-breaker-info'
    table = dynamodb.Table(table_name)

    item = {
        'contractId': contract_id,
        'timestamp': datetime.datetime.now().isoformat(),
        'circuitStatus': "CLOSED"
    }

    table.put_item(Item=item)

    raise ValueError("Erro proposital, abrindo o circuito...")

    # return {
    #     'statusCode': 200,
    #     'contractId': f'{contract_id}'
    # }



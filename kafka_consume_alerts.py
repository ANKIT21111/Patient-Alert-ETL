import boto3
import json
from kafka import KafkaConsumer

# Set up Kafka consumer
kafka_bootstrap_servers = '44.215.14.94:9092'
topic = 'PatientHealthNotification'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers=[kafka_bootstrap_servers],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Set up AWS SNS client
sns_client = boto3.client('sns', region_name='us-east-1')

# Define the SNS topic ARN
sns_topic_arn = 'arn:aws:sns:us-east-1:590184062134:Health_Alert_Notification'

for message in consumer:
    alert = message.value
    
    patient_name = alert.get('patientname')
    age = alert.get('age')
    patient_address = alert.get('patientaddress')
    phone_number = alert.get('phone_number')
    admitted_ward = alert.get('admitted_ward')
    bp = alert.get('bp')
    heartbeat = alert.get('heartbeat')
    input_message_time = alert.get('input_message_time')
    alert_message = alert.get('alert_message')
    
    email_subject = f"Health Alert for Patient {patient_name}"
    email_body = f"""
    Alert Details:
    
    Patient Name: {patient_name}
    Age: {age}
    Address: {patient_address}
    Phone Number: {phone_number}
    Admitted Ward: {admitted_ward}
    Blood Pressure: {bp}
    Heartbeat: {heartbeat}
    Alert Message: {alert_message}
    Message Time: {input_message_time}
    """
    
    # Publish message to SNS topic
    response = sns_client.publish(
        TopicArn=sns_topic_arn,
        Subject=email_subject,
        Message=email_body
    )
    
    print(f"Alert sent for patient {patient_name}. SNS response: {response}")
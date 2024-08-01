import json
import os
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=os.environ["KAFKA_BOOTSTRAP_SERVER"])

# Utility function to convert DynamoDB item to regular JSON
def mongodb_to_json(mongo_item):
    return json.loads(mongo_item)

def format_score_card(item_json):
    score_card_title = "Exam-Generator - Score Card"
    student_email = item_json.get("email", "No email provided")
    result = item_json.get("result", "Result not available")
    score = item_json.get("score", "Score not available")
    details = item_json.get("details", [])

    message_body = f"{score_card_title}\n\n"
    message_body += f"Student: {student_email}\n"
    message_body += f"Score: {score}\n"
    message_body += f"Result: {result.upper()}\n\n"
    message_body += "Exam Details:\n"

    for question in details:
        user_answer = question.get("user_answer", "N/A")
        correct_answer = question.get("correct_answer", "N/A")
        question_text = question.get("question", "N/A")
        is_correct = "Correct" if question.get("is_correct", False) else "Incorrect"
        message_body += f"- Question: {question_text}\n"
        message_body += f"  Your Answer: {user_answer} ({is_correct})\n"
        message_body += f"  Correct Answer: {correct_answer}\n\n"

    #message_body += "For full details about the questions answered, check the student's record in the database."

    return message_body

def lambda_handler(event, context):
    topic_arn = os.environ['EMAIL_TOPIC_ARN']

    image = event['payload']['after']

    # Convert DynamoDB JSON to regular JSON
    item_json = mongodb_to_json(image)

    # Format the message as a score card
    message = format_score_card(item_json)
    print(message)
    try:
        producer.send(topic_arn, message.encode())
    except Exception as e:
        print(f"Error sending Kafka notification: {e}")
        raise

    return {
        'statusCode': 200,
        'body': json.dumps('Lambda executed successfully!')
    }
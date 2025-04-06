import requests

def trigger_webhook(request_id, status):
    webhook_url = "https://your-webhook-endpoint.com"
    payload = {"request_id": request_id, "status": status}
    requests.post(webhook_url, json=payload)
    return "Webhook triggered"
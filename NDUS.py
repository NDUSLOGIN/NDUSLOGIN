import requests

def send_to_discord(username, fact):
    webhook_url = 'https://discordapp.com/api/webhooks/1338546359342469329/64X4z3WOE0GyGgmYPhMA792MxhaCJhoS3tfBOxNKbDzJQp5YzbiM21qQpranBzoCqadd'
    payload = {
        'content': f"New entry received:\nUsername: {username}\nFact: {fact}"
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(webhook_url, json=payload, headers=headers)
    if response.status_code == 204:
        print('Message sent successfully!')
    else:
        print(f'Error: {response.status_code}')

# Example form data
username = 'JohnDoe'
fact = 'I love programming!'

send_to_discord(username, fact)


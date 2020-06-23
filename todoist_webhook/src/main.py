import yaml
from todoist.api import TodoistAPI
from flask import Flask, request, Response

with open("config/config.yaml", "r") as yamlfile:
        cfg = yaml.load(yamlfile, Loader=yaml.FullLoader)

api = TodoistAPI(cfg['api_key'])


app = Flask(__name__)

def reduceItemPriority(payload):
    item_id = payload["event_data"]["id"]
    item = api.items.get_by_id(item_id)
    item.update(priority=2)
    api.commit()

@app.route('/webhook', methods=['POST'])
def respond():
        payload = request.json
        if payload["event_name"] == "item:completed":
            due = payload["event_data"]["due"]
            if due:
                is_recurring = due["is_recurring"]
                if is_recurring:
                    print(f"Task {payload['event_data']['content']}: Recurring Task checked. Reseting Priority to minimal");
                    reduceItemPriority(payload)
        return Response(status=200)

if __name__ == "__main__":
        from waitress import serve
        serve(app, host="0.0.0.0", port=8800)

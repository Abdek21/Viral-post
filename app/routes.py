from flask import Blueprint, request, jsonify, current_app
import requests
from .celery_config import celery

main = Blueprint('main', __name__)

@main.route('/generate', methods=['POST'])
def generate_content():
    data = request.get_json()
    prompt = data.get('prompt')
    
    api_key = current_app.config['OPENAI_API_KEY']
    
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={"Authorization": f"Bearer {api_key}"},
        json={"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": prompt}], "max_tokens": 150}
    )
    
    if response.status_code == 200:
        result = response.json()
        if result and 'choices' in result and len(result['choices']) > 0:
            content = result['choices'][0].get('message').get('content')
            return jsonify({"content": content})
        else:
            return jsonify({"error": "Invalid response from API"}), 500
    else:
        return jsonify({"error": "Failed to connect to API"}), 500

@main.route('/schedule', methods=['POST'])
def schedule_post():
    data = request.get_json()
    post_data = {
        "prompt": data.get('prompt'),
        "platform": data.get('platform'),
        "time": data.get('time')
    }
    
    try:
        task = celery.send_task('tasks.schedule_post', args=[post_data], eta=data.get('time'))
        return jsonify({"message": "Post scheduled successfully!", "task_id": task.id})
    except Exception as e:
        return jsonify({"error": f"Failed to schedule post: {str(e)}"}), 500

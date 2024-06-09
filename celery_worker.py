from app.celery_config import celery
import requests
import os

@celery.task(name='tasks.schedule_post')
def schedule_post(post_data):
    response = requests.post('https://api.openai.com/v1/engines/gpt-3.5-turbo/completions', 
                             headers={"Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"},
                             json={"prompt": post_data['prompt'], "max_tokens": 150})
    
    content = response.json().get('choices')[0].get('text')
    # Simuler la publication du contenu sur une plateforme de réseaux sociaux
    print(f"Posted to {post_data['platform']}: {content}")
    return content

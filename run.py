from app import create_app
import os

app, celery = create_app()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))  # Utiliser le port spécifié par Render ou 8000 par défaut
    app.run(host='0.0.0.0', port=port)

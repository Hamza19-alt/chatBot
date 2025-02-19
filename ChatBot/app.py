import json
import random
from flask import Flask, request, jsonify, render_template, redirect, url_for
import os  # Pour la gestion des fichiers

app = Flask(__name__)

# Base de connaissances du chatbot avec ajout de planification
responses = {
    "bonjour": ["Bonjour ! Comment puis-je vous aider ?"],
    "je veux regarder le programmes": [
        "voila notre programme : https://suprh.com/licence-en-intelligence-artificielle-et-business-2/"
    ],
     "Oui": [
        "Sup'RH propose plusieurs formations en RH, Management et Data. Souhaitez-vous plus de détails ?"
    ],
    "horaires": [
        "Les horaires des cours varient selon les modules et les niveaux. Consultez votre emploi du temps en ligne."
    ],
    "inscription": [
        "Les inscriptions se font en ligne ou sur place. Avez-vous besoin d'aide pour le dossier ?"
    ],
    "merci": ["De rien ! N'hésitez pas si vous avez d'autres questions."],
    "planification": [
        "Vous pouvez consulter votre planification sur le portail des étudiants. Voulez-vous voir un exemple ?",
        "Pour la planification des cours, vous pouvez vérifier votre emploi du temps en ligne."
    ],
    "emploi du temps": [
        "L'emploi du temps est disponible en ligne. Voulez-vous que je vous envoie un lien ?",
        "Voici un exemple d'emploi du temps : ![Image](https://example.com/emploi_du_temps.jpg)"
    ],
    "planning": [
        "Le planning des cours est sur la plateforme. Voulez-vous voir un visuel ?",
        "Voici une illustration du planning des cours : ![Planning](https://example.com/planning_image.jpg)"
    ],
}

# Chemin vers le fichier d'historique
HISTORY_FILE = "data/history.json"

# Fonction pour charger l'historique (si le fichier existe)
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    else:
        return []

# Fonction pour sauvegarder l'historique
def save_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

@app.route('/')
def home():
    return render_template('index.html', logo_url='/static/image.png')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message", "").lower()
    response = responses.get(user_input, ["Je ne suis pas sûr de comprendre. Pouvez-vous reformuler ?"])
    bot_response = random.choice(response)

    # Sauvegarder la conversation dans l'historique
    history = load_history()
    history.append({"user": user_input, "bot": bot_response})
    save_history(history)

    return jsonify({"response": bot_response})

@app.route('/history')
def history():
    conversation_history = load_history()
    return render_template('history.html', history=conversation_history, logo_url='/static/image.png')

if __name__ == '__main__':
    # Créer le dossier 'data' s'il n'existe pas
    if not os.path.exists("data"):
        os.makedirs("data")
    app.run(debug=True)

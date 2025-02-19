document.addEventListener('DOMContentLoaded', function() {
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const chatLog = document.getElementById('chat-log');

    function appendMessage(sender, message) {
        const messageElement = document.createElement('div');
        messageElement.innerHTML = `<b>${sender}:</b> ${message}`;
        chatLog.appendChild(messageElement);
        chatLog.scrollTop = chatLog.scrollHeight; // Faire défiler vers le bas
    }

    sendButton.addEventListener('click', function() {
        const message = userInput.value.trim();
        if (message) {
            appendMessage('Vous', message);
            userInput.value = ''; // Effacer l'input

            // Envoyer la requête au serveur
            fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message: message })
            })
            .then(response => response.json())
            .then(data => {
                appendMessage('Chatbot', data.response);
            });
        }
    });

    // Gérer la touche "Entrée" pour envoyer le message
    userInput.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            sendButton.click(); // Simuler un clic sur le bouton Envoyer
            event.preventDefault(); // Empêcher le saut de ligne
        }
    });
});
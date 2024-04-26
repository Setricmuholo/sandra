document.addEventListener('DOMContentLoaded', function() {
    const speakButton = document.getElementById('speakButton');

    speakButton.addEventListener('click', function() {
        const text = "Welcome to Sandra's Web App.";
        speakText(text);
    });

    function speakText(text) {
        const speech = new SpeechSynthesisUtterance();
        speech.text = text;
        speech.volume = 1;
        speech.rate = 1;
        speech.pitch = 1;

        window.speechSynthesis.speak(speech);
    }
});
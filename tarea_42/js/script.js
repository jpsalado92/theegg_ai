var SpeechRecognition = SpeechRecognition || webkitSpeechRecognition
var SpeechGrammarList = SpeechGrammarList || webkitSpeechGrammarList
var SpeechRecognitionEvent = SpeechRecognitionEvent || webkitSpeechRecognitionEvent

var vid = document.getElementById("myVideo");

var commands = ['start', 'stop'];
var grammar = '#JSGF V1.0; grammar commands; public <command> = ' + commands.join(' | ') + ' ;'

var recognition = new SpeechRecognition();
var speechRecognitionList = new SpeechGrammarList();

speechRecognitionList.addFromString(grammar, 1);

recognition.grammars = speechRecognitionList;
recognition.continuous = false;
recognition.lang = "en-US";
recognition.interimResults = false;
recognition.maxAlternatives = 1;

var diagnostic = document.querySelector(".output");

document.body.onclick = function () {
    recognition.start();
    console.log("Ready to receive a color command.");
};

recognition.onresult = function (event) {
    var command = event.results[0][0].transcript;
    diagnostic.textContent = "Result received: " + command + ".";
    if (command == "start") {
        vid.play();
    } else if (command == "stop") {
        vid.pause();
    } else {
    }
    console.log("Confidence: " + event.results[0][0].confidence);
};

recognition.onspeechend = function () {
    recognition.stop();
};

recognition.onnomatch = function (event) {
    diagnostic.textContent = "I didnt recognise that command.";
};

recognition.onerror = function (event) {
    diagnostic.textContent = "Error occurred in recognition: " + event.error;
};

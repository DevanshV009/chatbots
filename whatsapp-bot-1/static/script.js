async function sendMessage() {

    let msg =
        document.getElementById("message").value;

    let response =
        await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: msg
            })

        });

    let data =
        await response.json();

    let chat =
        document.getElementById("chat-box");

    chat.innerHTML +=
        "<p><b>You:</b> " + msg + "</p>";

    chat.innerHTML +=
        "<p><b>Bot:</b> " + data.reply + "</p>";

    document.getElementById("message").value = "";
}

window.onload = async function () {

    let response =
        await fetch("/chat", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: "start"
            })

        });

    let data =
        await response.json();

    document.getElementById("chat-box").innerHTML =
        "<p><b>Bot:</b> " + data.reply + "</p>";
};
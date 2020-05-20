document.addEventListener('DOMContentLoaded', () => {
    let ws_path = 'ws://' + window.location.host + window.location.pathname + 'websocket';
    let ws = new WebSocket(ws_path);
    ws.onopen = function() {
        ws.send(true);
    }
    ws.onmessage = function(msg) {
        console.log(msg.data)
        data = JSON.parse(msg.data)
        cam1 = document.getElementById('cam1');
        cam1.setAttribute('src', 'data:image/jpg;base64,' + data.colored)
        cam2 = document.getElementById('cam2');
        cam2.setAttribute('src', 'data:image/jpg;base64,' + data.gray)
        ws.send(true);
    };

    ws.onerror = function(e) {
        console.log(e);
        ws.send(true);
    };
});
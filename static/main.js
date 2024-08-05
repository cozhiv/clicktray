// web component MouseTray
class MouseTray extends HTMLElement {
  constructor() {
    super();

    const shadow = this.attachShadow({mode: 'open'});
    const title = document.createElement('h1');
    title.textContent = 'Your cursor coordinates:';
    shadow.appendChild(title);
    const holder = document.createElement('div');
    holder.setAttribute('class', 'tray-holder');
    shadow.appendChild(holder);
    const template = document.createElement('template');
    template.innerHTML = `
    <style>
    @import "static/styles.css";
    </style>`;
    this.shadowRoot.appendChild(template.content.cloneNode(true));
    const uri = document.getElementById("websocket-uri").textContent;
    const ws = new WebSocket(`ws://${uri}/`);
    console.log(ws);
    ws.onmessage = function(event){
      console.log('[Message received from server]', event.data)
      // Create paragraph node and add the recieved coordinates to it
      const currentPosition = document.createElement('div');
      currentPosition.setAttribute('class', 'tray')
      currentPosition.textContent = event.data;
      // Add to holder
      holder.appendChild(currentPosition);
      window.scrollTo(0, document.body.scrollHeight);
    };
  }
}

// Define click-tray element
customElements.define('mouse-tray', MouseTray);
// web component Shot
class Shot extends HTMLElement {
  constructor() {
    super();

    const shadow = this.attachShadow({mode: 'open'});
    const title = document.createElement('h1');
    title.textContent = 'Pic from your camera';
    shadow.appendChild(title);
    const holder = document.createElement('div');
    holder.setAttribute('class', 'tray-holder');
    shadow.appendChild(holder);
    const template = document.createElement('template');
    template.innerHTML = `
    <style>
    @import "static/shot.css";
    </style>`;
    this.shadowRoot.appendChild(template.content.cloneNode(true));
    window.addEventListener("load", this.handleClick)
      const yourPic = document.createElement('img');
      yourPic.setAttribute('class', 'snap')
      yourPic.setAttribute('id', 'snap1');
      yourPic.setAttribute('src', '')
      const coordinates = document.createElement('div');
      coordinates.setAttribute('class', 'coordinates');
      holder.appendChild(yourPic);
      holder.appendChild(coordinates)
      window.addEventListener('load', async function(){
        const pic1 = document.getElementById("snap1");
        const currentUrl = window.location.toString();
        const picNum = currentUrl.substring(currentUrl.lastIndexOf("/") + 1)
        console.log(picNum)
        const picAndXY = await getData(picNum);
        coordinates.textContent = `Clicked on (${picAndXY[0]} : ${picAndXY[1]})`
        yourPic.setAttribute("src", `data:image/jpeg;charset=utf-8;base64, ${picAndXY[2].substring(2,picAndXY[2].length-1)}`);
      })
  }
}

customElements.define('one-shot', Shot);

async function getData(p) {
    const url = `http://localhost:5000/snap/${p}`;
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }

      const json = await response.json();
      console.log(json);
      return json;
    } catch (error) {
      console.error(error.message);
    }

  }

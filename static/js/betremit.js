function loadIframe() {
  var iframe = document.createElement('iframe');
  iframe.id = 'betremitIframe';
  iframe.style.display = 'none';
  iframe.name = 'betremitIframe';
  iframe.frameBorder = 0;
  document.body.appendChild(iframe);
}

function openIframe() {
  loadIframe();
  var betremitIframe = document.getElementById('betremitIframe');
  betremitIframe.src = 'modal.html';
  betremitIframe.style.display = 'block';
  betremitIframe.style.position = 'fixed';
  betremitIframe.style.left = '0px';
  betremitIframe.style.top = '0px';
  betremitIframe.style.width = '100%';
  betremitIframe.style.height = '100%';
  betremitIframe.style.border = 0;
}

function closeIframe() {
  var betremitIframe = document.getElementById('betremitIframe');
  document.body.removeChild(betremitIframe);
}

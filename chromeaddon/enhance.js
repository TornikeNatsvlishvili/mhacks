// inject tooltip
$("body").append('<div id="tooltip"></div>')

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

var globalCount = 0;
function callback(contentJSON){
    var natlangJSON = contentJSON;
    
    $.each($(".story-body-text"), function(i, _v){
        var words = $(_v).text().split(" ");
        $(_v).empty();
        $.each(words, function(i, v) {
            
            tuple = natlangJSON['pos-tag'][parseInt(i)]
            _class = "inactive";
            if(tuple[1].indexOf("NN") != -1){
                _class = "token"
            }
            $elem = $("<span>").text(v + " ").attr("class", _class).attr("id", globalCount++);
            
            $elem.mousemove(function(event) { 
                id = $(event.target).attr("id")
                $tooltip = $("#tooltip")
                tuple = natlangJSON['pos-tag'][parseInt(id)]
                if(tuple[1].indexOf("NN") != -1){
                    $.ajax("http://45.33.74.171:5000/picture/" + tuple[0], function(data){
                        $tooltip
                            .css({top: event.pageY - $tooltip.height(), left: event.pageX - $tooltip.width()/2})
                            .innerHTML('<img src="' + data + '"/>' )
                            .show();
                    });
                }
            });
            $elem.mouseout(function() {
                $('#tooltip').hide();
            });
            
            $(_v).append($elem);
        });
            
    });

}


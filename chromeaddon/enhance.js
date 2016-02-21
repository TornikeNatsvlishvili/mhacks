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
var picHash = []

var neChunkCount = 0;

function callback(contentJSON){
    var natlangJSON = contentJSON;
    
    $.each($(".story-body-text"), function(i, _v){
        var words = $(_v).text().split(" ");
        $(_v).empty();
        $.each(words, function(i, v) {
            
            var tuple = natlangJSON['ne-chunk'][neChunkCount++]
            
            var count = (tuple[0][0].match(/\s/g) || []).length;
            var matchedString = ""
            for(var j = 0; j < count + 1; j++){
                matchedString += words[i+j] + " "
                neChunkCount++;
            }
            
            var _class = "inactive";
            if(tuple[0][1].indexOf("NN") != -1){
                _class = "token"
            }
            var $elem = $("<span>").text(matchedString).attr("class", _class).attr("id", globalCount++);
            
            
            
            
            
            
            
        //     var tuple = natlangJSON['pos-tag'][parseInt(i)]
        //     var _class = "inactive";
        //     if(tuple[1].indexOf("NN") != -1){
        //         _class = "token"
        //     }
        //     var $elem = $("<span>").text(v + " ").attr("class", _class).attr("id", globalCount++);
            
        //     if(tuple[1].indexOf("NN") != -1){
        //         $elem.mousemove(function(event) {
        //             var id = parseInt(event.target.id)
        //             if(picHash[id] == undefined){
        //                 var hoverTuple = natlangJSON['pos-tag'][id]
        //                 picHash[id] = "loading"
        //                 $.get("http://45.33.74.171:5000/picture/" + hoverTuple[0], function(data){
        //                     var $tooltip = $("#tooltip")                        
        //                     $tooltip                        
        //                         .css({top: event.pageY - $tooltip.height(), left: event.pageX - $tooltip.width()/2})
        //                         .html('<span>'+hoverTuple+'</span><img src="' + data + '"/>' )
        //                         .show();
        //                     picHash[id] = data
        //                 });
        //             } else{
        //                 var $tooltip = $("#tooltip")                        
        //                 $tooltip                        
        //                         .css({top: event.pageY - $tooltip.height(), left: event.pageX - $tooltip.width()/2})
        //                         .html('<span>'+hoverTuple+'</span><img src="' + picHash[id] + '"/>' )
        //                         .show();
        //             }
        //         });
        //         $elem.mouseout(function() {
        //             $('#tooltip').hide();
        //         });
        //     }
            
            $(_v).append($elem);
        });
            
    });

}


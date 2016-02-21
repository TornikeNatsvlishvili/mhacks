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
        
        var currentWord = 0;
        while(currentWord < words.length){
            // if bad character skip
            if("!\"#$%&\'()*+,-.:;<=>?@[\\]".indexOf(words[currentWord].trim()) != -1) {                
                $(_v).append($("<span>").text(words[currentWord].trim()));
                currentWord++;
                continue;
            }
            
            var chunk = natlangJSON['ne-chunk'][neChunkCount++]
            var matchedString = ""
            chunk['tokens'].forEach(function(v, i){
                matchedString += words[currentWord] + " "
                console.log(words[currentWord] + ' -- ' + chunk['tokens'][i]['phrase'] + ' -- ' + neChunkCount)
                currentWord++;
            });
               
            var _class = "inactive";
            if(chunk['tokens'][0]['tag'].indexOf("NN") != -1){
                _class = "token"
            }
            var $elem = $("<span>").text(matchedString).attr("class", _class).attr("id", globalCount++);
            
            if(_class === "token"){
                $elem.mousemove(function(event) {
                    var id = parseInt(event.target.id)
                    if(picHash[id] == undefined){
                        var hoverChunk = natlangJSON['ne-chunk'][id]
                        var query = ""
                        hoverChunk['tokens'].forEach(function(v, i){
                            query += v['phrase'] += " "
                        })
                        picHash[id] = "loading"
                        $.get("http://45.33.74.171:5000/picture/" + query, function(data){
                            var $tooltip = $("#tooltip")                        
                            $tooltip                        
                                .css({top: event.pageY - $tooltip.height(), left: event.pageX - $tooltip.width()/2})
                                .html('<img src="' + data + '"/>' )
                                .show();
                            picHash[id] = data
                        });
                    } else{
                        var $tooltip = $("#tooltip")                        
                        $tooltip                        
                                .css({top: event.pageY - $tooltip.height(), left: event.pageX - $tooltip.width()/2})
                                .html('<img src="' + picHash[id] + '"/>' )
                                .show();
                    }
                });
                $elem.mouseout(function() {
                    $('#tooltip').hide();
                });
            }
            
            $(_v).append($elem);
        }   
    });
}


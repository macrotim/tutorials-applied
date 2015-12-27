var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

exports.getTodos = function getTodos(listId, callback) {
    var xhr = new XMLHttpRequest();

    xhr.onreadystatechange = function() {
        if (this.readyState === 4) {
            callback(null, this.responseText);
        }
    };

    xhr.open("GET", "/todo/" + listId + "/items");
    xhr.send();
};

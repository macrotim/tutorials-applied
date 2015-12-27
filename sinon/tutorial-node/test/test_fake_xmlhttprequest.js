var assert = require('chai').assert;
var sinon = require('sinon');
var todos = require('../todos');

describe.skip('fake xmlhttprequest', function() {
    var xhr, requests;
    before(function () {
        xhr = sinon.useFakeXMLHttpRequest();
        requests = [];
        xhr.onCreate = function (req) { requests.push(req); };
    });

    after(function () {
        // Like before we must clean up when tampering with globals.
        xhr.restore();
    });

    it("makes a GET request for todo items", function () {
        todos.getTodos(42, sinon.spy());

        assert.equal(requests.length, 1);
        assert.notEqual(requests[0].url.indexOf("/todo/42/items") == -1);
    });
});

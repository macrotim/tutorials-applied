var assert = chai.assert;
var xhr, requests;

describe('fake xmlhttprequest', function() {
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
        getTodos(42, sinon.spy());

        assert.equal(requests.length, 1);
        assert.notEqual(requests[0].url.indexOf("/todo/42/items") == -1);
    });
});

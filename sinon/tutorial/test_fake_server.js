var server;

describe('fake server', function() {
    beforeEach(function () { server = sinon.fakeServer.create(); });
    afterEach(function () { server.restore(); });

    it("calls callback with deserialized data", function () {
        var callback = sinon.spy();
        getTodos(42, callback);

        // This is part of the FakeXMLHttpRequest API
        server.requests[0].respond(
            200,
            { "Content-Type": "application/json" },
            JSON.stringify([{ id: 1, text: "Provide examples", done: true }])
        );

        assert(callback.calledOnce);
    });
});

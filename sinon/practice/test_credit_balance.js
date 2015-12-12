/* Tim: Test a more complex example that uses ajax. */

var assert = chai.assert;

describe('get credit balance', function() {
    var server;
    beforeEach(function () { server = sinon.fakeServer.create(); });
    afterEach(function () { server.restore(); });

    var parseVer = function(requestNum) {
        var match = /ver=(\d+)/.exec(server.requests[requestNum].url)
        if (match.length == 1) {
            throw "ver not found";
        }
        return parseInt(match[1]);
    };

    it("responses arrive in order", function () {
        var user = {};
        getCreditBalance(user)
        getCreditBalance(user)

        // The second response returns early.
        server.requests[0].respond(
            200,
            { "Content-Type": "application/json" },
            JSON.stringify({
                creditBalance: 180,
                ver: parseVer(0)})
        );

        // The first response returns later.
        server.requests[1].respond(
            200,
            { "Content-Type": "application/json" },
            JSON.stringify({
                creditBalance: 150,
                ver: parseVer(1)})
        );

        assert.equal(user.creditBalance, 150);
    });

    it("responses arrive out of order, ignore stale responses", function () {
        var user = {};
        getCreditBalance(user);
        getCreditBalance(user);

        // The second response returns early.
        server.requests[1].respond(
            200,
            { "Content-Type": "application/json" },
            JSON.stringify({
                creditBalance: 150,
                ver: parseVer(1)})
        );

        // The first response returns later.
        server.requests[0].respond(
            200,
            { "Content-Type": "application/json" },
            JSON.stringify({
                creditBalance: 180,
                ver: parseVer(0)})
        );

        assert.equal(user.creditBalance, 150);
    });
});

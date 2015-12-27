var assert = require('chai').assert;
var sinon = require('sinon');
var jQuery = require('jquery');

describe.skip('stubbed ajax', function() {
    after(function () {
        // When the test either fails or passes, restore the original
        // jQuery ajax function (Sinon.JS also provides tools to help
        // test frameworks automate clean-up like this)
        jQuery.ajax.restore();
    });

    it("makes a GET request for todo items", function () {
        sinon.stub(jQuery, "ajax");
        getTodos(42, sinon.spy());

        assert(jQuery.ajax.calledWithMatch({ url: "/todo/42/items" }));
    });
});

/* Testing time-sensitive logic without the wait is a breeze with Sinon.JS. */

function throttle(callback) {
    var timer;
    return function () {
        clearTimeout(timer);
        var args = [].slice.call(arguments);
        timer = setTimeout(function () {
            callback.apply(this, args);
        }, 100);
    };
}

var clock;

describe('fake time', function() {
    before(function () { clock = sinon.useFakeTimers(); });
    after(function () { clock.restore(); });

    it("calls callback after 100ms", function () {
        var callback = sinon.spy();
        var throttled = throttle(callback);

        throttled();

        clock.tick(99);
        assert(callback.notCalled);

        clock.tick(1);
        assert(callback.calledOnce);

        // Also:
        // assert.equals(new Date().getTime(), 100);
    });
});

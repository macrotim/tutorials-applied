define(function (require) {
    var _ = require('underscore');

    _.each(_.functions(_), function (method) {
        _[method] = sinon.spy(_[method]);
    });

    return _;

});

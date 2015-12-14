define(function (require) {
    var $ = require('jquery');

    $(function() {
        $('body').append($('<div>').text('hello world'));
    });
});

/**
 * "Click Counter" is a simple jQuery plugin.
 */
(function($) {
    /**
     * Setup the jQuery object as a click-counter.
     * Each click increments the HTML text.
     */
    $.fn.counter = function() {
        return this.each(function() {
            var el = $(this);

            var count = el.attr('data-count') || 0;
            el.attr('data-count', count);
            el.text(count);

            el.click(function() {
                var count = el.attr('data-count');
                el.attr('data-count', ++count);
                el.text(count);
            });

            return el;
        });
    };
}(jQuery));

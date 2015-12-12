var ver = 0;

/*
 * getCreditBalance ignores stale server responses.
 */
var getCreditBalance = function(user) {
    var u = jQuery.extend({ver: ver++}, user);

    jQuery.ajax({
        url: "/credit-balance",
        data: u,
        success: function (data) {
            if (!('ver' in user) || data.ver >= user.ver) {
                user.creditBalance = data.creditBalance;
                user.ver = u.ver;
            }
        }
    });
};

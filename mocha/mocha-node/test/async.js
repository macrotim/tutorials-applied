var User = function(name) {
    return {
        save: function(callback) {
            // Perform the save asynchronously.
            setTimeout(function() {
                callback(null, this);
            }, 100);
        }
    }
};

var should = require('should');

describe('User', function() {
  describe('#save()', function() {
    it('should save without error', function(done) {
      var user = new User('Luna');
      user.save(function(err) {
        if (err) throw err;
        done();
      });
    });

    it('should save without error', function(done) {
      var user = new User('Luna');
      user.save(done);
    });
  });
});

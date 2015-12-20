var User = function(name) {
    return {
        save: function(callback) {
            // Perform the save asynchronously.
            setTimeout(function() {
                if (name != null) {
                    callback(null, this);
                } else {
                    callback('Error: name cannot be null');
                }
            }, 100);
        }
    }
};

var should = require('should');

describe('User', function() {
  describe('#save()', function() {
    it('throws error in async callback', function(done) {
      var cb = function(err) {
        if (err) {
          done();
        }
      };

      var user = new User(null);
      user.save(cb);
    });
  });
});

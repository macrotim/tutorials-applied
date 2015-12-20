/* By appending .skip(), you may tell Mocha to simply
   ignore these suite(s) and test case(s). */

describe('Array', function() {
  describe.skip('#indexOf()', function() {
    // ...
    it('return -1 if value is absent', function(done) {
        done();
    });
  });
});

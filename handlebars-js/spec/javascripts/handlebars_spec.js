/**
 * Tim: Here, I practice writing Javascript unit tests.
 *      The tests don't serve any real purpose.
 */
describe("Handlebars", function() {
  it("supports one string variable", function() {
    var template = Handlebars.compile('<div>{{body}}</div>');
    var html = template({body: "Body."});
    expect(html).toBe('<div>Body.</div>');
  });

  it("supports duplicate variables", function() {
    var template = Handlebars.compile('<div>{{body}}</div><div>{{body}}</div>');
    var html = template({body: "Body."});
    expect(html).toBe('<div>Body.</div><div>Body.</div>');
  });

  it("ignores variable if undefined", function() {
    var template = Handlebars.compile('<div>{{body}}</div>');
    var html = template({});
    expect(html).toBe('<div></div>');
  });
});

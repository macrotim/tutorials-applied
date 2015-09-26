Jasmine
=======

Jasmine is a Behavior Driven Development testing framework for JavaScript. It does not rely on browsers, DOM, or any JavaScript framework. Thus it's suited for websites, Node.js projects, or anywhere that JavaScript can run.

`Intro`_

.. _Intro: http://jasmine.github.io/2.3/introduction.html

Setup
=====

Install Jasmine's Python runner. 

    pip install -r reqs.txt
    
Initialize Jasmine for this project.

    jasmine-install

Configure the location of your .js source and specs.

    vi spec/javascripts/support/jasmine.yml

Start the Jasmine runner.

    jasmine

View Jasmine specs in the browser. 

    http://127.0.0.1:8888/

Jasmine Runner
==============

The Python runner serves up a project's Jasmine suite in a browser so you can focus on your code instead of manually editing script tags in the Jasmine runner HTML file.

`Overview`_

.. _Overview: https://github.com/jasmine/jasmine-py

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

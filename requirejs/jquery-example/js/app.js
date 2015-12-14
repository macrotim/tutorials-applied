requirejs.config({
    baseUrl: 'js',
    paths: {
        jquery: 'https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min'
    }
});

requirejs(["main"]);

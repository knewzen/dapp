require([
        'libs/polyfills',
        'jquery',
        'subapp/header/header'
    ],
    function (polyfill,
              $,
              Header
              ) {
        //header application
        new Header();


        console.log('index app fuck');


    });

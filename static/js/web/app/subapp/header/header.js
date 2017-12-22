define(['jquery', 'libs/Class'],function($,Class){
    var HeaderApp = Class.extend({
        init_menu: function () {
            $('#dropme').click(function (e) {
               $(e.currentTarget).toggleClass('is-active');
            });
        },
        init: function () {
            this.init_menu();

        }
    });

    return HeaderApp;
});
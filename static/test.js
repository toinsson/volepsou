$(document).ready(function() {
    console.log("AHAHHHAHHAHAHAHHAHAHHAAHH!");

    $('.photoset-grid').photosetGrid({
        layout: '232',
        width: '100%',
        gutter: '5px',
        highresLinks: true,
        lowresWidth: 300,
        rel: 'gallery-01',

        onInit: function(){},
        onComplete: function(){

            $('.photoset-grid').css({
                'visiblity': 'visible'
            });

        }
    });

    // $('.photoset-grid').photosetGrid();

});

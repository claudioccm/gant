$(document).ready(function($) {
    $('.js-stage-collapse').click(function() {
        $(this).closest('.stage').toggleClass('m-active');
    });

    $('.js-category-collapse').click(function() {
        $(this).closest('.category').toggleClass('m-active');
    });


    // $('.tweetable').click(function() {
    //     function success(data) {
    //         text = encodeURIComponent(text.slice(0, 124) + ' #opengov - ' + data.id);

    //         window.open(url2 + text, '_blank', 'width=450, height=300');
    //     }

    //     var text = $(this).text(),
    //         url1 = 'https://www.googleapis.com/urlshortener/v1/url?key=',
    //         url2 = 'https://twitter.com/intent/tweet?lang=en&count=none&text=';

    //     $.ajax({
    //         url: url1 + 'AIzaSyBnpHRDUZhCruzPnmNrN6U_KikY_28-61Q',
    //         type: 'POST',
    //         data: JSON.stringify({'longUrl': window.location.href}),
    //         success: success,
    //         dataType: 'json',
    //         contentType: 'application/json; charset=utf-8'
    //     });
    // });

    // $('.e-mobile-menu-trigger').click(function() {
    //     $('.b-menu').toggleClass('m-active');
    //     $('#overlay').toggleClass('m-active');
    // });

    // $('#overlay').click(function() {
    //     $('.b-menu').removeClass('m-active');
    //     $(this).removeClass('m-active');
    // });


    // var hamm = new Hammer.Manager($('.b-menu')[0]),
    //     left = $('.b-menu').css('transform').replace(', 0)', '');

    // left = parseInt(left.replace('matrix(1, 0, 0, 1, ', ''));

    // hamm.add(new Hammer.Pan({ threshold: 0}));

    // hamm.on('panmove', function(event) {
    //     if ($(window).outerWidth(true) < 768) {
    //         var x = left + event.deltaX,
    //             w = Math.round($('.b-menu').outerWidth() * -0.87);

    //         x = x > w ? x : w;
    //         x = x < 0 ? x : 0;

    //         $('.b-menu').css('transform', 'translateX(' + x + 'px)');

    //     } else {
    //         $('.b-menu').css('transform', 'translateX(0)');
    //     }
    // });

    // hamm.on('panend', function(event) {
    //     left = $('.b-menu').css('transform').replace(', 0)', '');
    //     left = parseInt(left.replace('matrix(1, 0, 0, 1, ', ''));
    // });
});

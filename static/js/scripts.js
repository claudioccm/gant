$(document).ready(function($) {
    
$('.tweetable').click(function() {
    function success(data) {
        text = encodeURIComponent(text.slice(0, 124) + ' #opengov - ' + data.id);

        window.open(url2 + text, '_blank', 'width=450, height=300');
    }

    var text = $(this).text(),
        url1 = 'https://www.googleapis.com/urlshortener/v1/url?key=',
        url2 = 'https://twitter.com/intent/tweet?lang=en&count=none&text=';

    $.ajax({
        url: url1 + 'AIzaSyBnpHRDUZhCruzPnmNrN6U_KikY_28-61Q',
        type: 'POST',
        data: JSON.stringify({'longUrl': window.location.href}),
        success: success,
        dataType: 'json',
        contentType: 'application/json; charset=utf-8'
    });
});

$('.e-mobile-menu-trigger').click(function() {
    $('.b-menu').toggleClass('m-active');
    $('#overlay').toggleClass('m-active');
});

$('#overlay').click(function() {
    $('.b-menu').removeClass('m-active');
    $(this).removeClass('m-active');
});

// var hammertime = new Hammer('#menu', myOptions);
// hammertime.on('swipe', function(ev) {
//     console.log(ev);
// });

});
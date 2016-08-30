var $ = jQuery;
$(document).ready(function() {
    var $ = jQuery;
    console.log('animation.js worked');

    $('.y-action-btn').click(function (e) {
        var $ = jQuery;

        if ($(this).attr('state') == 'open') {
            $selector = $(this).attr('data-default');
            if ($($selector)) {
                $($selector).stop().animate({
                    'left' : '0'
                }, 300);
            }

            $selector = $(this).attr('data-block');
            if ($($selector)) {
                $($selector).stop().animate({
                    'left' : '100vw'
                }, 300);
            }
            $(this).attr('state', 'close');
        }
        else {
            $selector = $(this).attr('data-default');
            if ($($selector)) {
                $($selector).stop().animate({
                    'left' : '-100vw'
                }, 300);
            }

            $selector = $(this).attr('data-block');
            if ($($selector)) {
                $($selector).stop().animate({
                    'left' : '0'
                }, 300);
            }
            $(this).attr('state', 'open');
        }
    });

    $('[data-close]').click(function(e) {
        e.stopPropagation();
        e.preventDefault();

        var $selector = $(this).attr('data-close');

        if ($($selector).attr('data-action-btn')) {
            $selector = $($selector).attr('data-action-btn');
            $($selector).click();
        }

        if ($(this).attr('data-action')) {
            $($(this).attr('data-action')).submit();
        }
    });
});
(function ($) {
    "use strict";

    // Spinner
    var spinner = function () {
        setTimeout(function () {
            if ($('#spinner').length > 0) {
                $('#spinner').removeClass('show');
            }
        }, 1);
    };
    spinner();
    
    
    // Initiate the wowjs
    new WOW().init();


    // Fixed Navbar
    $(window).scroll(function () {
        if ($(window).width() < 992) {
            if ($(this).scrollTop() > 45) {
                $('.fixed-top').addClass('bg-white shadow');
            } else {
                $('.fixed-top').removeClass('bg-white shadow');
            }
        } else {
            if ($(this).scrollTop() > 45) {
                $('.fixed-top').addClass('bg-white shadow').css('top', -45);
            } else {
                $('.fixed-top').removeClass('bg-white shadow').css('top', 0);
            }
        }
    });
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 300) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });


    // Testimonials carousel
    
    $(".testimonial-carousel").owlCarousel({
        autoplay: true,
        smartSpeed: 1000,
        margin: 25,
        loop: true,
        center: true,
        dots: false,
        nav: true,
        navText : [
            '<i class="bi bi-chevron-left"></i>',
            '<i class="bi bi-chevron-right"></i>'
        ],
        responsive: {
            0:{
                items:1
            },
            768:{
                items:2
            },
            992:{
                items:3
            }
        }
    });

    
})(jQuery);

// ajax emplement for product increase, dicrease and remove btn.

$('.plus-cart').click(function () {
   let id = $(this).attr('pid').toString()
   let elm = this.parentNode.children[2]

   $.ajax({
    type : 'GET',
    url  : '/pluscart/',
    data : {
        'prod_id' : id,
    },

    success: function (data) {
        elm.innerText = data.quantity
        document.getElementById('amount').innerText = data.amount
        document.getElementById('totalamount').innerText = data.totalamount

    }

   })

});

// minus product and price
$('.minus-cart').click(function () {
    let id = $(this).attr('pid').toString()
    let elm = this.parentNode.children[2]
 
    $.ajax({
     type : 'GET',
     url  : '/minuscart/',
     data : {
         'prod_id' : id,
     },
 
     success: function (data) {
         elm.innerText = data.quantity
         document.getElementById('amount').innerText = data.amount
         document.getElementById('totalamount').innerText = data.totalamount
 
     }
 
    })
 
 });
 
 // remove cart
 $('.remove-btn').click(function () {
    let id = $(this).attr('pid').toString()
    let remove = $('#remove')
    
    $.ajax({
     type : 'GET',
     url  : '/removecart/',
     data : {
         'prod_id' : id,
     },
 
     success: function (data) {
         document.getElementById('amount').innerText = data.amount
         document.getElementById('totalamount').innerText = data.totalamount

         remove.remove()

     }
 
    })
 
 });
 
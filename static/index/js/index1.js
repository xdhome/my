$(function () {

    var mySwiper = new Swiper('.swiper-container', {
        pagination: '.swiper-pagination',
        paginationClickable: true,
        spaceBetween: 5,
        centeredSlides: true,
        autoplay: 2500,
        autoplayDisableOnInteraction: false,
        loop: true,
    });
    $(".swiper-container").mouseenter(function () {//滑过悬停
    mySwiper.stopAutoplay();
}).mouseleave(function(){//离开开启
    mySwiper.startAutoplay();
});
})
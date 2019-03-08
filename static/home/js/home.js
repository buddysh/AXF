$(function () {
    $('.home').width(innerWidth)
    var swiper = new Swiper('#topSwiper', {
        pagination: '.swiper-pagination',
        paginationClickable: '.swiper-pagination',
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        spaceBetween: 30,
        autoplay: 2500,
        loop:true
    });
    console.log('aaaaa');
});


$(function () {
    var swiper = new Swiper('#mustbuySwiper', {
        pagination: '.swiper-pagination',
        paginationClickable: '.swiper-pagination',
        // nextButton: '.swiper-button-next',
        // prevButton: '.swiper-button-prev',
        spaceBetween: 5,
        slidesPerView: 3,
        // autoplay: 2500,
        loop:true
    });
    console.log('aaaaa');
});


// $(function () {
//         console.log('abc')
// })
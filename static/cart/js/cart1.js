$(function () {
    $(".cart .subtract").click(function () {
        console.log("click 购物车减操作")
        var cartid = $(".cart .subtract").attr("cartid")
        console.log(cartid)
        $.get('/wykl/subtract/', {"cartid": cartid}, function (response) {
            console.log("AJAX")
        })
    })
})
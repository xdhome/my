$(function () {
    $(".cart .subtract").click(function () {
        console.log("click 购物车减操作")
        var cartid = $(".cart .subtract").attr("cartid")
        console.log(cartid)
        var $that = $(this)
        $.get("/wykl/subtract/",{"cartid": cartid,},function (response) {
            console.log("AJAX")
            var number = response.number
            console.log(number)
            $that.prev().val(number)
            window.open("/wykl/cart/", target="_self")
        })
    })

    $(".cart .addcart1").click(function () {
        console.log("click 购物车加操作")
        var cartid = $(".cart .subtract").attr("cartid")
        console.log(cartid)
        var $that = $(this)
        $.get("/wykl/addcart1/",{"cartid": cartid,},function (response) {
            console.log("AJAX")
            var number = response.number
            console.log(number)
            $that.prev().val(number)
            window.open("/wykl/cart/", target="_self")
        })
    })

    $(".cart #del .span2").click(function () {
        console.log("click 购物车删除操作")
        var cartid = $(".cart #del .span2").attr("cartid")
        console.log(cartid)
        var goodsid = $(this).attr("goodsid")
        console.log(goodsid,'1111')
        var $that = $(this)
        $.get("/wykl/delcart/",{"cartid": cartid,"goodsid": goodsid},function (response) {
            console.log("AJAX")
            var status = response["status"]
            if (status){

            }
            window.open("/wykl/cart/", target="_self")
        })
    })

    $(".cart .glyphicon").click(function () {
        console.log("click 购物车选中操作")
        var cartid = $(this).attr("cartid")
        console.log(cartid)
        var $that = $(this)
        $.get("/wykl/select/",{"cartid": cartid,},function (response) {
            console.log("AJAX")
            var status = response["status"]
            if (status == 2){

            }
            window.open("/wykl/cart/", target="_self")
        })
    })

})
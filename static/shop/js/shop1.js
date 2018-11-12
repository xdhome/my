$(function () {
    $('.add').click(function () {
        console.log("++++++")
        var num = parseInt($('.ctrnum_wrap input').val())
        console.log(num)
        num += 1
        console.log(num)
        $('.ctrnum_wrap input').val(num)

        })

    $(".raduce").click(function () {
        console.log("-------")
        var num = parseInt($('.ctrnum_wrap input').val())
        console.log(num)
        if (num == 1) {
            num = 1
        }
        else
        {
            num -= 1
        }
        console.log(num)
        $('.ctrnum_wrap input').val(num)
        // $.get("/wykl/raducecart/",{"goodsid": goodsid},function (request) {
        //     console.log("AJAX")
    })
    $(".addcart").click(function () {
        console.log("加入")
        var number = $('.ctrnum_wrap input').val()
        console.log(number)
        var goodsid = $(".addcart").attr('goodsid')
        console.log(goodsid)
        $.get("/wykl/addcart/",{"goodsid": goodsid, "number": number},function (response) {
            console.log("AJAX")
            console.log(response["msg"])
            if (response["status"] == 1){
                window.open("/wykl/index/", target = "_self")
            }
            // else if (response["status"] == -1){
            //
            // }
        })
    })
})
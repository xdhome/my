// alert("111111")

$(function(){
    alert("111111")
    $('img').each(function(){
        var imgpath = $(this).attr('src')
        imgpath = "{% static '" + imgpath +  "' %}"
        $(this).attr('src', imgpath)
    })

    console.log($('body').html())
})

// alert("111111")

// $(function () {
//     $('img').each(function () {
//         let imgputh = $(this).attr('src')
//
//         console.log(imgputh)

        // imgputh = "{% static '" + imgputh + "' %}"
        // $(this).attr('src', imgputh)
    // })
    // alert("111111")
// })
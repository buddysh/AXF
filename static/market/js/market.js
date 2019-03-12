// $(function () {
//
//     $('.type-slider li').click(function () {
//         var ids=$(this).attr("id")
//         $.post('',{num:ids},function (data) {
//             console.log(data['goods'])
//
//             $.each(data['goods'],function (i,item) {
//                 img=item['productimg']
//                 // $('.content-wrapper img').attr('src',img)
//                 console.log(i,img)
//             })
//
//         })
//     })
// })

$(function () {

    $('.market').width(innerWidth)

    var index = $.cookie('index')
    if (index) { // 有点击，有下标
        $('.type-slider li').eq(index).addClass('active')
    } else {
        $('.type-slider li:first').addClass('active')
    }

    $('.type-slider li').click(function () {
        // $(this)  当前点击的对象
        // $(this).addClass('active')

        // 解决: 点击后，记录下标
        // localStorage.setItem('index', $(this).index())
        $.cookie('index', $(this).index(), {expires: 3, path: '/'})
    })


    $('#catgory-view').parent().hide()
    $('#sort-view').parent().hide()

    var catgoryShow = false
    $('#catgory-bt').click(function () {
        catgoryShow = !catgoryShow
        // if (catgoryShow) {
        //     categoryShow()
        // } else {
        //     categoryHide()
        // }
        catgoryShow ? categoryShow():categoryHide()
    })

    var sorShow = false
    $('#sort-bt').click(function () {
        sorShow = !sorShow
        // if (sorShow) {
        //     sortShow()
        // } else {
        //     sortHide()
        // }

        sorShow?sortShow():sortHide()
    })

    function sortShow() {
        catgoryShow = false
        categoryHide()
        // $('#sort-view').parent().addClass('bounce-view')
        $('#sort-view').parent().show()
        $('#sort-bt i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    }

    function sortHide() {
        // $('#sort-view').hide()
        // $('#sort-view').parent().removeClass('bounce-view')
        $('#sort-view').parent().hide()
        $('#sort-bt i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    }

    function categoryHide() {
        // $('#catgory-view').hide()
        // $('#catgory-view').parent().removeClass('bounce-view')
        $('#catgory-view').parent().hide()
        $('#catgory-bt i').removeClass('glyphicon glyphicon-chevron-down').addClass('glyphicon glyphicon-chevron-up')
    }

    function categoryShow() {
        sortHide()
        sorShow = false
        // $('#sort-view').show()
        // $('#catgory-view').parent().addClass('bounce-view')
        $('#catgory-view').parent().show()

        $('#catgory-bt i').removeClass('glyphicon glyphicon-chevron-up').addClass('glyphicon glyphicon-chevron-down')
    }


    $('.bt-wrapper .num').each(function () {
        var num = parseInt($(this).html())
        if (num){
            $(this).prev().show()
            $(this).show()
        }
        else {
            $(this).prev().hide()
            $(this).hide()
        }

    })

    //加操作
    $('.bt-wrapper #plus').click(function () {

        request_data={
            'goodsid':$(this).attr('data-goodsid')
        }

        var $that=$(this)
        console.log(request_data)
        console.log('22222222222222222222')
        $.get('/axf/addcart/',request_data,function(response) {
            console.log(response)
            if (response.status == -1){ // 未登录
                // 设置cookie
                $.cookie('back', 'market', {expires: 3, path: '/'})

                window.open('/axf/login/', '_self')

            } else  if (response.status ==1 ) { // 操作成功

                $that.prev().html(response.number)

                // 设置显示
                $that.prev().show()
                console.log($that.prev())
                console.log(response.status)
                $that.prev().prev().show()
            }

        })
    })




    $('.bt-wrapper #minus').click(function () {

    })


})

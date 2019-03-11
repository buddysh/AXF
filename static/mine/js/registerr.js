$(function () {
    $('.register').width(innerWidth)



    $('#email-id>input').blur(function () {
        var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$");
        // console.log($(this).val())
        request_data = {
                'email': $(this).val()
            }
        if (!reg.test($(this).val())){
            $('#email-t').attr('data-content',"邮箱格式不正确").popover('show')
            console.log($(this).val())
        }
        else {

            $.get('/axf/checkemail',request_data,function (response) {
                console.log(response)
                $('#email-t').attr('data-content',response.msg).popover('show')
            })
        }

    })

    $('#password-id>input').blur(function () {
        var reg=new RegExp("^[a-zA-Z0-9]{6,10}$");
        // console.log($(this).val())
        if (!reg.test($(this).val())){
            $('#pass-t').attr('data-content',"密码位数不够").popover('show')
            console.log($(this).val())
        }

    })

    $('#password-id2>input').blur(function () {
        if ($(this).val() !== $('#password-id>input').val() ){
            $('#pass-t2').attr('data-content',"密码不一致").popover('show')
            console.log($(this).val())
        }

    })



})




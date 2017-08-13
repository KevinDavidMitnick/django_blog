/*
 *
 * login-register modal
 * Autor: Creative Tim
 * Web-autor: creative.tim
 * Web script: #
 */
function showRegisterForm(){
    $('.loginBox').fadeOut('fast',function(){
        $('.registerBox').fadeIn('fast');
        $('.login-footer').fadeOut('fast',function(){
            $('.register-footer').fadeIn('fast');
        });
        $('.modal-title').html('Register with');
    });
    $('.error').removeClass('alert alert-danger').html('');
}
function showLoginForm(){
    $('#loginModal .registerBox').fadeOut('fast',function(){
        $('.loginBox').fadeIn('fast');
        $('.register-footer').fadeOut('fast',function(){
            $('.login-footer').fadeIn('fast');
        });
        $('.modal-title').html('Login with');
    });
     $('.error').removeClass('alert alert-danger').html('');
}

function openLoginModal(){
    showLoginForm();
    setTimeout(function(){
        $('#loginModal').modal({backdrop: 'static', keyboard: false});
        $('#loginModal').modal('show');
    }, 230);
}
function openRegisterModal(){
    showRegisterForm();
    setTimeout(function(){
        $('#loginModal').modal({backdrop: 'static', keyboard: false});
        $('#loginModal').modal('show');
    }, 230);
}

function shakeModal(){
    $('#loginModal .modal-dialog').addClass('shake');
    $('.error').addClass('alert alert-danger').html("请输入正确的用户名/邮箱 和密码进行登录!");
    $('input[type="password"]').val('');
    setTimeout( function(){
        $('#loginModal .modal-dialog').removeClass('shake');
    }, 1000 );
}

function shakeRegisterModal(){
    $('#loginModal .modal-dialog').addClass('shake');
    $('.error').addClass('alert alert-danger').html("请输入正确的用户名/邮箱 和密码进行注册!");
    $('input[type="password"]').val('');
    setTimeout( function(){
        $('#loginModal .modal-dialog').removeClass('shake');
    }, 1000 );
}

function loginAjax(){
    /*   Remove this comments when moving to server
    $.post( "/login", function( data ) {
            if(data == 1){
                window.location.replace("/home");
            } else {
                 shakeModal();
            }
        });
    */

/*   Simulate error message from the server   */
    if (document.referrer.indexOf('login') >=0 && (document.referrer.indexOf(window.location.href) >=0 || window.location.href.indexOf(document.referrer))){
        shakeModal();
    }
}

function registerAjax(){
    /*   Simulate error message from the server   */
    if (document.referrer.indexOf('register') >=0 && (document.referrer.indexOf(window.location.href) >=0 || window.location.href.indexOf(document.referrer))){
        shakeRegisterModal();
    }
}

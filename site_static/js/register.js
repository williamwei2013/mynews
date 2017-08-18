
$(document).ready(function(){
$("#tijiao").submit(function(){  
var email
email=$("#email").val()
$.ajax({  
type:"POST",  
url:"/register_check/",  
data:{email:email},  
dataType:"json",  
success: function(data) {  
	if(data == 1 ){
		        		$('#result').html('邮箱可用');
		        	}
		            if(data == -1  ){
		            $('#result').html('邮箱已注册');
		            }
		        },
		        error: function() {
		            $('#result').html('请求失败，请刷新页面后重试');
		        }
		    });
return false;
});
$("#email").bind('input porpertychange',function(){
$('#result').html('');
});
});
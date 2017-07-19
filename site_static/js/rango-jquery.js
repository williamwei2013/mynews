$(document).ready( function() {

    
    $('#likes').click(function(){
    var artid;
    catid = $(this).attr("data-catid");
    $.get('/rango/like_category/', {category_id: catid}, function(data){
               $('#like_count').html(data);
               //$('#likes').hide();
    });
    

    });
});

$(document).ready( function() {

    
    $('#likes').click(function(){
    var artid;
    artid = $(this).attr("data-artid");
    $.get('/news/like_article/', {article_id: artid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
    });
});



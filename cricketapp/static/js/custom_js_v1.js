
function myFunction(id){
    document.getElementById('id01').style.display='block'
    $("#deleteteam").click(function(){
          document.getElementById("form_id").action = '/delete-team/'+ id +'/'
          document.getElementById("form_id").method = 'POST'
    })
}

function imageclick(imageurl){
    $('.imagepreview').attr('src', imageurl);
    $('.imagepreview').attr('width', '100%');
    $('.imagepreview').attr('height', '100%');
    $('#imagemodal').modal('show');
}
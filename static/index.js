// ONLOAD ---------------------------------------------------------
window.onload = function() {
    
    // To update without reloading the page
    $('form').on('submit', function (e) {
        e.preventDefault();
        var data = new FormData();
        data.append("newUserEmail", $("#userEmail").val());
        data.append("oldUserEmail", $("#currentEmail").html().toString().replace('Email : ', ''));
        $.ajax({
            url : '/update', type: 'POST', data: data, cache : false, contentType: false, processData: false,
            success: function (response) {
                // console.log(response);
                $('#ajaxMessage').html(response);
                $('#closeBTN').trigger('click');
                $("#currentEmail").html('Email : '+$("#userEmail").val());
            }, error: function(e){
            //    console.log(e);
               $('#ajaxMessage').html(e);
            }
        });            
    });
}
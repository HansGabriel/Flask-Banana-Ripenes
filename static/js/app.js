console.log('javascript starting')

$(function() {
    $('#submit').click(function() {
        event.preventDefault();
        const img = $('#uploadform')[0]
        // const img = $('#imgInput').files[0]
        var form_data = new FormData(img);
        console.log(form_data)
        $.ajax({
            type: 'POST',
            url: '/uploadajax',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function(data, textStatus, jqXHR){
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
            console.log('Success!');
            $("#resultFilename").text(data['name']);
            $("#resultClassType").text(data['classType']);
        }).fail(function(data){
            alert('error!');
        });
    });
}); 
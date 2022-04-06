let old_form = false;
//$('.msg_history').append('<p>asd</p>');

$('.inbox_chat').click(function (event) {
    const form = event.target.closest('.messageForm');
    // создаем AJAX-вызов
    receiverId = $(form).serializeArray()[0]['value']
    if(form === null || form.classList.contains('active_chat')){
        return;
    }
    $
    .ajax({
        data: $(form).serialize(), // получаем данные формы
        url: "messages/ajax",
        // если успешно, то
        success: function (response) {
        answer = JSON.parse(response.msg)
        if (old_form){
        old_form.classList.toggle('active_chat')
        }
        form.classList.toggle('active_chat')
        old_form = form
         $('.msg_history').empty();
       for(let i = 0; i < answer.length; i++) {
       var newDate = new Date(answer[i]["fields"]["date"])
       if (answer[i]['fields']['author'] == $('#userId').val()){
          let incoming = '<div class="incoming_msg"><div class="received_msg"><div class="received_withd_msg"><p>' +  answer[i]["fields"]["content"] + '</p><span class="time_date">' +  newDate.toDateString() + '</span></div></div></div>'
          $('.msg_history').append(incoming);
       }
       else{
            let outcoming = '<div class="outgoing_msg"><div class="sent_msg"><p>' +  answer[i]["fields"]["content"] + '</p><span class="time_date">' + newDate.toDateString() + '</span></div></div>'
            $('.msg_history').append(outcoming);
       }
       }
       var div = $(".msg_history");
       div.scrollTop(div.prop('scrollHeight'));
       $("#receiver").val(receiverId)

        },
        // если ошибка, то
        error: function (response) {
            // предупредим об ошибке
            console.log(response.responseJSON.errors)
        }
    });
    return false;
});


 let url = `ws://${window.location.host}/ws/socket-server/`
        const chatSocket = new WebSocket(url)

        chatSocket.onmessage = function(e){
            let data = JSON.parse(e.data)
            console.log('Data:', data)

            if(data.type === 'chat'){
                 if (data.receiver == $('#currentUser').val()){
                  let incoming = '<div class="incoming_msg"><div class="received_msg"><div class="received_withd_msg"><p>' +  data.content + '</p><span class="time_date"> 11:01 AM    |    June 9</span></div></div></div>'

                          $('.msg_history').append(incoming);

                       }
                       else{
                            let outcoming = '<div class="outgoing_msg"><div class="sent_msg"><p>' +  data.content + '</p><span class="time_date"> 11:01 AM    |    June 9</span></div></div>'

                            $(".msg_history").append(outcoming);
                       }

                 var div = $(".msg_history");
                 div.scrollTop(div.prop('scrollHeight'));
            }
        }

        let form = document.getElementById('form')
        form.addEventListener('submit', (e)=> {
            e.preventDefault()
            let content = e.target.content.value
            let author = e.target.author.value
            let receiver = e.target.receiver.value
            chatSocket.send(JSON.stringify({
                'content':content,
                'author': author,
                'receiver':receiver,
            }))
            form.reset()
        })

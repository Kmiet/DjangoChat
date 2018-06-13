function connectChannel(channelID, user) {

    var chatSocket = new WebSocket('ws://' + window.location.host + ':6543' + '/ws/channel/' + channelID + '/');

    var previous = '';



    chatSocket.onmessage = function(e) {

        var data = JSON.parse(e.data);

        var author = data['name'];

        var colour = data['colour'];

        var message = data['message'];

        var prev = data['prev'];

        var is_prev_author = (previous == author);


        var element = document.createElement('div');

        element.classList.add('chat_main_section');



        if(is_prev_author) {

            element.classList.add('chat_prev_me');

        }



        var chat_msg = document.createElement('div');



        if(user.name == author) {

            chat_msg.classList.add('chat_my_msg_cont');

            chat_msg.innerHTML = message;

        } else {

            if(!is_prev_author) {

                //var chat_user_block = document.createElement('div');

                //chat_user_block.classList.add('chat_other_name_cont');



                var chat_username = document.createElement('div');

                chat_username.classList.add('chat_user_name');

                chat_username.setAttribute('style', 'color: ' + colour + ';');

                chat_username.innerHTML = author;



                var filler = document.createElement('div')

                filler.classList.add('chat_filler');

                //chat_user_block.appendChild(chat_username);

                element.appendChild(chat_username);

                element.appendChild(filler);

            }



            chat_msg.classList.add('chat_other_msg_cont');

            chat_msg.textContent = message;

        }



        element.appendChild(chat_msg);



        chat_log = document.querySelector('#chat-log');

        chat_log.appendChild(element);

        chat_log.scrollTop = chat_log.scrollHeight;

	previous = author;

    };



    chatSocket.onclose = function(e) {

        console.error('Chat socket closed unexpectedly');

    };



    document.querySelector('#chat-message-input').focus();

    document.querySelector('#chat-message-input').onkeyup = function(e) {

        if (e.keyCode === 13) {

            document.querySelector('#chat-message-submit').click();

        }

    };



    document.querySelector('#chat-message-submit').onclick = function(e) {

        var messageInputDom = document.querySelector('#chat-message-input');

        var message = messageInputDom.value;

        if(message != '') {

            chatSocket.send(JSON.stringify({

                'name': user.name,

                'colour': user.colour,

                'message': message,

                'prev': previous

            }));

        }

        messageInputDom.value = '';

    };

}
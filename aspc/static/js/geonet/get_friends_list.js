$.ajax({
    url:'/api/maps/friends',
    success: function(data){
        for(i in data){
            var friend = data[i];
            $('.friends-ul').append('<li>'+friend.first_name+' '+friend.last_name+'</li>');
        }
    },
    error: function(err){
        console.log(err);
    }
})
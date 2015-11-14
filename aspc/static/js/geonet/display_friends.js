var friends = {};

function initializeFriends(){
    $.ajax({
        url: '/api/maps/friends',
        method: 'GET',
        success: function(data){
            for(i in data){
                friend = data[i];
                friend_object = new Friend(friend.longitude, friend.latitude, friend.first_name+' '+friend.last_name, map);
                console.log(friend_object);
                friends[friend.username]=friend_object;
            }
        },
        error: function(err){
            console.log(err);
        }
    })
}

function updateFriends(){
    $.ajax({
        url: '/api/maps/friends',
        method: 'GET',
        success: function(data){
            for(i in data){
                friend = data[i];
                friend_object = friends[friend.username];
                friend_object.updateLocation(friend.longitude,friend.latitude);
            }
        },
        error: function(err){
            console.log(err);
        }
    })
}



initializeFriends();
setInterval(updateFriends(),50000);


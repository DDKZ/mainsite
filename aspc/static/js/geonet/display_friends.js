var friends = {};
function initializeFriends(){
    $.ajax({
        url: '/api/maps/friends',
        method: 'GET',
        success: function(data){
            for(i in data){
                friend = data[i];
                friend_object = Friend(friend.longitude, friend.latitude, friend.name, map);
                console.log(friend_object);
                friends[friend.name]=friend_object;
            }
        },
        error: function(err){
            console.log(err);
        }
    })
}
initializeFriends();

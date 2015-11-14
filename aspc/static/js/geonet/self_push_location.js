

function self_push_location(long,lati){
    $.ajax({
    url: '/api/maps/me',
    method: 'PUT',
    data: {'longitude':long.toFixed(5),'latitude':lati.toFixed(5)},
    success: function(){
        //console.log('successfully update self location to '+[long, lati]);
    },
    error: function(err){
        console.log(err);
    }
    })
}


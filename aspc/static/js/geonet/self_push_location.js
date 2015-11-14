function round(num, digit){
    return Math.round(num * 10^digit) / 10^digit;
}

function self_push_location(long,lati){
    $.ajax({
    url: '/api/maps/me',
    method: 'PUT',
    data: {'longitude':round(long,5),'latitude':round(lati,5)},
    success: function(){
        console.log('successfully update self location');
    },
    error: function(err){
        console.log(err);
    }
    })
}


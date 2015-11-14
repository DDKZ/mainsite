$.ajax({
    url: '/api/maps/me',
    method: 'POST',
    data: {'longitude':long,'latitude':lati},
    success: function(){
        console.log('successfully update self location');
    },
    error: function(){
        console.log('fail to update self location');
    }
})

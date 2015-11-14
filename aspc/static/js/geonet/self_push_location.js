$.ajax({
    url: '/geonet/self-update/',
    data: {'long':long,'lati':lati},
    success: function(){
        console.log('successfully update self location');
    },
    error: function(){
        console.log('fail to update self location');
    }
})

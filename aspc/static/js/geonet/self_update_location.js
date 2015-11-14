        var self_update_interval = 2000;
        var long = 0
        var lati = 0;
        function getLocation() {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(updatePosition);
            } else {
               alert('failed to get location from your browser')
            }
        }
        function updatePosition(position) {
            lati = position.coords.latitude;
            long = position.coords.longitude;
        }


        var marker = L.marker([34.10079, -117.71008]).addTo(map);

        setInterval(function() {
            getLocation();
            if (long !=0 || lati !=0) {
                map.setView([lati, long], 17);
                marker.setLatLng([lati, long]);
                console.log([lati, long]);
            }
        }, self_update_interval);

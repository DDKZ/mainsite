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


        var self_marker = L.marker([34.10079, -117.71008]).addTo(map);
        self_marker.bindPopup("me").openPopup();

        setInterval(function() {
            getLocation();
            if (long !=0 || lati !=0) {
                self_marker.setLatLng([lati, long]).update();
                map.setView([lati,long],18);
                self_push_location(long,lati);
            }
        }, self_update_interval);

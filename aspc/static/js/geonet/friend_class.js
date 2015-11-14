function Friend (longitude,latitude,name,map) {

    this.longitude = longitude;
    this.latitude = latitude;
    this.marker =  L.marker([this.longitude, this.latitude]).addTo(map);

  //  marker.bindPopup(this.name).openPopup();
    this.name = name;

    this.updateLocation = function(new_longitude,new_latitude) {
        this.longitude = new_longitude;
        this.latitude = new_latitude;
       // this.marker.setLatLng([this.latitude, this.longitude]);
    };
}
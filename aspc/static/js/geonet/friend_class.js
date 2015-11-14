var Friend = function(longitude,latitude,name,map) {

    this.longitude = longitude;
    this.latitude = latitude;
    this.name = name;
    this.marker =  L.marker([this.longitude, this.latitude],{ icon: new L.Icon.Label.Default({ labelText: this.name }) }).addTo(map);

    this.updateLocation = function(new_longitude,new_latitude) {
        this.longitude = new_longitude;
        this.latitude = new_latitude;
        this.marker.setLatLng([this.latitude, this.longitude]).update();
    };
}
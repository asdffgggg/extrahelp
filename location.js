navigator.geolocation.getCurrentPosition(
    (pos) => {
        document.getElementById("lat").value = pos.coords.latitude
        document.getElementById("lon").value = pos.coords.longitude
    },
    (error) => console.log(error),
    {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 0
    }
)
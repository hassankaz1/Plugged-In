function initMap(data) {

    const lat = document.getElementById("lat")
    const lng = document.getElementById("lng")
    const current_button = document.getElementById("current_button")
    
    const latq = document.getElementById("latq")
    const lngq = document.getElementById("lngq")
    const quick_button = document.getElementById("quick")
    const quickForm = document.getElementById('quickForm')


    const input = document.getElementById("autocomplete");
    const options = {
        componentRestrictions: { country: "us" },
        fields: ["address_components", "geometry", "name"],
        strictBounds: false,
        types: ["establishment"],
    };
    const autocomplete = new google.maps.places.Autocomplete(input, options);


    autocomplete.addListener("place_changed", () => {
        const place = autocomplete.getPlace();
        lat.value = place.geometry.location.lat()
        lng.value = place.geometry.location.lng()
    })

    if(current_button){
    current_button.addEventListener("click", (e) => {
        e.preventDefault()
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    input.value = "using current location"
                    lat.value = position.coords.latitude
                    lng.value = position.coords.longitude
                },
                (error) => {
                    alert(error.message + "\nPLEASE CHECK BROWSER SETTINGS")
                })
        }

    });
}

    quick_button.addEventListener("click", (e) => {
        e.preventDefault()
        
        // Try HTML5 geolocation.
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    latq.value = position.coords.latitude;
                    lngq.value = position.coords.longitude;

                    quickForm.submit();
                },
                (error) => {
                    alert(error.message + "\nPLEASE CHECK BROWSER SETTINGS")
                })
        } 
    });

}






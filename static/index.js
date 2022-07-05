let map;

// function initMap() {

//     mapStyle = [
//         {
//             "featureType": "administrative",
//             "elementType": "all",
//             "stylers": [
//                 {
//                     "visibility": "on"
//                 },
//                 {
//                     "lightness": 33
//                 }
//             ]
//         },
//         {
//             "featureType": "landscape",
//             "elementType": "all",
//             "stylers": [
//                 {
//                     "color": "#f2e5d4"
//                 }
//             ]
//         },
//         {
//             "featureType": "poi.park",
//             "elementType": "geometry",
//             "stylers": [
//                 {
//                     "color": "#c5dac6"
//                 }
//             ]
//         },
//         {
//             "featureType": "poi.park",
//             "elementType": "labels",
//             "stylers": [
//                 {
//                     "visibility": "on"
//                 },
//                 {
//                     "lightness": 20
//                 }
//             ]
//         },
//         {
//             "featureType": "road",
//             "elementType": "all",
//             "stylers": [
//                 {
//                     "lightness": 20
//                 }
//             ]
//         },
//         {
//             "featureType": "road.highway",
//             "elementType": "geometry",
//             "stylers": [
//                 {
//                     "color": "#c5c6c6"
//                 }
//             ]
//         },
//         {
//             "featureType": "road.arterial",
//             "elementType": "geometry",
//             "stylers": [
//                 {
//                     "color": "#e4d7c6"
//                 }
//             ]
//         },
//         {
//             "featureType": "road.local",
//             "elementType": "geometry",
//             "stylers": [
//                 {
//                     "color": "#fbfaf7"
//                 }
//             ]
//         },
//         {
//             "featureType": "water",
//             "elementType": "all",
//             "stylers": [
//                 {
//                     "visibility": "on"
//                 },
//                 {
//                     "color": "#acbcc9"
//                 }
//             ]
//         }
//     ]

//     map = new google.maps.Map(document.getElementById("map"), {
//         center: { lat: 40.648926, lng: -73.791323 },
//         zoom: 12,
//         mapTypeControlOptions: {
//             mapTypeIds: ['roadmap']
//         },
//         styles: mapStyle
//     });
// }



function initMap(data) {

    mapStyle = [
        {
            "featureType": "all",
            "elementType": "geometry",
            "stylers": [
                {
                    "color": "#ffffff"
                }
            ]
        },
        {
            "featureType": "all",
            "elementType": "labels.text.fill",
            "stylers": [
                {
                    "gamma": 0.01
                },
                {
                    "lightness": 20
                }
            ]
        },
        {
            "featureType": "all",
            "elementType": "labels.text.stroke",
            "stylers": [
                {
                    "saturation": -31
                },
                {
                    "lightness": -33
                },
                {
                    "weight": 2
                },
                {
                    "gamma": 0.8
                }
            ]
        },
        {
            "featureType": "all",
            "elementType": "labels.icon",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "administrative.locality",
            "elementType": "labels.text.fill",
            "stylers": [
                {
                    "color": "#050505"
                }
            ]
        },
        {
            "featureType": "administrative.locality",
            "elementType": "labels.text.stroke",
            "stylers": [
                {
                    "color": "#fef3f3"
                },
                {
                    "weight": "3.01"
                }
            ]
        },
        {
            "featureType": "administrative.neighborhood",
            "elementType": "labels.text.fill",
            "stylers": [
                {
                    "color": "#0a0a0a"
                },
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "administrative.neighborhood",
            "elementType": "labels.text.stroke",
            "stylers": [
                {
                    "color": "#fffbfb"
                },
                {
                    "weight": "3.01"
                },
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "landscape",
            "elementType": "geometry",
            "stylers": [
                {
                    "lightness": 30
                },
                {
                    "saturation": 30
                }
            ]
        },
        {
            "featureType": "poi",
            "elementType": "geometry",
            "stylers": [
                {
                    "saturation": 20
                }
            ]
        },
        {
            "featureType": "poi.attraction",
            "elementType": "labels.icon",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "poi.park",
            "elementType": "geometry",
            "stylers": [
                {
                    "lightness": 20
                },
                {
                    "saturation": -20
                }
            ]
        },
        {
            "featureType": "road",
            "elementType": "geometry",
            "stylers": [
                {
                    "lightness": 10
                },
                {
                    "saturation": -30
                }
            ]
        },
        {
            "featureType": "road",
            "elementType": "geometry.stroke",
            "stylers": [
                {
                    "saturation": 25
                },
                {
                    "lightness": 25
                }
            ]
        },
        {
            "featureType": "road.highway",
            "elementType": "geometry.fill",
            "stylers": [
                {
                    "visibility": "on"
                },
                {
                    "color": "#a1a1a1"
                }
            ]
        },
        {
            "featureType": "road.highway",
            "elementType": "geometry.stroke",
            "stylers": [
                {
                    "color": "#292929"
                }
            ]
        },
        {
            "featureType": "road.highway",
            "elementType": "labels.text.fill",
            "stylers": [
                {
                    "visibility": "on"
                },
                {
                    "color": "#202020"
                }
            ]
        },
        {
            "featureType": "road.highway",
            "elementType": "labels.text.stroke",
            "stylers": [
                {
                    "visibility": "on"
                },
                {
                    "color": "#ffffff"
                }
            ]
        },
        {
            "featureType": "road.highway",
            "elementType": "labels.icon",
            "stylers": [
                {
                    "visibility": "simplified"
                },
                {
                    "hue": "#0006ff"
                },
                {
                    "saturation": "-100"
                },
                {
                    "lightness": "13"
                },
                {
                    "gamma": "0.00"
                }
            ]
        },
        {
            "featureType": "road.arterial",
            "elementType": "geometry.fill",
            "stylers": [
                {
                    "visibility": "on"
                },
                {
                    "color": "#686868"
                }
            ]
        },
        {
            "featureType": "road.arterial",
            "elementType": "geometry.stroke",
            "stylers": [
                {
                    "visibility": "off"
                },
                {
                    "color": "#8d8d8d"
                }
            ]
        },
        {
            "featureType": "road.arterial",
            "elementType": "labels.text.fill",
            "stylers": [
                {
                    "visibility": "on"
                },
                {
                    "color": "#353535"
                },
                {
                    "lightness": "6"
                }
            ]
        },
        {
            "featureType": "road.arterial",
            "elementType": "labels.text.stroke",
            "stylers": [
                {
                    "visibility": "on"
                },
                {
                    "color": "#ffffff"
                },
                {
                    "weight": "3.45"
                }
            ]
        },
        {
            "featureType": "road.local",
            "elementType": "geometry.fill",
            "stylers": [
                {
                    "color": "#d0d0d0"
                }
            ]
        },
        {
            "featureType": "road.local",
            "elementType": "geometry.stroke",
            "stylers": [
                {
                    "lightness": "2"
                },
                {
                    "visibility": "on"
                },
                {
                    "color": "#999898"
                }
            ]
        },
        {
            "featureType": "road.local",
            "elementType": "labels.text.fill",
            "stylers": [
                {
                    "color": "#383838"
                }
            ]
        },
        {
            "featureType": "road.local",
            "elementType": "labels.text.stroke",
            "stylers": [
                {
                    "color": "#faf8f8"
                }
            ]
        },
        {
            "featureType": "water",
            "elementType": "all",
            "stylers": [
                {
                    "lightness": -20
                }
            ]
        }
    ]

    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: data[0]['lat'], lng: data[0]['lng'] },
        zoom: 12,
        mapTypeControlOptions: {
            mapTypeIds: ['roadmap']
        },
        styles: mapStyle
    });

    var marker;

    for (i = 1; i < data.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(parseInt(data[i][`latitude`]), parseInt(data[i][`longitude`])),
            map: map,
            title: data[i][`address`],

        })
    }



}








window.initMap = initMap;
var FeedbackApp = FeedbackApp || {};

// Restaurants Collection
FeedbackApp.Restaurants = new Backbone.Collection;
FeedbackApp.Restaurants.url = '/api/location/restaurants';
FeedbackApp.Restaurants.parse = function(data) {return data.locations};

// Recipients Collection
FeedbackApp.Recipients = new Backbone.Collection;
FeedbackApp.Recipients.url = '/api/location/recipients';
FeedbackApp.Recipients.parse = function(data) {return data.locations};

(FeedbackApp.updateMap = function() {
  _.each(FeedbackApp.Restaurants.models, function(el) {
    FeedbackApp.addMarker(el.attributes);
  });
  _.each(FeedbackApp.Recipients.models, function(el) {
    FeedbackApp.addMarker(el.attributes);
  });
});

(FeedbackApp.addMarker = function(location) {
  location.marker = new google.maps.Marker({
    position: new google.maps.LatLng(location.lat, location.lng),
    title: location.street_address
  });
  location.marker.setMap(map);
});


(FeedbackApp.poll = function(){
   setTimeout(function(){
      FeedbackApp.Restaurants.fetch();
      FeedbackApp.Recipients.fetch();
      FeedbackApp.updateMap();
      FeedbackApp.poll();
  }, 2000);
})();

(function() {
  $(document).ready(function() {
    initialize();
  });

  function initialize() {
    var mapOptions = {
      center: { lat: 40.03, lng: -82.98792147636415 },
      zoom: 12
    };

    map = new google.maps.Map(document.getElementById('map-canvas'),
      mapOptions);
  }
})();
var locations=[]
	var div=document.getElementsByClassName("data")
    var numberOfSubArrays=div.length/6;
    var start=0,end=6,m=0;
    tableSelection=0
    for(i=0;i<numberOfSubArrays;i++)
      locations.push([])
    for(j=0;j<locations.length;j++)
    {
      m=0
      for(k=start;k<end;k++)
      {
          locations[j][m]=div[k].innerHTML
          if(m==5 && tableSelection!=1){
            newTableName=locations[j][m]
            selectTableName=document.querySelectorAll('option')
            newTableName=newTableName.substring(0,3)
            if(selectTableName[0].id.substring(0,3)==newTableName){
              document.getElementById('Murder').selected='Murder'
              tableSelection=1
            }
            if(selectTableName[1].id.substring(0,3)==newTableName){
              document.getElementById('Rape').selected='Rape'
              tableSelection=1
            }
            if(selectTableName[2].id.substring(0,3)==newTableName){
              document.getElementById('Robbery').selected='Robbery'
              tableSelection=1
            }
            if(selectTableName[3].id.substring(0,3)==newTableName){
              document.getElementById('Attack').selected='Attack'
              tableSelection=1
            }
          }
          	m++;
       }
          
      start=end
      end=end+6
     } 
     var max=0
     for(var k=0;k<locations.length;k++)
     	if(max<locations[k][4])
     		max=locations[k][4]
     var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: new google.maps.LatLng(12.9716, 77.5946),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();
    var icon = {
    scaledSize: new google.maps.Size(250, 250), // scaled size
    origin: new google.maps.Point(0,0), // origin
    anchor: new google.maps.Point(0, 0) // anchor
};


    var marker, i;

    for (i = 0; i < locations.length; i++) {  
      marker = new google.maps.Marker({
      	icon:icon,
        position: new google.maps.LatLng(locations[i][2],locations[i][3]),
        map: map
      });
      if(locations[i][4]>=0 && locations[i][4]<=2)
      	marker.setIcon('http://maps.google.com/mapfiles/ms/icons/green-dot.png')
      if(locations[i][4]>2 && locations[i][4]<=4)
      	marker.setIcon('http://maps.google.com/mapfiles/ms/icons/yellow-dot.png')
      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
        
          {
            
            
            	
            content="<p id='markerContent'>"+locations[i][0]+"<br>"+'Count : '+locations[i][4]+"</p>"
            infowindow.setContent(content);
            infowindow.open(map, marker);
          }
        }
      })(marker, i));
    }
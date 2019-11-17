var locations=[]
    //var div=document.querySelectorAll("td")
    var div=document.getElementsByClassName("data")
    var numberOfSubArrays=div.length/7;
    var start=0,end=7,m=0;
    tableSelection=0
    for(i=0;i<numberOfSubArrays;i++)
      locations.push([])
    for(j=0;j<locations.length;j++)
    {
      m=0
      for(k=start;k<end;k++)
      {
          locations[j][m]=div[k].innerHTML
          if(m==6 && tableSelection!=1){
            newTableName=locations[j][m]
            selectTableName=document.querySelectorAll('option')
            newTableName=newTableName.substring(1,4)
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
      end=end+7
      }
    
    
		

    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: new google.maps.LatLng(12.9716, 77.5946),
      mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    var infowindow = new google.maps.InfoWindow();
    

    var marker, i;

    for (i = 0; i < locations.length; i++) {  
      marker = new google.maps.Marker({
        position: new google.maps.LatLng(locations[i][1], locations[i][2]),
        map: map
      });

      google.maps.event.addListener(marker, 'click', (function(marker, i) {
        return function() {
        
          {
            console.log(locations[0][3])
            locations[i][6]=locations[i][6].substring(1,locations[i][6].length-1)
            locations[i][3]=locations[i][3].substring(1,locations[i][3].length-2)
            content=locations[i][0] + "<br>" +locations[i][5]+"  ,  "+locations[i][4]+ "<br>" + "<a href=" + locations[i][3] + ">Click To View The Article</a>"
            infowindow.setContent(content);
            infowindow.open(map, marker);
          }
        }
      })(marker, i));
    }

var source = new EventSource('/listensForPushes');
    source.onmessage = function(event) {
      var notificationNumber = parseInt(document.getElementById("notificationValue").innerHTML);
      notificationNumber += 1
      document.getElementById("notificationValue").innerHTML = notificationNumber
}
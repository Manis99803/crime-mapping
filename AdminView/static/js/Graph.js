var locations=[]
  	xvalue=[]
  	yvalue=[]
	var div=document.getElementsByClassName("data")
    var numberOfSubArrays=div.length/3;
    var start=0,end=3,m=0;
    tableSelection=0
    for(i=0;i<numberOfSubArrays;i++)
      locations.push([])
    for(j=0;j<locations.length;j++)
    {
      m=0
      for(k=start;k<end;k++)
      {
          locations[j][m]=div[k].innerHTML
          if(m==2 && tableSelection!=1){
            newTableName=locations[j][m]
            selectTableName=document.querySelectorAll('option')
            newTableName=newTableName.substring(0,3)
            if(selectTableName[0].id.substring(0,3)==newTableName){
              document.getElementById('Murder').selected='Murder'
              tableSelection=1
              document.getElementById('GraphTitle').innerHTML='Murder Count Area Wise'
            }
            if(selectTableName[1].id.substring(0,3)==newTableName){
              document.getElementById('Rape').selected='Rape'
              tableSelection=1
              document.getElementById('GraphTitle').innerHTML='Rape Count Area Wise'
            }
            if(selectTableName[2].id.substring(0,3)==newTableName){
              document.getElementById('Robbery').selected='Robbery'
              tableSelection=1
              document.getElementById('GraphTitle').innerHTML='Robbery Count Area Wise'
            }
            if(selectTableName[3].id.substring(0,3)==newTableName){
              document.getElementById('Attack').selected='Attack'
              tableSelection=1
              document.getElementById('GraphTitle').innerHTML='Attack Count Area Wise'
            }
          }m++;
       }
      xvalue.push(locations[j][0])
      yvalue.push(locations[j][1])    
      start=end
      end=end+3
     }
     var data = [
  {
    x: xvalue,
    y: yvalue,
    type: 'bar'
  }
];

Plotly.newPlot('myDiv', data);

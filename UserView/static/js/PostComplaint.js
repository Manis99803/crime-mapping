function raiseError(errorMessage) {
  $("#outputFeedBack").css("display","block")
  $("#outputFeedBack").css("color","#FFFFFF")
  $("#outputFeedBack").html(errorMessage)
}

function extractUserParameters(complaintObject){
    complaintObject["name"] = $("#name").val()
    complaintObject["description"] = $("#description").val()
    complaintObject["crimeType"] = $("#category").val()
    complaintObject["location"] = $("#location").val()
    return complaintObject;
}

function checkForAllParameters(complaintObject){
  if(complaintObject["name"] == '')
      return false;
  if(complaintObject['location'] == '')
      return false;
  if(complaintObject['crimeType'] == '')
      return false;
  if(complaintObject['description'] == '')
      return false;
  return true;
}

$('#post_complaint').on('click', function(e) {
  
  console.log("In post Complaint object");
  var complaintObject = {}
  complaintObject = extractUserParameters(complaintObject);
  if(checkForAllParameters(complaintObject)){
      $.ajax({
        url : 'http://127.0.0.1:5000/api/v1/post_complaint',
        dataType : "json",
        type : "POST",
        contentType: "application/json",
        xhrFields: {withCredentials: false},
        crossDomain: true,
        data: JSON.stringify(complaintObject),
        success: function(data) {
            window.location.href = "http://127.0.0.1:5000/homepage"
        },
        error: function(jqXHR, textStatus, errorThrown) {
          statusCode = (jqXHR.status);
          raiseError("Please provide proper inputs")
        }
      });
  } else {
      raiseError("Please provide proper inputs")
  }           
});
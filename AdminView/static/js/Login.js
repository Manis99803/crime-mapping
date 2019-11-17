function raiseError(errorMessage) {
  $("#outputFeedBack").css("display","block")
  $("#outputFeedBack").css("color","#FFFFFF")
  $("#outputFeedBack").html(errorMessage)
}

function extractUserParameters(userObject){
    userObject["name"] = $("#emailId").val()
    userObject["password"] = $("#password").val()
    return userObject;
}

function checkForAllParameters(userObject){
  if(userObject["name"] == '')
      return false;
  if(userObject['password'] == '')
      return false;
  return true;
}

$('#user_login').on('click', function(e) {
          
  var userObject = {}
  userObject = extractUserParameters(userObject);
  if(checkForAllParameters(userObject)){
      $.ajax({
        url : 'http://127.0.0.1:5001/api/v1/admin_login',
        dataType : "json",
        type : "POST",
        contentType: "application/json",
        xhrFields: {withCredentials: false},
        crossDomain: true,
        data: JSON.stringify(userObject),
        success: function(data) {
            window.location.href = 'http://127.0.0.1:5001/getData'
        },
        error: function(jqXHR, textStatus, errorThrown) {
          statusCode = (jqXHR.status);
          raiseError("The given email id is already registered with us")
        }
      });
  } else {
      raiseError("Please Provide Proper Credentials")
  }           
});
function raiseError(errorMessage) {
  $("#outputFeedBack").css("display","block")
  $("#outputFeedBack").css("color","#FFFFFF")
  $("#outputFeedBack").html(errorMessage)
}

function extractUserParameters(userObject){
    userObject["emailId"] = $("#email").val()
    userObject["password"] = $("#password").val()
    return userObject;
}

function checkForAllParameters(userObject){
  if(userObject["emailId"] == '')
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
        url : 'http://127.0.0.1:5000/api/v1/user_login',
        dataType : "json",
        type : "POST",
        contentType: "application/json",
        xhrFields: {withCredentials: false},
        crossDomain: true,
        data: JSON.stringify(userObject),
        success: function(data) {
            window.location.href = 'http://127.0.0.1:5000/homepage'
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
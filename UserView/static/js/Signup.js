function raiseError(errorMessage) {
  $("#outputFeedBack").css("display","block")
  $("#outputFeedBack").css("color","#FFFFFF")
  $("#outputFeedBack").html(errorMessage)
}

function extractUserParameters(userObject){
    userObject["userName"] = $("#firstName").val();
    userObject["address"] = $("#address").val();
    userObject["place"] = $("#place").val();
    userObject["state"] = $("#state").val();
    userObject["emailId"] = $("#email-Id").val();
    userObject["password"] = $("#password").val();
    return userObject;
}

function checkForAllParameters(userObject){
  if(userObject["userName"] == '')
      return false;
  if(userObject["address"] == '')
      return false;
  if(userObject["place"] == '')
      return false;
  if(userObject["state"] == '')
      return false;
  if(userObject["emailId"] == '')
      return false;
  if(userObject['password'] == '')
      return false;
  return true;
}

function isValidEmailAddress(emailAddress) {
    var pattern = new RegExp(/^(("[\w-+\s]+")|([\w-+]+(?:\.[\w-+]+)*)|("[\w-+\s]+")([\w-+]+(?:\.[\w-+]+)*))(@((?:[\w-+]+\.)*\w[\w-+]{0,66})\.([a-z]{2,6}(?:\.[a-z]{2})?)$)|(@\[?((25[0-5]\.|2[0-4][\d]\.|1[\d]{2}\.|[\d]{1,2}\.))((25[0-5]|2[0-4][\d]|1[\d]{2}|[\d]{1,2})\.){2}(25[0-5]|2[0-4][\d]|1[\d]{2}|[\d]{1,2})\]?$)/i);
    return pattern.test(emailAddress);
};

$('#user_signup').on('click', function(e) {
          
  var userObject = {}
  console.log("in user signup function")
  userObject = extractUserParameters(userObject);
  console.log(userObject)
  if(checkForAllParameters(userObject)){
      $.ajax({
        url : 'http://127.0.0.1:5000/api/v1/user_signup',
        dataType : "json",
        type : "POST",
        contentType: "application/json",
        xhrFields: {withCredentials: false},
        crossDomain: true,
        data: JSON.stringify(userObject),
        success: function(data) {
            window.location.href = 'http://127.0.0.1:5000/login_page'
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


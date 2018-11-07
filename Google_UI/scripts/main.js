function check_input() { 

    var inputValue =document.getElementById("userInput").value; 

    if(inputValue == "") { 
        document.getElementById("message").innerHTML = "Please type something!";
        return false; 
    } else { 
        userInput.onkeydown = function() {
        document.getElementById("message").innerHTML = "";
        }
        document.getElementById("message").innerHTML = "";
        swal({
            // title: "Output", 
            html: inputValue,  
            confirmButtonText: "OK",
            // allowOutsideClick: "true" 
          });
        // alert(inputValue)                
    } 
} 

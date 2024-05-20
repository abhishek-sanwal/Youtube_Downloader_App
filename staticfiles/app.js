
document.addEventListener("DOMContentLoaded",function(){

    //  Function to copy from clipboard using navigation api

    document.querySelector(".paste").addEventListener("click",function paste(){

        // console.log("Event has been triggered")
        navigator.clipboard
        .readText()
        .then((clipText)=>{
            // console.log(clipText);
            document.getElementById("link").value = clipText;
        }
        )
    });

});

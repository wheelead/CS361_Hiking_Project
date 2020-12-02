// Created for CS 361 by team "To Be Determined"
// Chelsea Satterwhite, Adam Wheeler, Diane Nguyen, Colin Kasowski, and Nick Dal

document.addEventListener('DOMContentLoaded', bindButtons);

/* Binding Function for the Buttons
 * Input:   n/a
 * Output:  n/a
 */
function bindButtons(){
    let openObj = document.getElementById("open");
    openObj.addEventListener("click", function(event){
        document.getElementById("myForm").style.display = "block";
    })
    let closeObj = document.getElementById("cancel");
    closeObj.addEventListener("click", function(event){
        document.getElementById("myForm").style.display = "none";
    })
};







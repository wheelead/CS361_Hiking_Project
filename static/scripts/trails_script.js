/*  Programmers:    
 *  Date:           
 *  Assignment:     
 *  Description:    Trails specific script
 */

document.addEventListener('DOMContentLoaded', bindAndBuild);

/* Initiating the binding functions
 * Input:   n/a
 * Output:  n/a
 */

function bindAndBuild(){
    bindButtons();
};

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







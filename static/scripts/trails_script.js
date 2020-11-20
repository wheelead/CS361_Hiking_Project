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
    openObj.addEventListener("click", function(){
        openForm();
    };
    let closeObj = document.getElementById("close");
    openObj.addEventListener("click", function(){
        closeForm();
    };
};

function openForm(){
    document.getElementById("myForm").style.display = "block";
};

function closeForm(){
    document.getElementById("myForm").style.display = "none";
};
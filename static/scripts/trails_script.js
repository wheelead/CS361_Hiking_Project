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

/* Set up the 
 * Input:   n/a
 * Output:  n/a
 * Additional Detail: 
 */
function bindButtons(){
// for loop to go through all buttons as needed?
    let buttonType = "home_btn";
    let obj = document.getElementById(buttonType);
    obj.addEventListener("click", function(){
        location.href = "/";
    });
};




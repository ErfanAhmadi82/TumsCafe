function signup() {
    if(document.getElementById("signup").style.display == "none"){
        document.getElementById("signup").style.display = "inline";
        document.getElementById("conteiner").style.filter="blur(10px)";}
    else{
        document.getElementById("signup").style.display = "none";
        document.getElementById("conteiner").style.filter="blur(0px)";}

    };

function getback(){
    if(document.getElementById("conteiner").style.filter != "blur(0px)"){
        document.getElementById("signup").style.display = "none";
        document.getElementById("conteiner").style.filter="blur(0px)"
}
}
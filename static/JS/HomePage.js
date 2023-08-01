function signup(){
    if(document.getElementById("conteiner").style.filter = "blur(0px)"){
        document.getElementById("user").style.display = "block";
        document.getElementById("conteiner").style.filter = "blur(10px)";
        document.getElementById("Cart").style.display = "none";

    }
    else{
        document.getElementById("user").style.display = "none";
        document.getElementById("conteiner").style.filter="blur(0px)"
    }
}

function Cart(){
    if(document.getElementById("conteiner").style.filter = "blur(0px)"){
        document.getElementById("Cart").style.display = "block";
        document.getElementById("conteiner").style.filter = "blur(10px)";
        document.getElementById("user").style.display = "none";

    }
    else{
        document.getElementById("Cart").style.display = "none";
        document.getElementById("conteiner").style.filter="blur(0px)"
    }
}

function getback(){
    if(document.getElementById("conteiner").style.filter != "blur(0px)"){
        document.getElementById("user").style.display = "none";
        document.getElementById("Cart").style.display = "none";
        document.getElementById("conteiner").style.filter="blur(0px)";
}
}
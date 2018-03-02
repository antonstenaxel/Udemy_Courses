
var cells = document.querySelectorAll("td");
var knapp = document.querySelector("#b");

for(var i = 0; i<cells.length; i++){
  cells[i].addEventListener("click",cellClicked);
}

knapp.addEventListener("click",restart);

function restart(){
  for(var i = 0; i<cells.length; i++){
    cells[i].textContent = "";
  }
}

function cellClicked(event){
  let currentText = event.srcElement.textContent;

  if(currentText == "X"){
    event.srcElement.textContent = "O";
  }else if(currentText == "O"){
    event.srcElement.textContent = "";
  }else{
    event.srcElement.textContent = "X";
  }
}

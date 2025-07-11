const posvote = document.getElementById("likeBtn");
const posnum = document.getElementById("likeCount");
const posicon = document.getElementById("likeIcon");

let poscount = 0;
let isliked = false;

function likebtn() {
  posvote.addEventListener("click", () => {
    if (!isliked) {
      poscount++;
      isliked = true;
      posicon.src = "../img/Vector (1).svg"; // 눌린 상태 이미지
    } else {
      poscount--;
      isliked = false;
      posicon.src = "../img/Vector.svg"; // 원래 이미지
    }
    posnum.innerText = poscount;
  });
}

function clicklikebtn(){
  posvote.addEventListener("click", () => {
    document.getElementById("btnPostGood").click();})
  };

likebtn();
licklikebtn();
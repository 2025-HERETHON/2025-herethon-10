  for (let i = 1; i <= 8; i++) {
    const btn = document.getElementById(`btn${i}`);
    btn.addEventListener('click', () => {
      // 모든 버튼의 선택 상태 초기화
      for (let j = 1; j <= 8; j++) {
        document.getElementById(`btn${j}`).classList.remove('selected');
      }
      // 현재 클릭된 버튼만 선택
      btn.classList.add('selected');
    });
  }
let map; // 전역 변수

window.onload = function () {
  const mapContainer = document.getElementById('map');
  const mapOption = {
    center: new kakao.maps.LatLng(37.5665, 126.9780),
    level: 3
  };
  
  map = new kakao.maps.Map(mapContainer, mapOption); // 지도 생성
};


document.addEventListener("DOMContentLoaded", function () {
  const sidebar = document.getElementById("sidebar");
  const openBtn = document.getElementById("openSidebar");
  const icon = document.getElementById("sidebarIcon")

if (openBtn) {
  openBtn.addEventListener("click", () => {
    sidebar.classList.toggle("open");
    openBtn.classList.toggle("shifted");

    if (sidebar.classList.contains("open")) {
      icon.src = "/static/img/chevron-left.svg";
    } else {
      icon.src = "/static/img/chevron-right.svg"; // 닫힌 상태일 때 아이콘
    }
  });
}

});



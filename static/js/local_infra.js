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

  map = new kakao.maps.Map(mapContainer, mapOption); // map 초기화

  // ✅ 이 안에서 이벤트 등록
  kakao.maps.event.addListener(map, 'click', function(mouseEvent) {
    onMapClick(0);
  });
};

const places = [
  {
    name: '카페 이디야',
    address: ''
  },
  {
    name: '스타벅스 강남점',
    address: ''
   /*영업 중과 시간 없앴습니다.*/
   /*address로 도로명 주소*/
  }
];

function onMapClick(placeIndex) {
  const place = places[placeIndex];

  const container = document.getElementById('place-info-container');
  const nameEl = document.getElementById('place-name');
  const statusEl = document.getElementById('place-address');/*address*/
  const hoursEl = document.getElementById('place-hours');

  nameEl.textContent = place.name;
  statusEl.textContent = place.address;
  hoursEl.textContent = place.hours;

  container.classList.remove('hidden');
}

document.getElementById('savebtn').addEventListener('click', () => {
  onMapClick(0);
});

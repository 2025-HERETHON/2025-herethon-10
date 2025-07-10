document.getElementById("bud").addEventListener("click", function () {

    document.getElementById("divider2").style.display = "block";
    document.getElementById("menutext").style.display = "block";


    function getNumber(id) {
        const val = document.getElementById(id).value;
        return Number(val) || 0;
    }

    const 중개수수료 = getNumber("inputcharge1");
    const 가구가전비 = getNumber("inputcharge2");
    const 이사비용 = getNumber("inputcharge3");

    const 식비 = getNumber("inputcharge4");
    const 쇼핑비 = getNumber("inputcharge5");
    const 취미비 = getNumber("inputcharge6");
 
    const 월세 = getNumber("inputcharge7");
    const 관리비 = getNumber("inputcharge8");
    const 통신비 = getNumber("inputcharge9");
    const 교통비 = getNumber("inputcharge10");

    const 알바 = getNumber("inputcharge11");
    const 용돈 = getNumber("inputcharge12");

    const 초기정착비용 = 중개수수료 + 가구가전비 + 이사비용 + 월세;
    const 고정지출 = 월세 + 관리비 + 통신비 + 교통비;
    const 변동지출 = 식비 + 쇼핑비 + 취미비;
    const 월지출 = 고정지출 + 변동지출;
    const 최초생존예산 = 식비 + 교통비;
    const 총수입 = 알바 + 용돈;
    const 수입지출차이 = 총수입 - 월지출;

    let 여유정도 = " ";

     if (수입지출차이 >= 100) {
            여유정도="여유 예산";
    } 
    else if (수입지출차이 >= 0) {
            여유정도="적정 예산";
    } 
    else {
        여유정도="예산 부족";
    }

    // 📌 계산 결과 calbox에 표시
   document.getElementById("result1").innerHTML = `초기 정착 비용으로 총 <span class="highlight">${초기정착비용} 만원</span>이 필요해요.`;
    document.getElementById("result2").innerHTML = `월 고정 지출은 <span class="highlight">${월지출} 만원</span>으로 예상돼요.`;
    document.getElementById("result3").innerHTML = `현실적인 최초 월 지출은 <span class="highlight">${최초생존예산} 만원</span>으로 예상돼요.`;
    document.getElementById("result4").innerHTML = `현재 님의 예산은 <span class="highlight">${여유정도}</span>이에요.`;


    const explanationText = `집 계약 비용 (첫 월세 + 보증금 + 중개 수수료) + 이사 및 가구 비용`;
    document.getElementById("explanation1").innerText = explanationText;

    const explanationText2 = `고정비 + 변동비의 월 평균으로 계산한 값`;
    document.getElementById("explanation2").innerText = explanationText2;

    const explanationText3 = `식비 + 교통비의 월 평균으로 계산한 최초 생존 예산`;
    document.getElementById("explanation3").innerText = explanationText3;

    const explanationText4 = `수입 - 지출 하여 남는 금액으로 판단`;
    document.getElementById("explanation4").innerText = explanationText4;


    // 📌 예산 여유 결과 budbox에 표시
    let 이미지, 멘트, 멘트2;

    if (수입지출차이 >= 100) {
        이미지 = "/static/img/happy.svg";
        멘트 = "현재 님의 예산은<br><span class='Highlight1'>여유로워요</span>";
        멘트2 = "변동비나 가구 비용에 더 투자해도 좋을 것 같아요";
    } else if (수입지출차이 > 0) {
        이미지 = "/static/img/normal.svg";
        멘트 = "현재 님의 예산은<br><span class='Highlight2'>딱 맞아요</span>";
        멘트2 = "예산을 좀 더 여유롭게 조정해보는 것을 추천해요";
    } else {
        이미지 = "/static/img/warning.svg";
        멘트 = "현재 님의 예산은<br><span class='Highlight3'>불안해요</span>";
        멘트2 = "수입보다 지출이 초과될 것으로 예상돼요";
    }

    document.getElementById("statusImage").src = 이미지;
    document.getElementById("statusImage").style.display = "block";
    document.getElementById("mainMessage").innerHTML = 멘트;
    document.getElementById("subMessage").innerHTML = 멘트2;
    document.getElementById("budbox").style.display = "block"; 


    
});

var dom = document.getElementById("influenceRankChart");
var influenceRankChart = echarts.init(dom);
var app = {};
var mediasOfInflu = [];
var mediasScore = [];
var buttonQueryInfluRank = $('#query-influRank');
var selectInfluNum = $('#selectNum-influRank');
var selectInfluSenti = $('#selectSenti-influRank');

var seriesTitleInfluSelect = {
    "all" : "综合影响力",
    "-1" : "负面影响力",
    "0" : "中性影响力",
    "1" : "正面影响力",
}
var seriesTitleInflu = null;

for (let i=1; i<=showNum; i++){
    selectInfluNum.append($('<option>', {
        value: i,
        text: String(i)
    }));
}

// 设置一开始为5
document.getElementById('selectNum-influRank')
    .getElementsByTagName('option')[4].selected = 'selected'

buttonQueryInfluRank.click(function(){
    axios
        .get(
            djangoIpAddress.addrHost + ':' 
            + djangoIpAddress.addrPort 
            + '/api/medias_influence_score/'
            + "all" + '/'
            + selectInfluSenti.val() + '/'
        )
        .then(response => {
            mediasOfInflu = [];
            mediasScore = [];
            seriesTitleInflu = seriesTitleInfluSelect[selectInfluSenti.val()];

            Object.keys(response.data).forEach(function(key){
                mediasOfInflu.push(key);
                mediasScore.push(response.data[key]);
            })
            let tmp = null;
            for (let i=0; i<mediasOfInflu.length-1; i++){
                for (let j=mediasOfInflu.length-1; j>i; j--){
                    if (mediasScore[j] > mediasScore[j-1]){
                        tmp = mediasScore[j];
                        mediasScore[j] = mediasScore[j-1];
                        mediasScore[j-1] = tmp;
                        tmp = mediasOfInflu[j];
                        mediasOfInflu[j] = mediasOfInflu[j-1];
                        mediasOfInflu[j-1] = tmp;
                    }
                }
            }

            mediasOfInflu = mediasOfInflu.slice(0, Number(selectInfluNum.val()));
            mediasScore = mediasScore.slice(0, Number(selectInfluNum.val()));
            for (let i=0; i<mediasScore.length; i++){
                mediasScore[i] = mediasScore[i].toFixed(2);
            }

            option = null;
            app.title = '坐标轴刻度与标签对齐';

            option = {
                color: ['#3398DB'],
                tooltip : {
                    trigger: 'axis',
                    axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                        type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                    }
                },
                grid: {
                    left: '3%',
                    right: '4%',
                    bottom: '3%',
                    containLabel: true
                },
                xAxis : [
                    {
                        type : 'category',
                        data : mediasOfInflu,
                        axisTick: {
                            alignWithLabel: true
                        }
                    }
                ],
                yAxis : [
                    {
                        type : 'value'
                    }
                ],
                series : [
                    {
                        name : seriesTitleInflu,
                        type : 'bar',
                        barWidth : '60%',
                        data : mediasScore
                    }
                ]
            };
            ;
            if (option && typeof option === "object") {
                influenceRankChart.setOption(option, true);
            }
            if (mediasOfInflu.length == 0){
                alert("暂无" + seriesTitleInflu);
            }
            else if (selectInfluNum.val() > mediasOfInflu.length) {
                alert("媒体数量不足" + String(selectInfluNum.val()) + "个");
            }
        })
});

buttonQueryInfluRank.click();


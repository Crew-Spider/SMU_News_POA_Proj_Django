var dom = document.getElementById("sentimentRankChart");
var sentimentRankChart = echarts.init(dom);
var app = {};
var medias = [];
var mediasNewsCount = [];
var buttonQuerySentiRank = $('#query-sentiRank');
var selectSentiNum = $('#selectNum-sentiRank');
var selectSentiUni = $('#selectUni-sentiRank');
var selectSenti = $('#selectSenti-sentiRank');

var seriesTitleSentiSelect = {
    "-1" : "负面报道",
    "0" : "中性报道",
    "1" : "正面报道",
}
var seriesTitleSenti = null;

for (let i=1; i<=showNum; i++){
    selectSentiNum.append($('<option>', {
        value: i,
        text: String(i)
    }));
}

selectSentiUni.append($('<option>', {
    value: "all",
    text: "全部"
}));
for (let uni of school_list){
    selectSentiUni.append($('<option>', {
        value: uni.zh_name,
        text: uni.zh_name
    }));
}

// 设置一开始为5
document.getElementById('selectNum-sentiRank')
    .getElementsByTagName('option')[4].selected = 'selected'

buttonQuerySentiRank.click(function(){
    axios
        .get(
            djangoIpAddress.addrHost + ':' 
            + djangoIpAddress.addrPort 
            + '/api/medias_sentiment_count/'
            + selectSentiUni.val() + '/'
            + selectSenti.val() + '/'
        )
        .then(response => {
            medias = [];
            mediasNewsCount = [];
            seriesTitleSenti = seriesTitleSentiSelect[selectSenti.val()];

            Object.keys(response.data).forEach(function(key){
                medias.push(key);
                mediasNewsCount.push(response.data[key]);
            })
            let tmp = null;
            for (let i=0; i<medias.length-1; i++){
                for (let j=medias.length-1; j>i; j--){
                    if (mediasNewsCount[j] > mediasNewsCount[j-1]){
                        tmp = mediasNewsCount[j];
                        mediasNewsCount[j] = mediasNewsCount[j-1];
                        mediasNewsCount[j-1] = tmp;
                        tmp = medias[j];
                        medias[j] = medias[j-1];
                        medias[j-1] = tmp;
                    }
                }
            }

            medias = medias.slice(0, Number(selectSentiNum.val()));
            mediasNewsCount = mediasNewsCount.slice(0, Number(selectSentiNum.val()));

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
                        data : medias,
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
                        name : seriesTitleSenti,
                        type : 'bar',
                        barWidth : '60%',
                        data : mediasNewsCount
                    }
                ]
            };
            ;
            if (option && typeof option === "object") {
                sentimentRankChart.setOption(option, true);
            }
            if (medias.length == 0){
                alert("暂无" + seriesTitleSenti);
            }
            else if (selectSentiNum.val() > medias.length) {
                alert("媒体数量不足" + String(selectSentiNum.val()) + "个");
            }
        })
});

buttonQuerySentiRank.click();


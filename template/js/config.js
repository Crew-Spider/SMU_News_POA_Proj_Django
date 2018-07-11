

// var school_list = {};
//
// $.ajax({
// 	url:'/api/v1/colleges',
// 	type:'GET',
// 	async:false,
// 	success:function(data){
// 		for(var i = 0;i < data.length; i++){
// 			if(data[i].en_colleges)
// 			school_list[data[i].en_colleges] = data[i].zh_colleges;
// 		}
// 	}
// });

var school_list = [
	{
		"zh_name": "上海海事大学",
		"en_name": "smu"
	},

	{
		"zh_name": "上海交通大学",
		"en_name": "sjtu"
	},

	{
		"zh_name": "同济大学",
		"en_name": "tongji"
	},

	{
		"zh_name": "复旦大学",
		"en_name": "fudan"
	},

	{
		"zh_name": "华东师范大学",
		"en_name": "ecnu"
	},

	{
		"zh_name": "上海大学",
		"en_name": "shu"
	},

	{
		"zh_name": "华东理工大学",
		"en_name": "ecust"
	},

	{
		"zh_name": "东华大学",
		"en_name": "dhu"
	},

	{
		"zh_name": "上海财经大学",
		"en_name": "shufe"
	},

	{
		"zh_name": "上海外国语大学",
		"en_name": "shisu"
	},

	{
		"zh_name": "华东政法大学",
		"en_name": "ecupl"
	},

	{
		"zh_name": "上海师范大学",
		"en_name": "shnu"
	},

	{
		"zh_name": "上海理工大学",
		"en_name": "usst"
	},

	{
		"zh_name": "上海海洋大学",
		"en_name": "shou"
	},

	{
		"zh_name": "上海中医药大学",
		"en_name": "shutcm"
	},

	{
		"zh_name": "上海音乐学院",
		"en_name": "sus"
	},

	{
		"zh_name": "上海戏剧学院",
		"en_name": "sta"
	},

	{
		"zh_name": "上海对外经贸大学",
		"en_name": "shift"
	},

	{
		"zh_name": "上海电机学院",
		"en_name": "sdju"
	},

	{
		"zh_name": "上海工程技术大学",
		"en_name": "sues"
	}
];

var classification = {
	study:"学习学术",
	entrance:"招生考试",
	activity:"社团活动",
	social:"社会新闻"

};


var ipAddress = {
	addrHost:'http://127.0.0.1',
	addrPort: '4000'
};

var djangoIpAddress = {
	addrHost:'http://127.0.0.1',
	addrPort: '8000'
};

// 最大可选显示的媒体个数
var showNum = 15;

//
// var school_list_ch_en={
// 	"上海交通大学":"sjtu",
// 	'同济大学':'tongji',
// 	'复旦大学':'fudan',
// 	'华东师范大学':'ecnu',
// 	'上海大学':'shu',
// 	'华东理工大学':'ecust',
// 	'东华大学':'dhu',
// 	'上海财经大学':'shufe',
// 	'上海外国语大学':'shisu',
// 	'华东政法大学':'ecupl',
// 	'上海师范大学':'shnu',
// 	'上海理工大学':'usst',
// 	'上海海事大学':'smu',
// 	'上海海洋大学':'shou',
// 	'上海中医药大学':'shutcm',
// 	'上海体育学院':'sus',
// 	'上海音乐学院':'shcmusic',
// 	'上海戏剧学院':'sta',
// 	'上海对外经贸大学':'shift',
// 	'上海电机学院':'sdju',
// 	'上海工程技术大学':'sues',
// 	'上海科技大学':'shanghaitech',
// 	'大连海事大学':'dlmu',
// 	'武汉理工大学':'whut',
// 	'集美大学':'jmu',
// 	'中国海洋大学':'ouc'};
//







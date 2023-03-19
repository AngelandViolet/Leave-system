//转化函数
var change = (number) => {
    var result;
    if (number == "第一大节") { result = 1; }
    else if (number == "第二大节") { result = 2; }
    else if (number == "第三大节") { result = 3; }
    else { result == 4; }
    return result;
}


var judged = (judge,date) => {
    


    var dated = new Date();

    let day = dated.getDate();
    if (day < 10) {
        day = "0" + day;
    }

    let month = dated.getMonth();

    month = month + 1;
    if (month < 10) {
        month = "0" + month;
    }

    let year = dated.getFullYear();

    var nowdate = year + "-" + month + "-" + day;
    console.log("你选的时间是" + date);
    
    console.log("现在的时间是" + nowdate);

    if (date >= nowdate) {
        return 1;
    }
    else {
        return 0;
    }




}

//判断调整前后时间是否合理

//点击确认后执行
function isconfirm() {
    //获取各种元素
    var cause = document.getElementById('cause').value;
    var from = document.getElementById('date-from-text').value;
    var to = document.getElementById('date-to-text').value;
    var number1 = document.getElementById('date-text1').value
    var number2 = document.getElementById('date-text2').value
    //将第几大节转化为数字
    var result1 = change(number1);
    var result2 = change(number2);
    var indexd = 0;
    var index = confirm('是否确认调整研学');
    //获取判断时间是否合理
    var judge1 = judged(result1,from);
    var judge2 = judged(result2,to);

    //这块是再次确认之后向后端传入信息
    if (cause == '') {
        alert("原因不能为空");
    }
    if (from == '') {
        alert("调整前时间不能为空");
    }
    if (to == '') {
        alert("调整后时间不能为空");
    }
    if (!judge1||!judge2) {
        alert("调整研学时间不合理，请重新选择研学时间");
    }
    if (cause != '' && from != '' &&to!='' &&  judge1 && judge2) {
        indexd = 1;
    }

    if (index && indexd) {
        axios({
            method: 'post',
            url: 'http://6xa4kvxq.shenzhuo.vip:47020/excused/',
            data: {
                reason: `${cause}`,
                old_date: `${from}`,
                new_date: `${to}`,
                old_time: `${number1}`,
                new_time:`${number2}`
            }

        }).then((res) => { console.log(res.data); })
        alert("成功调整");
        console.log("已成功调整");
        console.log(number1);
        console.log(number2);

        
        










        
    }
    if (index && indexd) {
        axios({
            method: 'get',
            url: 'http://6xa4kvxq.shenzhuo.vip:47020/api/getdata/'


        }).then((res) => { console.log(res.data.username); })


    }
};


//偷来的接口,获取当前时间
var time = document.getElementById('time');

function getTime() {
    axios.get('https://api.reginvolver.cn//common/time').then((res) => {
        time.innerHTML = '当前时间为:' + `${res.data}`;
    });
}
setInterval(getTime, 1000);

// 获取用户基本信息
let username = document.querySelector('.username');
let direction = document.querySelector('.direction');
let grade = document.querySelector('.grade');
// let username = document.getElementById('username');
// let direction = document.getElementById('direction');
// let grade = document.getElementById('grade');
axios.defaults.baseURL = "https://zkr.shenzhuo.vip";
let user_id = localStorage.getItem('user_id');
axios.interceptors.request.use(function (config) {
    if(!localStorage.getItem('user_id')){
        location.href = "C:\\Users\\麻花几路\\Desktop\\研学请假系统\\src\\SignUpAndLogIn\\loginSign\\loginSign.html";
    }
    alert('未经登录，禁止访问！请登录！');
    return config;
}, function (error) {
    return Promise.reject(error);
});

(function getId() {
    axios({
        url: '/user/show_user_information',
        method: 'post',
        headers: { "Content-type": "application/json" },
        data: {
            user_id: `${user_id}`,
        }
    }).then(function (response) {
        console.log(response);
        // console.log(response.status);
        username.innerText = '姓名：'+response.data.user_name;
        direction.textContent = '方向：' +response.data.user_sector;
        grade.textContent = '期数：' +response.data.user_period;
    }).catch(err => console.log(err));
})();

// 获取数据
let leave_table = document.querySelector('.leave_table');
let change_table = document.querySelector('.change_table');
let leave_tbody = document.querySelector('.leave_tbody');
let change_tbody = document.querySelector('.change_tbody');
(function () {
    axios({
        // url: '/show_all/all_data',
        url: '/user/show_all_data',
        method: 'post',
        headers: { "Content-type": "application/json" },
        data: {
            user_id: `${user_id}`,
        }
    }).then(res => {
        console.log(res);
        let leave = res.data.leave_data;
        // console.log(leave)
        let change = res.data.change_data;
        if (Array.isArray(leave)) {
            for (leave_item of leave) {
                let tr = document.createElement("tr");
                tr.innerHTML = `<td>${leave_item.time}</td>                    
            <td>${leave_item.reason}</td>`
                leave_tbody.appendChild(tr);
            }
        }
        // console.log(typeof(leave),'@@@');
        // console.log(typeof(change),'%%%');
        if (Array.isArray(change)) {
            for (change_item of change) {
                let tr = document.createElement("tr");
                tr.innerHTML = `<td>${change_item.old_time}</td>
            <td>${change_item.new_time}</td>
            <td>${change_item.reason}</td>`
                change_tbody.appendChild(tr);
            }
        }

    }).catch(err => console.log(err));
})();
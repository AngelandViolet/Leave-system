let table = document.querySelector('table');
let tbody = document.querySelector('tbody');
let sort = document.getElementsByClassName('sort');
axios.defaults.baseURL = "http://gaosu.shenzhuo.vip:50003";
(function () {
    axios({
        url: '/show_all/all_data?user_id=003',
        // url: `/show_all/all_data?user_id=${id}`,
        method: 'get',
        headers: { "Content-type": "application/json" }
    }).then(res => {
        console.log(res);
        let list = res.data.data.change_data;
        let tr = document.createElement("tr")
        tr.innerHTML = `<td>${item.old_time}</td>                    
        <td>${item.reason}</td>
        <td>${item.old_time}</td>
        <td>${item.new_time}</td>
        <td>${item.reason}</td>`
        tbody.appendChild(tr)
    }).catch(err => console.log(err));
})();

let table = document.querySelector('table');
let tbody = document.querySelector('tbody');
(function () {
    axios({
        url: 'http://wnzu57jq.shenzhuo.vip:50003/show_all/all_data?user_id=001',
        method: 'get',
        headers: { "Content-type": "application/json" }
    }).then(res => {
        console.log(res);
        let list = res.data;
        let tr = document.createElement("tr");
        tr.innerHTML = `<td>${item.leave_data}</td>                    
        <td>${item.username}</td>
        <td>${item.base_data}</td>
        <td>${item.change_data}</td>
        <td>${item.role}</td>`
        tbody.appendChild(tr);
    }).catch(err => console.log(err));
})();
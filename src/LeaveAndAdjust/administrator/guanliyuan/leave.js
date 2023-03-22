let table = document.querySelector('table');
let tbody = document.querySelector('tbody');
(function () {
    axios({
        url: 'https://zkr.shenzhuo.vip/manager/show_leave_data',
        method: 'get',
        headers: {
            "Content-type": "application/json",
            

        }
    }).then(res => {
        console.log(res.data);
        let list = res.data;
        for (let hh of list ){
            let tr = document.createElement("tr");
            tr.innerHTML =
                `
        <td>${hh.user_name}</td>                    
        <td>${hh.user_sector}</td>
        <td>${hh.leave_time}</td>
        <td>${hh.leave_class}</td>
        <td>${hh.leave_reason}</td>
        `
            tbody.appendChild(tr);
        }
        
    }).catch(err => console.log(err));
})();





function change() {
    window.open()
}
let table = document.querySelector('table');
let tbody = document.querySelector('tbody');
function get () {
    axios({
        url: 'https://zkr.shenzhuo.vip/manager/show_change_data',
        method: 'get',
        headers: { "Content-type": "application/json" }
    }).then(res => {
        console.log(res.data);
        let list = res.data;
        for (let hh of list) {
            let tr = document.createElement("tr");
            tr.innerHTML =
                `<td>${hh.user_name}</td>                    
        <td>${hh.user_sector}</td>
        <td>${hh.old_time}${hh.old_class}</td>
        <td>${hh.new_time}${hh.new_class}</td>
        <td>${hh.change_reason}</td>`
            tbody.appendChild(tr);
        }
    }).catch(err => console.log(err));
}
get();
function change() {
    window.open();
}

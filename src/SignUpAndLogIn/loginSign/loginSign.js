const signInBtn = document.getElementById("signIn");
const signUpBtn = document.getElementById("signUp");
const fistForm = document.getElementById("SignUp_form");
const secondForm = document.getElementById("SignIn_form");
const container = document.querySelector(".container");


signInBtn.addEventListener("click", () => {
    container.classList.remove("right-panel-active");
});

signUpBtn.addEventListener("click", () => {
    container.classList.add("right-panel-active");
});

console.log(fistForm)
fistForm.addEventListener("submit", (e) => {
    e.preventDefault()
    fistForm
});
secondForm.addEventListener("submit", (e) => e.preventDefault());

//密码框  获取元素
var SignIn_eye = document.getElementById('SignIn_eye');
var SignUp_eye = document.getElementById('SignUp_eye');
var SignIn_password = document.getElementById('SignIn_password');
var SignUp_password = document.getElementById('SignUp_password');
//注册事件 处理程序
var flag = 0;
SignIn_eye.onclick = function () {
    if (flag == 0) {
        SignIn_password.type = 'text';
        SignUp_password.type = 'text';
        SignIn_eye.src = "https://lmy-2.oss-cn-beijing.aliyuncs.com/yanjing.png"
        flag = 1;
    } else {
        SignIn_password.type = 'password';
        SignUp_password.type = 'password';

        SignIn_eye.src = "https://lmy-2.oss-cn-beijing.aliyuncs.com/yanjing-bi.png"
        flag = 0;
    }
}
SignUp_eye.onclick = function () {
    if (flag == 0) {
        SignIn_password.type = 'text';
        SignUp_password.type = 'text';
        SignUp_eye.src = "https://lmy-2.oss-cn-beijing.aliyuncs.com/yanjing.png"
        flag = 1;
    } else {
        SignIn_password.type = 'password';
        SignUp_password.type = 'password';
        SignUp_eye.src = "https://lmy-2.oss-cn-beijing.aliyuncs.com/yanjing-bi.png"
        flag = 0;
    }
}

axios.defaults.baseURL = 'https://zkr.shenzhuo.vip';
axios.defaults.withCredentials = true;

// 获取各种元素
var SignIn_StudentID = document.getElementById('SignIn_StudentID');
var SignIn_password = document.getElementById('SignIn_password');

// 用户登录界面
function stu_login() {
    if (SignIn_StudentID.value == '') {
        alert("请输入账号");
    }

    else if (SignIn_password.value == '') {
        alert("请输入密码");
    }
    axios({
        method: 'GET',
        url: '/user/user_log'
    }).then(res => {
        alert('登录成功')
        //跳转至请假界面
        window.location.href = "../../LeaveAndAdjust/user/front/leave/leave.html";
        localStorage.setItem('id', `${SignIn_StudentID.value}`);
    }).catch(err => {
        console.log(err.response.status)
        if (err.response.status == 403) {
            axios({
                url: '/user/user_log',
                method: 'POST',
                data: {
                    "user_id": `${SignIn_StudentID.value}`,
                    "user_pass": `${SignIn_password.value}`,
                }
            })
                .then(res => {
                    if (res.status == 200) {
                        alert("登录成功")
                        // console.log(res)
                        // console.log(document.cookie)
                        //跳转至请假界面
                        window.location.href = "../../LeaveAndAdjust/user/front/leave/leave.html";
                        localStorage.setItem('id', `${SignIn_StudentID.value}`);
                    }
                    else if (res.status == 201) {
                        alert("密码错误,请重新输入")
                    }
                    else if (res.status == 202) {
                        alert("用户不存在,请重新输入")
                    }
                })
        }
    })

}


// 用户注册界面
function sign() {
    //获取元素
    var name = document.getElementById('name');
    var direction = document.getElementById('direction');
    var NumberOfPeriods = document.getElementById('NumberOfPeriods');
    var SignUp_StudentID = document.getElementById('SignUp_StudentID');
    var SignUp_password = document.getElementById('SignUp_password');
    var InvitationCode = document.getElementById('InvitationCode');

    //判断内容是否为空为空
    if (name.value == '') {
        alert('请输入姓名')
    }
    // else if (name.value != '') {
    //     if (name.value != /[^\u4E00-\u9FA5]/g)
    //         alert('姓名不符合国情');
    // }
    else if (direction.value == '') {
        alert('请选择方向')
    }
    else if (NumberOfPeriods.value == '') {
        alert('请输入期数')
    }
    else if (SignUp_StudentID.value == '') {
        alert('请输入账号')
    }
    // else if (StudentID.value != '') {
    //     if (StudentID.value != /[^\d]/g)
    //         alert('请输入数字');
    // }
    else if (SignUp_password.value == '') {
        alert('请输入密码')
    }
    // else if (password.value != '') {
    //     if (password.value != /^(?=.*\d)(?=.*[a-zA-Z])(?=.*[~!@#$%^&*])[\da-zA-Z~!@#$%^&*]{8,}$/)
    //         alert('必须包含数字、英文字母、特殊符号且大于等于8位(特殊符号包括: ~!@#$%^&*)');
    // }
    else if (InvitationCode.value == '') {
        alert('请输入邀请码')
    }
    else {
        axios({
            url: '/user/user_sign',
            method: 'POST',
            headers: { "Content-type": "application/json" },
            data: {
                "user_name": `${name.value}`,
                "user_sector": `${direction.value}`,
                "user_period": `${NumberOfPeriods.value}`,
                "user_id": `${SignUp_StudentID.value}`,
                "user_pass": `${SignUp_password.value}`,
                "invitation_code": `${InvitationCode.value}`
            }
        })
            .then((res) => {
                if (res.status == 200) {
                    alert("注册完成！");
                    container.classList.remove("right-panel-active");
                }
                if (res.status != 200) {
                    alert("邀请码错误，请重新输入");
                }
            })
    }
}


// 管理员登录界面
function login() {
    if (SignIn_StudentID.value == '') {
        alert("请输入账号");
    }

    else if (SignIn_password.value == '') {
        alert("请输入密码");
    }
    axios({
        url: 'https://zkr.shenzhuo.vip/manager/manager_log',
        method: 'POST',
        data: {
            "manager_id": `${SignIn_StudentID.value}`,
            "manager_pass": `${SignIn_password.value}`,
        }
    }).then(res => {
        if (res.status == 203) {
            alert("登录成功")
            //此处跳转至管理端
            window.location.href = "C:\\Users\\麻花几路\\Desktop\\研学请假系统\\src\\LeaveAndAdjust\\user\\front\\guanliyuan\\leave.html";
            localStorage.setItem('id', `${SignIn_StudentID.value}`);
        }
        else if (res.status == 204) {
            alert("账号或密码错误,请重新输入")
        }
    })
}
$(document).ready(function(){
    $("#b1").click(function(){
        $(".rb").show();
        $(".rb").attr("disabled", true);
    });
});

let resetBtn = document.querySelector("#reset-btn");

let resetQuiz = (e) => {
    let correctAns = document.querySelectorAll("#corans");
    let options = document.querySelectorAll(".rb");

    correctAns.forEach(item => {
        item.style.display = "none";
    });

    options.forEach(item => {
        item.removeAttribute("disabled");
        item.removeAttribute("checked");
    });
    e.preventDefault();
};

resetBtn.addEventListener("click", resetQuiz);
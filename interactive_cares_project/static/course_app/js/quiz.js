// Define Jquery
$(document).ready(function(){
    $("#b1").click(function(){
        $(".rb").show();
        $(".rb").attr("disabled", true);
    });
});

// Define UI
let b1 = document.querySelector("#b1");
let resetBtn = document.querySelector("#reset-btn");
let scoreBoard = document.querySelector("#score-board");

// Define Function
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

    scoreBoard.innerText = "";
    e.preventDefault();
};

let checkAnswer = (e) => {
    let answer = document.querySelectorAll(".ans");
    let correctAns = document.querySelectorAll(".correct-ans");
    let score = 0;

    answer.forEach(answer => {
        if (answer.checked) {
            correctAns.forEach(correctAns => {
                if (answer.value === correctAns.textContent){
                    score++;
                };
            });
        };
    });

    scoreBoard.textContent = `You got ${score} out of ${correctAns.length}`; 

    e.preventDefault();
};

// Define Event Listener
resetBtn.addEventListener("click", resetQuiz);
b1.addEventListener("click", checkAnswer);

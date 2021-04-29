const canvas = document.getElementById('canvas')
const ctx = canvas.getContext('2d')
const nameInput = document.getElementById('name')
const courseInput = document.getElementById('course')
const logo = document.getElementById('logo')
const downloadBtn = document.getElementById('download-btn')

const image = new Image()
image.src = '../../../static/course_app/img/certificate.png'
image.onload = function () {
	drawImage()
}

function drawImage() {
	ctx.drawImage(image, 0, 0, canvas.width, canvas.height)
	ctx.font = 'bolder 130px Verdana, Geneva, Tahoma, sans-serif'
	ctx.fillStyle = '#3A4153'
	ctx.fillText(nameInput.value.toUpperCase(), 830, 1350)
	ctx.font = 'bolder 80px Verdana, Geneva, Tahoma, sans-serif'
	ctx.fillText(courseInput.value, 820, 1700);
	ctx.font = '60px Verdana, Geneva, Tahoma, sans-serif'
	ctx.fillText(`on ${new Date()}`, 820, 1800);
	ctx.drawImage(logo, 820, 250)
}

nameInput.addEventListener('input', function () {
	drawImage()
})

courseInput.addEventListener('input', function () {
	drawImage()
})

downloadBtn.addEventListener('click', function () {
	downloadBtn.href = canvas.toDataURL('image/jpeg');
	downloadBtn.download = 'Certificate - ' + nameInput.value;
}, false)

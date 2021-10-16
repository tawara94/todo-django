function setBgColor(bgColor) {
  document.getElementById('content').style.backgroundColor = bgColor
  localStorage.setItem('bgColor', bgColor)
}

function setColor(btnId, bgColor) {
  document.getElementById(btnId).style.backgroundColor = bgColor
  document.getElementById(btnId).addEventListener('click', () => {
    setBgColor(bgColor)
  })
}

setColor('white', 'white')
setColor('gray', 'lightgray')
setColor('yellow', 'lightyellow')
setColor('red', 'pink')
setColor('blue', 'lightblue')
setColor('green', 'lightgreen')

bgColor = localStorage.getItem('bgColor')
setBgColor(bgColor)

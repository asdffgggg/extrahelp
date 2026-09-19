

const checkbox = document.getElementById('other')

checkbox.addEventListener('change', (event) => {
  if (event.currentTarget.checked) {
    document.getElementById('othertext').style.display = 'block'
  } else {
    document.getElementById('othertext').style.display = 'none'
  }
})
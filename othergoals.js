const checkbox = document.getElementById('other goals')

checkbox.addEventListener('change', (event) => {
  if (event.currentTarget.checked) {
    document.getElementById('othergoalstext').style.display = 'block'
  } else {
    document.getElementById('othergoalstext').style.display = 'none'
  }
})
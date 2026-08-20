const form = document.getElementById("form");
form.addEventListener("submit", (event) => {
  
    for (let input of document.getElementsByClassName("input")) {
        sessionStorage.setItem(input.name, input.value)
    }

})
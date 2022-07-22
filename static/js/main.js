// Data Not Saving, Error Message: "GET /static/js/main.js HTTP/1.1" 304 0
// Full path runs but data is not saved

function saveEntry() {
    // Remember to add '.value' (this is necessary because teh element is an object)
    title = document.getElementById("newTitle").value
    description = document.getElementById("newDescription").value
    // "" is re-running this url but now in a POST request
    axios.post("", {title : title, description: description}).then((response) => {
      // Redirecting from JS based on your current url
      // Example: if current url = "authors/2/entries/1/"
      // ../../ will cut off two of the last snippets of your url and run "authors/"
    window.location.href = "../../"
    })
}

//   function editBook(){
//     title = document.getElementById("newTitle").value
//     author = document.getElementById("newAuthor").value
//     description = document.getElementById("newDescription").value
  
//     axios.post("", {title : title, author : author, description: description}).then((response) => {
//       window.location.href = "../../../"
//       })
  
//   }
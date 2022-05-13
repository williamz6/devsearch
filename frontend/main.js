let loginBtn =  document.getElementById('login-btn')
let logoutBtn =  document.getElementById('logout-btn')

let token = localStorage.getItem('token')

if (token) {
    loginBtn.remove()
}
else {
    logoutBtn.remove()
}

logoutBtn.addEventListener('click', (e) => {
    e.preventDefault()
    localStorage.removeItem('token')
    window.location= 'http://127.0.0.1:59601/login.html'
})
let projectsUrl =  "http://127.0.0.1:8000/api/projects/"

let getProjects = () => {
    fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        buildProjects(data)
    })
}


let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects--wrapper')
    projectsWrapper.innerHTML = ''

    for (let i = 0; projects.length > i; i++) {

        let project = projects[i]

        let projectCard = `
                <div class="project--card">
                        <img src="http://127.0.0.1:8000${project.feature_image}" alt="...">
                        <div >                            
                            <div class="card--header">
                                <h3>${project.title}</h3>
                                <strong class= "vote--option" data-vote="up" data-project="${project.id}">&#43;</strong>
                                <strong class= "vote--option" data-vote="down" data-project="${project.id}">&#8722;</strong>
                            </div>
                            ${(()=>{
                                if (project.vote_ratio){
                                    return `<i>${project.vote_ratio}% Postitve feedback</i> `
                                }
                                else{
                                    return`<i>No vote</i>`
                                }

                            })()}  
                            ${(() => {
                                if (project.description){
                                    return `<p class="card-text">${project.description.substring(0,150)}.</p>`
                                }
                                else{
                                    return `<p></p>`
                                }
                            })()}                         
                        </div>
                 
                </div>
            
        `
        projectsWrapper.innerHTML += projectCard

    }
    addVoteEvents()
}

let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option')
    for(let i = 0; voteBtns.length > i; i++){
         voteBtns[i].addEventListener('click', (e) => {
             let token = localStorage.getItem('token')
             console.log('Token:', token)
             let vote = e.target.dataset.vote
             let project = e.target.dataset.project
             fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method:'POST',
                headers:{
                    'Content-Type':'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({'value':vote}),
                

             })
             .then(response => response.json())
             .then(data => {
                 console.log('SUCCESS', data)
                 getProjects()
             })
         })
    }
}
getProjects()

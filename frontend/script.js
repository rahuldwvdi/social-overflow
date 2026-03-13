async function runDebate(){

const q = document.getElementById("questionInput").value
const results = document.getElementById("results")

results.innerHTML = "agents are thinking..."

const res = await fetch("/debate?question=" + encodeURIComponent(q))
const data = await res.json()

console.log(data)

results.innerHTML = ""

const agents = data.arguments

if(!agents){
results.innerHTML = "No responses returned"
return
}

Object.keys(agents).forEach(agent => {

const div = document.createElement("div")

div.className = "agent"

div.innerHTML = `
<h3>${agent}</h3>
<p>${agents[agent]}</p>
`

results.appendChild(div)

})

}
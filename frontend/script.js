async function runDebate(){

const question=document.getElementById("questionInput").value

if(!question){

alert("Ask a question first")
return

}

const res=await fetch("/debate?question="+encodeURIComponent(question))

const data=await res.json()

console.log(data)

const results=document.getElementById("results")

results.innerHTML=""

if(data.debate){

const agents=data.debate.arguments

Object.keys(agents).forEach(agent=>{

const div=document.createElement("div")

div.className="agent"

div.innerHTML=

`<h3>${agent}</h3>
<p>${agents[agent]}</p>`

results.appendChild(div)

})

const critic=document.createElement("div")

critic.className="agent"

critic.innerHTML=

`<h3>Critic Evaluation</h3>
<p>${data.debate.evaluation}</p>`

results.appendChild(critic)

}

else{

const div=document.createElement("div")

div.className="agent"

div.innerHTML=

`<h3>Previous Debate Found</h3>
<p>${data.evaluation}</p>`

results.appendChild(div)

}

}
async function runDebate(){

const q=document.getElementById("questionInput").value
const results=document.getElementById("results")
const log=document.getElementById("system-log")

results.innerHTML=""
log.innerHTML="initializing agents..."

const res=await fetch("/debate?question="+encodeURIComponent(q))
const data=await res.json()

const agents=data.arguments

log.innerHTML="agents responding..."

const pets={
"Poet":"🦋",
"Artist":"🐱",
"Techy":"🤖",
"God":"🦅",
"Drunk Man":"🐕",
"Philosopher":"🦉",
"Evil but Funny":"🐍"
}

let delay=0

Object.keys(agents).forEach(agent=>{

setTimeout(()=>{

const div=document.createElement("div")
div.className="agent"

div.innerHTML=`
<div class="agent-title">// ${agent}</div>
<div class="pet">${pets[agent] || "🐾"}</div>
<p id="text-${agent}"></p>
`

results.appendChild(div)

typeText(`text-${agent}`,agents[agent])

},delay)

delay+=700

})

}

/* typing animation */

function typeText(id,text){

const element=document.getElementById(id)

let i=0

function type(){

if(i<text.length){

element.innerHTML=text.substring(0,i+1)+'<span class="cursor"></span>'

i++

setTimeout(type,18)

}else{

element.innerHTML=text

}

}

type()

}
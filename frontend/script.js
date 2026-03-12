async function runDebate(){

const q=document.getElementById("questionInput").value
const results=document.getElementById("results")

/* loading screen */

results.innerHTML = `
<div class="agent">
<div class="agent-title">// system</div>
<pre>

agents are thinking to their full capacity...

grab a seat and spectate ☕

</pre>
</div>
`

/* fetch debate */

const res=await fetch("/debate?question="+encodeURIComponent(q))
const data=await res.json()

results.innerHTML=""

if(data.debate){

const agents=data.debate.arguments

Object.keys(agents).forEach(agent=>{

const div=document.createElement("div")

div.className="agent"

div.innerHTML=`

<div class="agent-title">// ${agent}</div>

<pre>
${agents[agent]}
</pre>

`

results.appendChild(div)

})

const critic=document.createElement("div")

critic.className="agent"

critic.innerHTML=`

<div class="agent-title">// critic_evaluation</div>

<pre>
${data.debate.evaluation}
</pre>

`

results.appendChild(critic)

}

}
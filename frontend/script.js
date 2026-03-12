async function runDebate() {

    const question = document.getElementById("questionInput").value;

    if (!question) {
        alert("Enter a question");
        return;
    }

    try {

        const response = await fetch(
            "/debate?question=" + encodeURIComponent(question)
        );

        const data = await response.json();

        console.log(data);

        const results = document.getElementById("results");
        results.innerHTML = "";

        const agents = data.debate.arguments;

        for (const agent in agents) {

            const div = document.createElement("div");

            div.className = "agent";

            div.innerHTML =
                "<h3>" + agent + "</h3>" +
                "<p>" + agents[agent] + "</p>";

            results.appendChild(div);
        }

        const evaluation = document.createElement("div");

        evaluation.className = "agent";

        evaluation.innerHTML =
            "<h3>Critic Evaluation</h3>" +
            "<p>" + data.debate.evaluation + "</p>";

        results.appendChild(evaluation);

    } catch (error) {

        console.error(error);

        alert("Error contacting backend");
    }
}
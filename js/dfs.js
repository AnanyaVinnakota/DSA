/* =========================================
   DFS TEST CASES
========================================= */

const testCases = {

    simple: {
        title: "Simple Connected Graph",

        description:
            "A basic connected graph where DFS explores one branch completely before backtracking.",

        graph: {
            A: ["B", "C"],
            B: ["D", "E"],
            C: ["F"],
            D: [],
            E: [],
            F: []
        },

        start: "A",

        expected: ["A", "B", "D", "E", "C", "F"]
    },


    cycle: {
        title: "Graph with Cycle",

        description:
            "A graph containing a cycle. DFS must avoid visiting an already visited vertex again.",

        graph: {
            A: ["B"],
            B: ["C"],
            C: ["A", "D"],
            D: []
        },

        start: "A",

        expected: ["A", "B", "C", "D"]
    },


    disconnected: {
        title: "Disconnected Graph",

        description:
            "A graph containing multiple disconnected components. DFS only visits vertices reachable from the starting node.",

        graph: {
            A: ["B"],
            B: [],
            C: ["D"],
            D: []
        },

        start: "A",

        expected: ["A", "B"]
    },


    selfloop: {
        title: "Graph with Self Loop",

        description:
            "A graph containing a self-loop. DFS should not repeatedly visit the same vertex.",

        graph: {
            A: ["A", "B"],
            B: ["C"],
            C: []
        },

        start: "A",

        expected: ["A", "B", "C"]
    },


    complex: {
        title: "Complex Graph with Multiple Cycles",

        description:
            "A complex graph containing multiple cycles and branches.",

        graph: {
            A: ["B", "C"],
            B: ["D", "E"],
            C: ["F"],
            D: ["C"],
            E: ["F", "G"],
            F: ["A"],
            G: []
        },

        start: "A",

        expected: ["A", "B", "D", "C", "F", "E", "G"]
    }

};


/* =========================================
   DFS STATE
========================================= */

let currentTest = testCases.simple;

let stack = [];

let visited = [];

let currentNode = null;

let finished = false;


/* =========================================
   LOAD TEST CASE
========================================= */

function loadTestCase() {

    const selected =
        document.getElementById("test-select").value;

    currentTest =
        testCases[selected];

    document.getElementById("test-title").textContent =
        currentTest.title;

    document.getElementById("test-description").textContent =
        currentTest.description;

    document.getElementById("start-node").textContent =
        currentTest.start;

    document.getElementById("expected-output").textContent =
        JSON.stringify(currentTest.expected);

    displayGraph(currentTest.graph);

    resetDFS();

}


/* =========================================
   DISPLAY GRAPH
========================================= */

function displayGraph(graph) {

    const graphElement =
        document.getElementById("input-graph");

    graphElement.textContent = "";

    for (const node in graph) {

        const line =
            document.createElement("div");

        line.textContent =
            `${node} → [${graph[node].join(", ")}]`;

        graphElement.appendChild(line);

    }

}


/* =========================================
   RESET DFS
========================================= */

function resetDFS() {

    stack = [currentTest.start];

    visited = [];

    currentNode = null;

    finished = false;

    updateUI();

    document.getElementById("actual-output").textContent =
        "-";

    const result =
        document.getElementById("test-result");

    result.textContent = "";

    result.className = "";

}


/* =========================================
   RUN DFS
========================================= */

function runDFS() {

    resetDFS();

    executeStep();

}


/* =========================================
   NEXT STEP
========================================= */

function nextStep() {

    if (finished) {
        return;
    }

    executeStep();

}


/* =========================================
   EXECUTE ONE DFS STEP
========================================= */

function executeStep() {

    if (stack.length === 0) {

        finished = true;

        showResult();

        return;

    }


    currentNode = stack.pop();


    /*
       If already visited, skip it.
    */

    if (visited.includes(currentNode)) {

        updateUI();

        return;

    }


    /*
       Mark current node as visited.
    */

    visited.push(currentNode);


    /*
       Add neighbours in reverse order.

       This makes the first neighbour
       get processed first.
    */

    const neighbours =
        currentTest.graph[currentNode] || [];


    for (
        let i = neighbours.length - 1;
        i >= 0;
        i--
    ) {

        const neighbour =
            neighbours[i];


        if (!visited.includes(neighbour)) {

            stack.push(neighbour);

        }

    }


    updateUI();


    /*
       If there is nothing left
       to process, finish.
    */

    if (stack.length === 0) {

        finished = true;

        showResult();

    }

}


/* =========================================
   UPDATE UI
========================================= */

function updateUI() {

    document.getElementById(
        "current-node"
    ).textContent =
        currentNode ?? "-";


    document.getElementById(
        "queue"
    ).textContent =
        stack.length
            ? stack.join(", ")
            : "-";


    document.getElementById(
        "visited"
    ).textContent =
        visited.length
            ? visited.join(", ")
            : "-";

}


/* =========================================
   SHOW TEST RESULT
========================================= */

function showResult() {

    const actual =
        JSON.stringify(visited);

    const expected =
        JSON.stringify(currentTest.expected);


    const actualElement =
        document.getElementById("actual-output");

    const resultElement =
        document.getElementById("test-result");


    actualElement.textContent =
        actual;


    if (actual === expected) {

        resultElement.textContent =
            "✓ Test Passed";

        resultElement.className =
            "test-pass";

    } else {

        resultElement.textContent =
            "✗ Test Failed";

        resultElement.className =
            "test-fail";

    }

}


/* =========================================
   INITIALIZE
========================================= */

loadTestCase();
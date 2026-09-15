/* =========================================================
   BFS TEST CASES
   These are based directly on test_bfs.py
========================================================= */

const testCases = {

    // 1. Basic connected graph
    basic: {
        title: "Basic Connected Graph",

        description:
            "A basic connected graph to verify standard BFS traversal.",

        graph: {
            A: ["B", "C"],
            B: ["D", "E"],
            C: ["F"],
            D: [],
            E: [],
            F: []
        },

        start: "A",

        expected: ["A", "B", "C", "D", "E", "F"]
    },


    // 2. Graph containing a cycle
    cycle: {
        title: "Graph Containing a Cycle",

        description:
            "Tests whether BFS correctly handles a graph containing a cycle.",

        graph: {
            A: ["B"],
            B: ["C"],
            C: ["A", "D"],
            D: []
        },

        start: "A",

        expected: ["A", "B", "C", "D"]
    },


    // 3. Disconnected graph
    disconnected: {
        title: "Disconnected Graph",

        description:
            "Tests BFS on a graph containing disconnected components.",

        graph: {
            A: ["B"],
            B: [],
            C: ["D"],
            D: []
        },

        start: "A",

        expected: ["A", "B"]
    },


    // 4. Graph with duplicate neighbors
    duplicate: {
        title: "Graph With Duplicate Neighbors",

        description:
            "Tests whether BFS correctly handles duplicate neighbours.",

        graph: {
            A: ["B", "B", "C"],
            B: ["D"],
            C: ["D"],
            D: []
        },

        start: "A",

        expected: ["A", "B", "C", "D"]
    },


    // 5. Single node graph
    single: {
        title: "Single Node Graph",

        description:
            "Tests BFS on a graph containing only one node.",

        graph: {
            A: []
        },

        start: "A",

        expected: ["A"]
    },


    // 6. Empty adjacency lists
    empty: {
        title: "Empty Adjacency Lists",

        description:
            "Tests BFS when all vertices have empty adjacency lists.",

        graph: {
            A: [],
            B: [],
            C: []
        },

        start: "A",

        expected: ["A"]
    },


    // 7. Large branching graph
    branching: {
        title: "Large Branching Graph",

        description:
            "Tests BFS on a graph with multiple branches and levels.",

        graph: {
            1: [2, 3, 4],
            2: [5, 6],
            3: [7, 8],
            4: [9],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        },

        start: 1,

        expected: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },


    // 8. Graph with self loop
    selfloop: {
        title: "Graph With Self Loop",

        description:
            "Tests whether BFS correctly handles a vertex connected to itself.",

        graph: {
            A: ["A", "B"],
            B: ["C"],
            C: []
        },

        start: "A",

        expected: ["A", "B", "C"]
    },


    // 9. Integer graph with cycle
    "integer-cycle": {
        title: "Integer Graph With Cycle",

        description:
            "Tests BFS on an integer graph containing a cycle.",

        graph: {
            1: [2, 3],
            2: [4],
            3: [4],
            4: [1, 5],
            5: []
        },

        start: 1,

        expected: [1, 2, 3, 4, 5]
    },


    // 10. Deep graph
    deep: {
        title: "Deep Graph",

        description:
            "Tests BFS on a graph containing a long chain of vertices.",

        graph: {
            1: [2],
            2: [3],
            3: [4],
            4: [5],
            5: [6],
            6: []
        },

        start: 1,

        expected: [1, 2, 3, 4, 5, 6]
    }

};


/* =========================================================
   BFS STATE
========================================================= */

let currentTest = testCases.basic;

let queue = [];

let visited = [];

let currentNode = null;

let finished = false;


/* =========================================================
   LOAD SELECTED TEST CASE
========================================================= */

function loadTestCase() {

    const selectedTest =
        document.getElementById("test-select").value;

    currentTest = testCases[selectedTest];

    if (!currentTest) {
        return;
    }


    // Update title
    document.getElementById("test-title")
        .textContent = currentTest.title;


    // Update description
    document.getElementById("test-description")
        .textContent = currentTest.description;


    // Update starting node
    document.getElementById("start-node")
        .textContent = currentTest.start;


    // Update expected output
    document.getElementById("expected-output")
        .textContent =
        `[${currentTest.expected.join(", ")}]`;


    // Display graph
    displayGraph(currentTest.graph);


    // Reset execution
    resetBFS();
}


/* =========================================================
   DISPLAY GRAPH
========================================================= */

function displayGraph(graph) {

    let graphText = "";

    for (const node in graph) {

        const neighbours = graph[node];

        if (neighbours.length === 0) {

            graphText += `${node} → -\n`;

        } else {

            graphText +=
                `${node} → ${neighbours.join(", ")}\n`;
        }
    }


    document.getElementById("input-graph")
        .textContent = graphText.trim();
}


/* =========================================================
   START BFS
========================================================= */

function runBFS() {

    resetBFS();

    queue.push(currentTest.start);

    updateUI();

    executeStep();
}


/* =========================================================
   NEXT STEP
========================================================= */

function nextStep() {

    if (finished) {
        return;
    }


    // If BFS hasn't started yet,
    // add starting node to queue.

    if (
        queue.length === 0 &&
        visited.length === 0 &&
        currentNode === null
    ) {

        queue.push(currentTest.start);
    }


    executeStep();
}


/* =========================================================
   EXECUTE ONE BFS STEP
========================================================= */

function executeStep() {

    /*
        If queue is empty, BFS is complete.
    */

    if (queue.length === 0) {

        finished = true;

        currentNode = null;

        document.getElementById("current-node")
            .textContent = "Finished";

        document.getElementById("queue")
            .textContent = "Empty";

        showResult();

        return;
    }


    /*
        Remove first element from queue.
        This is the FIFO behaviour of BFS.
    */

    currentNode = queue.shift();


    /*
        If this node has not already been visited,
        visit it.
    */

    if (!visited.includes(currentNode)) {

        visited.push(currentNode);


        /*
            Get neighbours of current node.
        */

        const neighbours =
            currentTest.graph[currentNode] || [];


        /*
            Add unvisited neighbours to queue.
        */

        neighbours.forEach(neighbour => {

            if (!visited.includes(neighbour)) {

                queue.push(neighbour);
            }

        });

    }


    updateUI();
}


/* =========================================================
   UPDATE WEBSITE
========================================================= */

function updateUI() {

    /*
        Current node
    */

    document.getElementById("current-node")
        .textContent =
        currentNode !== null
            ? currentNode
            : "-";


    /*
        Queue
    */

    document.getElementById("queue")
        .textContent =
        queue.length > 0
            ? queue.join(", ")
            : "Empty";


    /*
        Visited nodes
    */

    document.getElementById("visited")
        .textContent =
        visited.length > 0
            ? visited.join(", ")
            : "-";
}


/* =========================================================
   SHOW FINAL RESULT
========================================================= */

function showResult() {

    /*
        Convert both arrays to strings
        so that they can be compared.
    */

    const actual =
        JSON.stringify(visited);

    const expected =
        JSON.stringify(currentTest.expected);


    /*
        Display actual output
    */

    document.getElementById("actual-output")
        .textContent =
        `[${visited.join(", ")}]`;


    const result =
        document.getElementById("test-result");


    /*
        Compare actual and expected output.
    */

    if (actual === expected) {

        result.textContent =
            "✓ Test Passed — Actual output matches expected output.";

        result.className =
            "test-result passed";

    } else {

        result.textContent =
            "✗ Test Failed — Actual output does not match expected output.";

        result.className =
            "test-result failed";
    }
}


/* =========================================================
   RESET BFS
========================================================= */

function resetBFS() {

    queue = [];

    visited = [];

    currentNode = null;

    finished = false;


    /*
        Current node
    */

    document.getElementById("current-node")
        .textContent = "-";


    /*
        Starting node appears in queue
        before execution begins.
    */

    document.getElementById("queue")
        .textContent =
        currentTest.start;


    /*
        Visited
    */

    document.getElementById("visited")
        .textContent = "-";


    /*
        Actual output
    */

    document.getElementById("actual-output")
        .textContent = "-";


    /*
        Result message
    */

    document.getElementById("test-result")
        .textContent =
        "Run the test case to see the result.";

    document.getElementById("test-result")
        .className = "test-result";
}


/* =========================================================
   INITIALIZE PAGE
========================================================= */

loadTestCase();
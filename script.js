const sentences = [
  ["prospector", "Mining", "Digging", "Through layers to discover nuggets of insight."],
  ["explorer", "Navigating", "Charting", "Unknown territories to reveal hidden opportunities."],
  ["cryptographer", "Decoding", "Unlocking", "Secret codes that lead to valuable discoveries."],
  ["archaeologist", "Analysing", "Brushing", "Away layers to expose buried treasures."],
  ["detective", "Combing through", "Piecing", "Together clues to solve intricate puzzles."],
  ["surgeon", "Dissecting", "Cutting", "Through the noise to reveal critical insights."],
  ["alchemist", "Transforming", "Turning", "Raw numbers into strategic gold."],
  ["storyteller", "Unraveling", "Weaving", "Complex details into a clear, compelling narrative."],
  ["prospector", "Sifting through", "Refining", "Raw material into brilliant gems of understanding."],
  ["spelunker", "Exploring", "Venturing", "Into the depths to uncover hidden chambers of opportunity."],
  ["puzzle master", "Piecing together", "Assembling", "Fragments to form a complete picture."],
  ["linguist", "Translating", "Converting", "Complex figures into a language everyone understands."],
  ["gemologist", "Uncovering", "Identifying", "Rare insights that sparkle with potential."],
  ["miner", "Extracting", "Unearthing", "Rich veins of actionable intelligence."],
  ["sailor", "Steering through", "Navigating", "Stormy seas to reach clear, calm waters of clarity."],
  ["cartographer", "Mapping out", "Drawing", "Detailed charts of uncharted informational landscapes."],
  ["farmer", "Harvesting", "Cultivating", "Raw inputs into a bountiful yield of insights."],
  ["conductor", "Orchestrating", "Harmonizing", "Disparate notes into a symphony of clarity."],
  ["lighthouse", "Illuminating", "Guiding", "Teams safely through foggy complexities."],
  ["puzzle-Solver", "Decoding", "Fitting", "Together disparate pieces to reveal a vivid picture of opportunity."],
];

let index = 0;
let actionToggle = false;
const identityEl = document.getElementById("identity");
const action1El = document.getElementById("action1");
const action2El = document.getElementById("action2");

function updateText() {
  const [identity, action1, action2, actionFinal] = sentences[index];
  requestAnimationFrame(() => {
      action1El.classList.add("fade-out");
      
      setTimeout(() => {
          identityEl.textContent = identity;
          action1El.textContent = actionToggle ? action2 : action1;
          action2El.textContent = actionFinal;
          
          action1El.classList.remove("fade-out");
      }, 500);
  });
}

function cycleSentences() {
  updateText();
  setInterval(() => {
      actionToggle = !actionToggle;
      if (!actionToggle) {
          index = (index + 1) % sentences.length;
      }
      updateText();
  }, 3900);
}

window.onload = cycleSentences;
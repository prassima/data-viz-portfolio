const sentences = [
    ["⛏️ prospector", "mining", "digging", "through layers to discover nuggets of insight."],
    ["🧭 explorer", "navigating", "charting", "unknown territories to reveal hidden opportunities."],
    ["🔐 cryptographer", "decoding", "unlocking", "secret codes that lead to valuable discoveries."],
    ["🏺 archaeologist", "analysing", "brushing", "away layers to expose buried treasures."],
    ["🕵️ detective", "combing through", "piecing", "together clues to solve intricate puzzles."],
    ["🩺 surgeon", "dissecting", "cutting", "through the noise to reveal critical insights."],
    ["⚗️ alchemist", "transforming", "turning", "raw numbers into strategic gold."],
    ["📖 storyteller", "unraveling", "weaving", "complex details into a clear, compelling narrative."],
    ["⛏️ prospector", "sifting through", "refining", "raw material into brilliant gems of understanding."],
    ["🕳️ spelunker", "exploring", "venturing", "into the depths to uncover hidden chambers of opportunity."],
    ["🧩 puzzle master", "piecing together", "assembling", "fragments to form a complete picture."],
    ["🗣️ linguist", "translating", "converting", "complex figures into a language everyone understands."],
    ["💎 gemologist", "uncovering", "identifying", "rare insights that sparkle with potential."],
    ["⛏️ miner", "extracting", "unearthing", "rich veins of actionable intelligence."],
    ["⛵ sailor", "steering through", "navigating", "stormy seas to reach clear, calm waters of clarity."],
    ["🗺️ cartographer", "mapping out", "drawing", "detailed charts of uncharted informational landscapes."],
    ["🌾 farmer", "harvesting", "cultivating", "raw inputs into a bountiful yield of insights."],
    ["🎼 conductor", "orchestrating", "harmonizing", "disparate notes into a symphony of clarity."],
    ["🛟 lighthouse", "illuminating", "guiding", "teams safely through foggy complexities."],
    ["🧩 puzzle-solver", "decoding", "fitting", "together disparate pieces to reveal a vivid picture of opportunity."]
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
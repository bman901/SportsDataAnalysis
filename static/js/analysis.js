var sport = GetURLParameter("sport");
var chosen_league = 0;
var chosen_season = 0;
var chosen_bet = 10;
var data = {};
var analysis = {};
var perc_chart = 0;

window.onload = function () {
  if (sport.includes("-")) {
    capital_sport = sport.replace("-", " ");
  } else if (sport == "afl") {
    capital_sport = sport.toUpperCase();
  } else {
    capital_sport = sport;
  }
  FillInTitle(capital_sport);
  if (sport !== "all-sports") {
    LoadImage(sport);
  }
  clearAll();
};

$(document).ready(function () {
  $.ajax({
    url: "",
    type: "get",
    contentType: "application/json",
    data: {
      chosen_sport: sport,
    },
    success: function (response) {
      data = response.data;
      analysis = response.analysis;

      if (sport !== "all-sports") {
        CreateLeagueBtns(data);
      } else {
        loadAllSports(analysis);
      }
    },
  });
});

function GetURLParameter(sParam) {
  let sPageURL = window.location.search.substring(1);
  let sURLVariables = sPageURL.split("&");
  for (let i = 0; i < sURLVariables.length; i++) {
    let sParameterName = sURLVariables[i].split("=");
    if (sParameterName[0] == sParam) {
      return sParameterName[1];
    }
  }
}

function createRows(row_id, location, class_name = "") {
  let row = document.createElement("div");
  row.className = "row " + class_name;
  row.id = row_id;
  let body = document.getElementById(location);
  body.appendChild(row);
}

function createBtn(btn_name, btn_id, location, class_name) {
  let btn = document.createElement("button");
  btn.className = "btn " + class_name;
  btn.id = btn_id;
  btn.textContent = btn_name;
  let body = document.getElementById(location);
  body.appendChild(btn);
}

function loadAllSports(analysis) {
  createChartAllSeasons(analysis);
  allSportsAnalysis(analysis);
}

function clearAll() {
  if (sport === "all-sports") {
    document.getElementById("league_heading").innerHTML = "";
    document.getElementById("league_col").className = "";
    document.getElementById("season_col").className = "";
    document.getElementById("result_col").className = "col";
    document.getElementById("result_col").align = "center";
    document.getElementById("perc_fav").innerHTML = "";
  }
}

function TitleCase(str) {
  let splitStr = str.split(" ");
  for (var i = 0; i < splitStr.length; i++) {
    // Assign it back to the array
    splitStr[i] =
      splitStr[i].charAt(0).toUpperCase() + splitStr[i].substring(1);
  }
  // Directly return the joined string
  return splitStr.join(" ");
}

function FillInTitle(sport) {
  document.getElementById("title").innerHTML = document
    .getElementById("title")
    .innerHTML.replace("?sport?", TitleCase(sport));
}

function LoadImage(sport) {
  let sport_img = document.getElementById("sport_img");
  if (sport_img) {
    sport_img.src = `../static/img/${sport}.jpg`;
  } else {
    let image = document.createElement("IMG");
    image.id = "sport_img";
    image.className = "img-fluid d-block half-size";
    image.alt = "Image of the chosen sport";
    image.src = `../static/img/${sport}.jpg`;
    let body = document.getElementById("img-div");
    body.appendChild(image);
  }
}

function CreateLeagueBtns(data) {
  for (let i = 0; i < data.length; i++) {
    createRows(`league_row${i}`, "league_btns", "m-2");
    createBtn(
      data[i]["league_name"],
      data[i]["league_id"],
      `league_row${i}`,
      "btn-primary"
    );
  }

  GetChosenLeague();
}

function GetChosenLeague() {
  const league_btn = document.querySelectorAll(".btn-primary");

  for (let i = 0; i < league_btn.length; i++) {
    league_btn[i].addEventListener("click", function () {
      chosen_league = league_btn[i].id;
    });
    league_btn[i].addEventListener("click", function () {
      clearBetting();
      LoadAvailableSeasons(data, chosen_league);
      document.getElementById("season_text").innerHTML =
        "Choose season to review:";
      document.getElementById("perc_fav").innerHTML =
        "<-- Please choose a season to review";
    });
  }
}

// Add an All Seasons button

function LoadAvailableSeasons(data, chosen_league) {
  LoadImage(sport);
  clearGraph();
  document.getElementById("season_btns").innerHTML = "";
  for (let i = 0; i < data.length; i++) {
    if (data[i]["league_id"] == chosen_league) {
      for (let j = 0; j < data[i]["seasons"].length; j++) {
        createRows(`season_row${j}`, "season_btns", "m-2");
        createBtn(
          data[i]["seasons"][j],
          data[i]["seasons"][j],
          `season_row${j}`,
          "btn-secondary"
        );
      }
    }
  }

  GetChosenSeason();
}

function GetChosenSeason() {
  const season_btn = document.querySelectorAll(".btn-secondary");

  for (let i = 0; i < season_btn.length; i++) {
    season_btn[i].addEventListener("click", function () {
      chosen_season = season_btn[i].id;
    });
    season_btn[i].addEventListener("click", function () {
      GetAnalysisData();
    });
    season_btn[i].addEventListener("click", function () {
      createBetInputText();
      CreateBetInput();
      GetChosenBet();
    });
  }
}

function GetAnalysisData() {
  $.ajax({
    url: "",
    type: "get",
    contentType: "application/json",
    data: {
      chosen_sport: sport,
      chosen_league: chosen_league,
      chosen_season: chosen_season,
      chosen_bet: chosen_bet,
    },
    success: function (response) {
      analysis = response.analysis;
      let perc_fav = analysis["perc_fav"];
      if (perc_fav) {
        createChart(analysis);
        PercentageAnalysis(analysis);
        ReportBetting(analysis);
      }
    },
  });
}

function PercentageAnalysis(analysis) {
  let perc_fav = Math.round(analysis["perc_fav"] * 100);
  let chosen_league_name = analysis["league_name"];
  if (perc_fav) {
    document.getElementById("perc_fav").innerHTML =
      `In the ${chosen_season} season of the ${chosen_league_name}, the favourite won ${perc_fav}% of the time`;
  } else {
    document.getElementById("perc_fav").innerHTML =
      "No data for the chosen season";
  }
}

function allSportsAnalysis(analysis) {
  max = 0;
  best = 0;
  league = "";
  for (const [key, value] of Object.entries(analysis)) {
    if (value > max) {
      best = value;
      league = key;
    }
  }
  best = (best * 100).toFixed(2);
  document.getElementById("perc_fav").innerHTML =
    `${league} has the highest percentage win rate of all leagues analysed this season at ${best}%`;
}

function ReportBetting(analysis) {
  let chosen_league_name = analysis["league_name"];
  let totalWinnings = analysis["bet_on_fav"];
  let roundedWinnings = totalWinnings.toFixed(2);
  let outcome = "won";
  if (totalWinnings) {
    if (totalWinnings < 0) {
      outcome = "lost";
    }
    document.getElementById("betting_output").innerHTML =
      `If you'd bet $${chosen_bet} on the favourites in every game in the ${chosen_league_name} you would've ${outcome} $${Math.abs(
        roundedWinnings
      )}`;
  } else {
    document.getElementById("betting_output").innerHTML = "";
  }
}

function updateBetting(chosen_bet) {
  let chosen_league_name = analysis["league_name"];
  let totalWinnings = (analysis["bet_on_fav"] / 10) * chosen_bet;
  let roundedWinnings = totalWinnings.toFixed(2);
  let outcome = "won";
  if (totalWinnings) {
    if (totalWinnings < 0) {
      outcome = "lost";
    }
    document.getElementById("betting_output").innerHTML =
      `If you'd bet $${chosen_bet} on the favourites in every game in the ${chosen_league_name} you would've ${outcome} $${Math.abs(
        roundedWinnings
      )}`;
  } else {
    document.getElementById("betting_output").innerHTML = "";
  }
}

function GetChosenBet() {
  let bet_input_val = document.getElementById("bet");
  bet_input_val.addEventListener("input", function () {
    chosen_bet = bet_input_val.value;
    if (chosen_bet == "") {
      document.getElementById("betting_output").innerHTML =
        "Please enter a bet";
    } else if (chosen_bet <= 0) {
      document.getElementById("betting_output").innerHTML =
        "Please enter a positive number";
    } else {
      updateBetting(chosen_bet);
    }
  });
}

function createBetInputText() {
  bettingInputText = document.getElementById("betting_input_text");
  bettingInputText.innerHTML = "Enter amount to bet per game:";
}

function CreateBetInput() {
  if (document.getElementById("betting_input").innerHTML == "") {
    let bet_input = document.createElement("input");
    bet_input.type = "number";
    bet_input.min = "0";
    bet_input.id = "bet";
    bet_input.inputmode = "decimal";
    bet_input.pattern =
      "^\\$?(([1-9](\\d*|\\d{0,2}(,\\d{3})*))|0)(\\.\\d{1,2})?$";
    bet_input.required = "";
    bet_input.value = "10";
    bet_input.className = "";
    let body = document.getElementById("betting_input");
    body.appendChild(bet_input);
  }
}

function createChart(analysis) {
  clearGraph();
  let new_canvas = document.createElement("canvas");
  new_canvas.id = "perc_graph";
  let body = document.getElementById("canvas-div");
  body.appendChild(new_canvas);
  const ctx = document.getElementById("perc_graph");
  let perc_fav = analysis["perc_fav"] * 100;
  let sport_img = document.getElementById("sport_img");
  if (sport_img) {
    sport_img.remove();
  }

  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: [chosen_season],
      datasets: [
        {
          label: "% wins by favourites",
          data: [perc_fav],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

function createChartAllSeasons(analysis) {
  clearGraph();
  let leagues = [];
  let perc_fav = [];
  let new_canvas = document.createElement("canvas");
  new_canvas.id = "perc_graph";
  let body = document.getElementById("canvas-div");
  body.appendChild(new_canvas);
  const ctx = document.getElementById("perc_graph");
  for (const [key, value] of Object.entries(analysis)) {
    leagues.push(key);
    perc_fav.push(value * 100);
  }
  let sport_img = document.getElementById("sport_img");
  if (sport_img) {
    sport_img.remove();
  }

  const myChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: leagues,
      datasets: [
        {
          label: "% wins by favourites",
          data: perc_fav,
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}

function clearGraph() {
  let perc_graph = document.getElementById("perc_graph");
  if (perc_graph) {
    perc_graph.remove();
  }
}

function clearBetting() {
  document.getElementById("betting_input_text").innerHTML = "";
  document.getElementById("betting_input").innerHTML = "";
  document.getElementById("betting_output").innerHTML = "";
}
